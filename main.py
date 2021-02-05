from antlr4 import *
from ExpBoolLexer import ExpBoolLexer
from ExpBoolListener import ExpBoolListener
from ExpBoolParser import ExpBoolParser
from copy import deepcopy
import sys
import math

varTable = {}
binaryTable = []
posTable = 0
treeByLevel = {}
idUnique = 0

#Convierte un numero decimal a su formato binario
def DecimalToBinary(num):
    v1 = ""
    if num >= 1:
        v1 = DecimalToBinary(num // 2)
    v2 = str(num % 2)
    v2 += v1
    return v2
#Convierte un numero decimal a su formato binario con longitud length
def tobinary(num, length):
    b = DecimalToBinary(num)
    bOrdenada =b[::-1]
    dif = length - len(b) 
    if dif >= 0 :
        aux = ""
        for i in range(dif):
            aux += "0"
        bOrdenada = aux + bOrdenada
        return bOrdenada
    else:
        dif *= -1
        return bOrdenada[dif:]

#Clase usada para recorrer el arbol sintactico para obtener las variables implicadas en una funcion booleana
class Variables(ExpBoolListener):
    count = 0

    def exitVariableBool(self, ctx):
        global varTable
        name = ctx.getText()
        #se almacenan las variables
        try:
            a = varTable[name]
        except:
            varTable[name] = self.count
            self.count += 1

#Clase usada para evaluar un funcion booleana y obtener su tabla de verdad
class VF(ExpBoolListener):

    def exitVariableBool(self, ctx):
        global posTable
        global binaryTable
        ctx.truth = False
        name = ctx.getText()
        #se obtiene el valor de verdad
        valT = binaryTable[posTable][name]
        #print(str(posTable)+" "+name+": "+valT)
        if valT == '0':
            ctx.truth = False
        else:
            ctx.truth = True

    #operacion AND
    def exitOpANDD(self, ctx):
        global posTable

        v1 = ctx.getChild(0)
        v2 = ctx.getChild(2)

        ctx.truth = v1.truth and v2.truth
        
    #operacion OR
    def exitOpORR(self, ctx):
        v1 = ctx.getChild(0)
        v2 = ctx.getChild(2)
        
        ctx.truth = v1.truth or v2.truth

    #operacion XOR
    def exitOpXor(self, ctx):
        v1 = ctx.getChild(0)
        v2 = ctx.getChild(2)
        ctx.truth = v1.truth ^ v2.truth
    
    def exitFunctionBool(self, ctx):
        A = ctx.getChild(0).getText()
        boolFunct = ctx.getChild(2).truth
        binaryTable[posTable]["truth"] = boolFunct
    
    #Operacion NOT
    def exitOpNOT(self, ctx):
        ctx.truth = not(ctx.getChild(1).truth)
    
    #Operacion entre comillas
    def exitIntoMarks(self, ctx):
        ctx.truth = ctx.getChild(1).truth

#Clase usada para crear los BDDs
class Node:
    def __init__(self, parent, name,array, numLayer,idu):
        self.parent = parent
        self.false = None
        self.true = None
        self.name = name
        self.numlayer = numLayer
        self.id = None
        self.idUnique = idu
        if(array == None):
            self.array = {}
        else:
            self.array = array
    
    #elimina los datos y referencias del nodo y con ello python elimina el nodo
    def eraseData(self):
        self.parent = None
        self.false = None
        self.true = None
        self.name = None
        self.numlayer = None
        self.id = None
        self.array = {}

    #Inserta un nuevo nodo en el BDD
    def insert(self, variable):
        global idUnique
        if self.false == None:
            treeByLevel[self.numlayer].append(self)
            at = {self.name:"1"}
            af = {self.name:"0"}
            
            #se arma por la derecha e izquierda un array que contiene la ruta 
            #desde la raiz hasta el actual nodo
            af = concat_dic(self.array,af)
            at = concat_dic(self.array,at)

            #se crean los nuevos nodos
            self.false = Node(self, variable,af, self.numlayer + 1, idUnique)
            idUnique += 1
            self.true = Node(self, variable,at, self.numlayer + 1, idUnique)
            idUnique += 1
        else:
            self.false.insert(variable)
            self.true.insert(variable)

    #crea y calcula la ruta desde la raiz hasta cada nodo hoja
    def computeLeaves(self):
        global idUnique

        if self.false != None:
            self.false.computeLeaves()
            self.true.computeLeaves()
        else:
            treeByLevel[self.numlayer].append(self)

            at = {self.name:"1"}
            af = {self.name:"0"}

            #calculo de la ruta de la raiz a el nodo raiz
            af = concat_dic(self.array,af)
            at = concat_dic(self.array,at)
            #creacion de las hojas
            self.false = Node(self, "leave", af, self.numlayer + 1, idUnique)
            idUnique += 1
            self.true = Node(self, "leave", at, self.numlayer + 1, idUnique)
            idUnique += 1
            self.false.computeTruth()
            self.true.computeTruth()

    #calcula el valor de verdad de cada nodo hoja
    def computeTruth(self):
        global varTable
        global binaryTable

        #se busca en la tabla de verdad cual es su valor de verdad 
        #en base a la ruta del nodo raiz a nodo hoja actual
        l = len(binaryTable)
        for pos in range(l):
            data = binaryTable[pos]
            aux = True
            for key in varTable:
                d1 = data[key]
                d2 = self.array[key]
                if d1 != d2:
                    aux = False
                    break
            #se etiqueta el nodo hoja
            if aux:
                self.truth = data["truth"]
                if self.truth == True:
                    self.id = 1
                else:
                    self.id = 0
                break
    
    #Imprime el BDD, sea reducido o no
    #Num siempre debe ser mandado a llamar con 0
    #Num es el numero de espacios antes del texto que muestra el nodo
    def printTree(self, num):
        print("[",end="")

        txt = self.name+": "+str(self.idUnique)

        if self.name == "leave":
            txt += " truth: "+str(self.truth)
        print(txt)

        if self.false != None:
            printLine2(num+1,"false->")
            self.false.printTree(num +1 )
            

        if self.name != "leave":
            if self.false != None and self.true != None:
                printLine(num+1,",")
        if self.true != None:
            printLine2(num+1, "true->")
            self.true.printTree(num + 1)

        printLine(num, "]")
    
    #Crea una copia del BDD
    def newCopy(self):
        nodeThis = deepcopy(self)

        if self.false != None:
            nodeThis.false = self.false.newCopy()

        if self.true != None:
            nodeThis.true = self.true.newCopy()

        return nodeThis

#se usa para imprimir el BDD
#Num es el nuero de espacios que hay antes del texto 
def printLine(num, txt):
    a = ""
    for i in range(num): a+="\t"
    print(a+txt)
def printLine2(num, txt):
    for i in range(num): print("\t",end="")
    print(txt,end="")

#Clase que guarda un ROBDD
class OrderedBDD:
    truthTable = None
    varTableOrder = None
    varTableName = None
    ROBDD = None
    treeLevel = None

#Crea un BDD
def createBDD():
    global treeByLevel
    global idUnique
    idUnique = 0

    root = None
    #se instancia el array que guarda por nivel
    treeByLevel = [None]*len(varTable)
    for m in range(len(varTable)):
        treeByLevel[m] = []
    
    #se crea el OBDD
    for key in varTable:
        if root == None:
            root = Node(None, key, None, 0, idUnique)
            idUnique += 1
        else:
            root.insert(key)

    #se crean los nodos hoja
    root.computeLeaves()
    return root

#concatena dos diccionarios
def concat_dic(d1, d2):
    d3 = {}
    for d in (d1,d2):
        d3.update(d)
    return d3

#reduce un BDD
#Primera version: Ademas de estar enlazado los nodos por la rama true y false, se tiene un array bidimencional
# que guarda las referencias de los nodos por nivel
def reduce(BDD):
    global treeByLevel
    one = None
    zero = None
    one1 = None
    zero1 = None

    #aplicando c1
    for i in range(len(treeByLevel[-1])):
        node = treeByLevel[-1][i]
        if node.false.truth == False:
            if zero == None:
                zero = node.false
            else:
                node.false = zero
        else:
            if one == None:
                one = node.false
            else:
                node.false = one
        
        if node.true.truth == False:
            if zero1 == None:
                zero1 = node.true
            else:
                node.true = zero1
        else:
            if one1 == None:
                one1 = node.true
            else:
                node.true = one1

    n = len(treeByLevel)-1
    while n >= 0:
        m = 0
        #aplicando C2
        while m < len(treeByLevel[n]):
            node = treeByLevel[n][m]
            id1 = node.false.id
            id2 = node.true.id
            if id1 == id2:
                #identificar rama del padre
                if node.parent.false == node:
                    node.parent.false = node.true
                else: 
                    node.parent.true = node.true
                node.parent.id = id1
                #se elimina el nodo actual
                node.eraseData()            
            else:
                node.id = str(id1)+str(id2)

            m += 1

        #aplicando C3
        m = 0
        while m < len(treeByLevel[n]):
            node1 = treeByLevel[n][m]
            if node1.true != None:
                id11 = node1.true.id
                id12 = node1.false.id

                k = m+1
                while k < len(treeByLevel[n]):
                    node2 = treeByLevel[n][k]
                    
                    if node2.true != None:
                        id21 = node2.true.id
                        id22 = node2.false.id
                        if id11 == id21 and id12 == id22:
                            #identificando rama del padre
                            if node2.parent.false == node2:
                                node2.parent.false = node1
                            else: 
                                node2.parent.true = node1
                            node2.eraseData()
                    k += 1
            m += 1
        n -= 1

    return treeByLevel

#Clase que realiza la memorizacion entre dos ROBDD
#Realiza la operacion entre dos ROBDD
class Memoisation:

    def __init__(self, OBDD1, OBDD2, order, num, tbl,parent):
        self.obdd1 = OBDD1
        self.obdd2 = OBDD2
        self.true = None
        self.false = None
        self.name = None
        self.order = order
        self.treeByLevel = tbl
        self.id = None
        self.level = num
        self.idUnique = None
        self.parent = parent
    
    #Realiza el apply sobre el arbol de memorizacion, creado por la operacion de dos ROBDD
    def memorizar(self, op):
        global idUnique
        idUnique = 0
        if op == "+" or op == "." or op == "xor":
            robdd1 = self.obdd1.ROBDD
            robdd2 = self.obdd2.ROBDD
        else:
            if op == "¬":
                robdd1 = self.obdd1.ROBDD
                robdd2 = self.obdd1.ROBDD
            else:
                print("Operacion invalida ", op)
                exit()

        self.apply(op,robdd1, robdd2,0)

    def apply(self, op, node1, node2, num):
        global idUnique
        self.idUnique = idUnique
        idUnique += 1

        #guardamos el nombre de los nodos con los cuales se esta operando
        self.name = "("+node1.name+","+node2.name+")"

        if self.name == "(leave,leave)":
            self.treeByLevel.append(self)
        
        if node1.name in self.order:
            pos1 = self.order[node1.name]
        if node2.name in self.order:
            pos2 = self.order[node2.name]

        #se verifica si son hojas
        #si son hojas se opera con ellos
        if node1.name == "leave" and node2.name == "leave":
            self.var = "terminal"
            if op == "+":
                self.truth = int(node1.truth or node2.truth)
            if op == ".":
                self.truth = int(node1.truth and node2.truth)
            if op == "xor":
                self.truth = int(node1.truth ^ node2.truth)
            if op == "¬":
                #aux1 = (node1.truth and not True) or (not node1.truth and True)
                aux1 = node1.truth ^ 1
                self.truth = int(aux1)
            self.id = str(self.truth)
            return
        
        #los nodos pertenecen al mismo nivel i
        if pos1 == pos2:
            self.var = node1.name
            self.true = Memoisation(self.obdd1,self.obdd2, self.order, num+1,self.treeByLevel,self)
            self.false = Memoisation(self.obdd1,self.obdd2, self.order, num+1,self.treeByLevel,self)
            #Se llama apply() con el lado falso y true de los dos nodos actuales
            self.false.apply(op, node1.false, node2.false, num+1)
            self.true.apply(op, node1.true, node2.true, num+1)
            return
        
        #difieren de nivel los nodos
        #el numero de nivel es ascendente, el nodo raiz es el cero y el nodo hoja es el N

        #el nodo1 esta un nivel mas abajo que el nodo 2
        if pos1 > pos2:
            self.var = node2.name
            self.true = Memoisation(self.obdd1,self.obdd2, self.order, num+1,self.treeByLevel,self)
            self.false = Memoisation(self.obdd1,self.obdd2, self.order, num+1,self.treeByLevel,self)
            #El nodo 1 esta en un nivel mas abajo que el nodo 2, por lo tanto el nodo1 debe quedarse igual y nodo2
            #debe avanzar un nivel mas abajo por el lado falso y verdadero
            self.false.apply(op, node1, node2.false, num+1)
            self.true.apply(op, node1, node2.true, num+1)
            return
        #el nodo1 esta un nivel mas arriba que el nodo 2
        if pos1 < pos2:
            self.var = node1.name
            self.true = Memoisation(self.obdd1,self.obdd2, self.order, num+1,self.treeByLevel,self)
            self.false = Memoisation(self.obdd1,self.obdd2, self.order, num+1,self.treeByLevel,self)
            #El nodo 1 esta en un nivel mas arriba que el nodo 2, por lo tanto el nodo2 debe quedarse igual y nodo1
            #debe avanzar un nivel mas abajo por el lado falso y verdadero
            self.false.apply(op, node1.false, node2, num+1)
            self.true.apply(op, node1.true, node2, num+1)
            return
    
    #reduce el arbol generado por la memorizacion de dos OBDD
    def reduce(self):
        nodeParent = {}
        #etiquetado de los nodos hoja
        for node in self.treeByLevel:
            if node.truth:
                node.id = "1"
            else:
                node.id = "0"
            #guardamos los nodo padre de las hojas
            nodeParent[node.parent.idUnique] = node.parent

        self.reduceOp(nodeParent)

    #Algoritmo de reduccion de un OBDD. 
    #Version 2: Se procede de manera recursiva
    def reduceOp(self, parent):
        parent2 = {}
        Zero = None
        One = None

        for key in parent:
            node = parent[key]
            if node.level != None and node.false.id != None and node.true.id != None:
                #etiquetado
                node.id = node.false.id + node.true.id
                
                #aplicando regla c1
                if node.false.name == "(leave,leave)":
                    if node.false.truth == 0:
                        if Zero == None:
                            Zero = node.false
                        else:
                            node.false = Zero
                    else:
                        if One == None:
                            One = node.false
                        else:
                            node.false = One
                if node.true.name == "(leave,leave)":
                    if node.true.truth == 0:
                        if Zero == None:
                            Zero = node.true
                        else:
                            node.true = Zero
                    else:
                        if One == None:
                            One = node.true
                        else:
                            node.true = One
                
                #aplicando regla c2
                if node.true.id == node.false.id:
                    #identificando de que rama del padre pertenece el nodo actual
                    if node.parent.false == node:
                        node.parent.false = node.false
                    else:
                        node.parent.true = node.false
                    #se guarda el nodo padre del nodo actual, para que en la siguiente 
                    #llamada recursiva se le apliquen las reglas de reduccion
                    parent2[node.parent.idUnique] = node.parent
                    #se borra el nodo
                    node.eraseData()

                #aplicando regla C3
                #se busca en todos los nodos del actual nivel, si alguno posee los mismos id que el nodo actual
                for key2 in parent:
                    if key != key2 and parent[key2].level != None and parent[key].level != None:
                        node2 = parent[key2]
                        #identificando de que rama del padre pertenece el nodo actual
                        if node.true.id == node2.true.id and node.false.id == node2.false.id:
                            #se guarda el nodo padre del nodo actual, para que en la siguiente 
                            #llamada recursiva se le apliquen las reglas de reduccion
                            parent2[node2.parent.idUnique] = node2.parent
                            #identificando al padre
                            if node2.parent.false == node2:
                                    node2.parent.false = node
                            else:
                                node.parent.true = node
                            #se borra el nodo
                            node2.eraseData()
            
        #guardamos los padres de los nodos a los cuales no se les aplico ninguna de las reglas de reduccion
        for n in parent:
            p = parent[n]
            if p.id != None and p.parent != None:
                parent2[p.parent.idUnique] = p.parent

        del parent
        if len(parent2) > 0:
            #llamada recursiva con los padres de los nodos actuales
            self.reduceOp(parent2)

    #borra todos los miembros del nodo
    def eraseData(self):
        self.obdd1 = None
        self.obdd2 = None
        self.true = None
        self.false = None
        self.order = None
        self.treeByLevel = None
        self.id = None
        self.level = None
        self.parent = None

    #imprime el arbol generado tras la memorizacion entre dos OBDD, el arbol puede estar 
    #sin reducir o reducido
    def printMemoisation(self, num):
        print("[",end="")

        txt = self.var+" : "+str(self.idUnique)
        if self.name == "(leave,leave)":
            txt += " truth: "+str(self.truth)
        print(txt)

        if self.false != None:
            printLine2(num+1,"false->")
            self.false.printMemoisation(num+1)
        
        if self.true != None:
            printLine2(num+1,"true->")
            self.true.printMemoisation(num+1)
        
        printLine(num, "]")

#Crea una tabla de verdad de uan funcion booleana
def bdd2tabla(input):
    global varTable
    global binaryTable
    global posTable

    inputStream = InputStream(input)
    lexer = ExpBoolLexer(inputStream)
    stream = CommonTokenStream(lexer)
    parser = ExpBoolParser(stream)
    tree = parser.funtion()
    walker = ParseTreeWalker()

    #calculamos las variables
    varTable = {}
    printer = Variables()
    walker.walk(printer, tree)

    #orden de las variables
    orderVarTable = [None]*len(varTable)
    for key in varTable:
        pos = varTable[key]
        orderVarTable[pos] = key

    #tabla con numeros binarios de tamanio pow(2,numVars)
    #Cada digito binario es el valor de verdad de una variable booleana
    binaryTable = []
    numVars = len(varTable) 
    lim = int(math.pow(2,numVars))
    for i in range(lim):
        bn = tobinary(i,numVars)
        aux = {}
        for key in varTable:
            char = bn[varTable[key]]
            aux[key] = char
        binaryTable.append(aux)
    
    #se recorre la tabla y cada numero binario es usado 
    #para saber el valor de verdad de la expresion booleana
    posTable = 0
    numTable = len(binaryTable)
    truth = VF()
    while(posTable < numTable):
        #se calcula el valor de verdad
        walker.walk(truth,tree)
        posTable += 1

    #se crea el BDD con su tabla de verdad e informacion respectiva
    table = OrderedBDD()
    table.truthTable = binaryTable.copy()
    table.varTableOrder = orderVarTable.copy()
    table.varTableName = varTable.copy()
    return table

#crea un BDD y lo reduce.
#recibe como parametro el objeto devuelto por la funcion bdd2tabla()
def expr2bdd(BDDin):
    #se crea el BDD
    BDD = createBDD()
    OBDDLevel = reduce(BDD)

    #se limpian los nodos de cada nivel
    for level in range(len(OBDDLevel)):
        #se eliminan los nodos sin referencias de cada nivel
        i = 0
        while i < len(OBDDLevel[level]):
            name = OBDDLevel[level][i]
            if name == None:
                del OBDDLevel[level][i]
                i -= 1
            i += 1
    #se verifica si hay niveles sin nodos
    level = 0
    while i < len(OBDDLevel):
        if len(OBDDLevel[level]) == 0:
            del OBDDLevel[level]
            level -= 1
        level += 1
    #actualizamos el nivel de los nodos
    for i in range(len(OBDDLevel)):
        for j in range(len(OBDDLevel[i])):
            OBDDLevel[i][j].numlayer = i
        
    BDDin.treeLevel = OBDDLevel.copy()
    BDDin.ROBDD = OBDDLevel[0][0].newCopy()
    return BDDin

if __name__ == '__main__':
    print("\n\n------------------ "+sys.argv[1]+" ------------------------------------------\n\n")
    #calculo de la tabla de verdad de la primera funcion booleana
    table = bdd2tabla(sys.argv[1])
    #impresion de la tabla
    for i in range(len(table.truthTable)):
        print(table.truthTable[i])
    #calcula el OBDD reducido
    ROBDD1 = expr2bdd(table)
    print("--- OBDD---\n\n")
    ROBDD1.ROBDD.printTree(0) 

    print("\n\n------------------- "+sys.argv[2]+" ------------------------------------------\n\n")
    #calculo de la tabla de la segunda expresion
    table2 = bdd2tabla(sys.argv[2])
    #impresion de la tabla
    for i in range(len(table2.truthTable)):
        print(table2.truthTable[i])
    #calcula el OBDD reducido
    ROBDD2 = expr2bdd(table2)
    print("--- OBDD---\n\n")
    ROBDD2.ROBDD.printTree(0) 
    
    #sacamos las variables comunes entre OBDDs
    common = {}
    for key in ROBDD1.varTableName:
        try:
            v1 = ROBDD1.varTableName[key]
            v2 = ROBDD2.varTableName[key]
            common[key] = key
        except:
            continue
    #se extrae el orden de las variables
    o1 = []
    for i in range(len(ROBDD1.varTableOrder)):
        key = ROBDD1.varTableOrder[i]
        if key in common:
            o1.append(key)
    
    o2 = []
    for i in range(len(ROBDD2.varTableOrder)):
        key = ROBDD2.varTableOrder[i]
        if key in common:
            o2.append(key)
    
    #se compruba que el orden sea igual de ambas funciones booleanas
    for i in range(len(o1)):
        v1 = o1[i]
        v2 = o2[i]
        if v1 != v2:
            print("\n\nOBDD\'s con orden disparejo, variables comunes no concuerdan")
            print("OBDD1 ",end="")
            print(o1)
            print("OBDD2 ",end="")
            print(o2)
            exit()

    #orden global, se usa para saber como operar con dos OBDDs
    orderGlobal = []
    if len(o1) > 0:
        for i in range(len(o1)):
            if i == 0:
                pos1 = ROBDD1.varTableName[o1[i]]
                a1 = ROBDD1.varTableOrder[:pos1]
                pos2 = ROBDD2.varTableName[o1[i]]
                a2 = ROBDD2.varTableOrder[:pos2]

                orderGlobal += a1+a2
            else:
                pos11 = ROBDD1.varTableName[o1[i-1]]+1
                pos12 = ROBDD1.varTableName[o1[i]]
                a1 = ROBDD1.varTableOrder[pos11:pos12]

                pos21 = ROBDD2.varTableName[o1[i-1]]+1
                pos22 = ROBDD2.varTableName[o1[i]]
                a2 = ROBDD2.varTableOrder[pos21:pos22]

                orderGlobal += a1+a2
            orderGlobal += [o1[i]]

        #variables restantes
        pos1 = ROBDD1.varTableName[o1[-1]]
        if pos1 < len(ROBDD1.varTableOrder)-1:
            pos1+=1
            orderGlobal += ROBDD1.varTableOrder[pos1:]
        pos2 = ROBDD2.varTableName[o1[-1]]
        if pos2 < len(ROBDD2.varTableOrder)-1:
            pos2 +=1
            orderGlobal += ROBDD2.varTableOrder[pos2:]
        
    else:
        for i in ROBDD1.varTableOrder:
            orderGlobal.append(i)
        for j in ROBDD2.varTableOrder:
            orderGlobal.append(j)
    orderGlobal.append("leave")
            
    #conversion a dic
    dicOrder = {}
    for pos in range(len(orderGlobal)):
        dicOrder[orderGlobal[pos]] = pos

    print("\n\nTable1: ",ROBDD1.varTableOrder)
    print("Table2: ",ROBDD2.varTableOrder)
    print("OrderGlobal: ",orderGlobal)
    #print(dicOrder)
    
    #memorizacion, crea el OBDD en base a las operaciones de dos OBDD
    l = []
    memo = Memoisation(ROBDD1, ROBDD2, dicOrder,0,l,None)
    memo.memorizar(sys.argv[3])
    print("\n\n---------- ROBDD resultante, despues de operar los OBDD de las funciones ----------")
    #Se reduce el OBDD
    memo.reduce()
    #Se imprime
    memo.printMemoisation(0)

   