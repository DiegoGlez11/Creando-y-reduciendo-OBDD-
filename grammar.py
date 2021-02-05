from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarListener import GrammarListener
from GrammarParser import GrammarParser
import sys

class ErrorDetected(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        if self.msg: 
            return " {0}".format(self.msg)
        else:
            return "Error al detectar el String"

class GrammarPrintListener(GrammarListener):

    def exitArticulo(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["T"] = " "
        ctx.data["G"] = " "

        if(txt == "un"):
            ctx.data["T"] = "sing"
            ctx.data["G"] = "masc"
        
        if(txt == "las"):
            ctx.data["T"] = "plur"
            ctx.data["G"] = "fem"

        if(txt == "unos"):
            ctx.data["T"] = "plur"
            ctx.data["G"] = "fem"
        print("Articulo ", ctx.data, txt)

    def exitSustantivo(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["T"] = " "
        ctx.data["G"] = " "
        ctx.data["C"] = " "

        if(txt == "ninio"):
            ctx.data["T"] = "sing"
            ctx.data["G"] = "masc"
            ctx.data["C"] = "sust"
        
        if(txt == "monstruos"):
            ctx.data["T"] = "plur"
            ctx.data["G"] = "masc"
            ctx.data["C"] = "sust"

        if(txt == "arbol"):
            ctx.data["T"] = "sing"
            ctx.data["G"] = "masc"
            ctx.data["C"] = "sust"
        
        if(txt == "galletas"):
            ctx.data["T"] = "plur"
            ctx.data["G"] = "fem"
            ctx.data["C"] = "sust"

        print("sustantivo ", ctx.data, txt)

    def exitVerbo(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["L"] = " "
        ctx.data["J"] = " "
        T = ctx.parentCtx.getChild(1).data["T"]
        C = ctx.parentCtx.getChild(1).data["C"]

        if(T == "sing" and C == "sust"):
            ctx.data["L"] = "sing"
            ctx.data["J"] = "sust"
        
        if(T == "plur" and C == "conj"):
            ctx.data["L"] = "plur"
            ctx.data["J"] = "conj"

        if(T == "sing" and C == "pronom"):
            ctx.data["L"] = "sing"
            ctx.data["J"] = "pronom"
        
        if(T == "plur" and C == "sust"):
            ctx.data["L"] = "plur"
            ctx.data["J"] = "sust"
        print("Verbo ", ctx.data, txt)
    
    def exitPreposicion(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["p"] = " "
        if(txt == "a"):
            ctx.data["P"] = "prep"
        else:
            ctx.data["P"] = " "
        print("Preposicion ", ctx.data, txt)

    def exitPronombre(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["T"] = "sing"
        ctx.data["G"] = "pronom"
        print( "Pronombre ", ctx.data, txt)

    def exitSujeto(self, ctx):
        txt = ctx.getText()
        art = ctx.getChild(0)
        susta = ctx.getChild(1)
        ctx.data = {}
        ctx.data["Es"] = " "
        ctx.data["T"] = " "
        T = art.data["T"]
        G = art.data["G"]
        if(T == susta.data["T"] and G == susta.data["G"]):
            ctx.data["Es"] = susta.data["C"]
            ctx.data["T"] = art.data["T"]
        print ("Sujeto ", ctx.data, txt)
    
    def exitConjuncion(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["T"] = " "
        ctx.data["C"] = " "


        G = ctx.parentCtx.getChild(0).data["G"]
        N = ctx.parentCtx.getChild(0).data["T"]
       
        if(ctx.getChildCount() == 2):
            tx = ctx.getChild(1).getText()
            if(G == "pronom"):
                if(tx != "yo"):
                    ctx.data["T"] = "plur"
                    ctx.data["C"] = "conj"
            else:
                if(tx == "yo"):
                    ctx.data["T"] = "plur"
                    ctx.data["C"] = "conj"
        else:
            if(G == "pronom"):
                ctx.data["T"] = "sing"
                ctx.data["C"] = "pronom"
            else:
                ctx.data["T"] = N
                ctx.data["C"] = G
        print ("Conjuncion",ctx.data, txt)
    
    def exitSujetoIni(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["T"] = ctx.getChild(0).data["T"]
        if(ctx.getChild(0).getText() == "yo"):
            ctx.data["G"] = ctx.getChild(0).data["G"]
        else:
            ctx.data["G"] = ctx.getChild(0).data["Es"]
        print("SujetoIni ", ctx.data, txt)


    def exitSujetoFin(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        conj = ctx.parentCtx.getChild(1)
        prepo = ctx.parentCtx.getChild(3)
        ctx.data["salida"] = "false"

        if(conj.data["T"] == "plur" and conj.data["C"] == "pronom"):
            if(ctx.getChild(0).data["C"] == "sust" and ctx.getChild(0).data["T"] == conj.data["T"]):
                ctx.data["salida"] = "true"
                return

        if(conj.data["T"] == "plur" and conj.data["C"] == "sust" and prepo.data["P"] != "prep"):
            if(ctx.getChild(0).data["C"] == "sust" and ctx.getChild(0).data["T"] == conj.data["T"]):
                ctx.data["salida"] = "true"
                return   
        
        ctx.data["salida"] = "true"
        print("SujetoFin ", ctx.data, txt)


    def exitPronombre(self, ctx):
        txt = ctx.getText()
        ctx.data = {}
        ctx.data["T"] = "sing"
        ctx.data["G"] = "pronom" 
        print ("Pronombre ", ctx.data, txt  )
    
    def exitOracion(self, ctx):
        if(ctx.getChild(4).data["salida"] == "true"):
            print ("Aceptado")
        else:
            print ("Rechazado")

        
def main(argv):
    inputStream = InputStream(argv[1])
    lexer = GrammarLexer(inputStream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.oracion()
    printer = GrammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)