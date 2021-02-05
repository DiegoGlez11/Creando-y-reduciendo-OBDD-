# Creando-y-reduciendo-OBDD-

Proyecto creado para la materia de lógica computacional

El programa es creado con Python3.

El comando de ejecucion es el siguiente
  
```python
python main.py #funcion1 #funcion2 #operacion
```
Donde ```#funcion1``` y ```#funcion2``` son funciones booleanas de las cuales se crea y reduce su OBDD y ```#operacion``` es la operacion a realizar entre OBDDs

Las funciones deben deben seguir el siguiente formato 

``` "NombreFuncion := FuncionBooleana" ```

Los operandos aceptados por FuncionBooleana son and, or, xor, not( ) y permite aislar subfunciones con ( )

Los operandos entre OBDDs son: 
1. or ```"+"```
2. and ```"."```
3. xor ```xor```
4. complemento ```"¬"```

## Ejemplo: 

```python
python main.py "f := (a or b) and c or d" "g := (a and not(c)) or d" "+"
```

El programa nos imprimirá la tabla de verdad y el OBDD reducido de ambas funciones booleanas, al final imprime el OBDD resultante de la operacion OR entre los OBDD de las dos funciones de entrada

A continuación se muestra los resultado:

```python
------------------ f := (a or b) and c or d ------------------------------------------

tabla de verdad:
{'a': '0', 'b': '0', 'c': '0', 'd': '0', 'truth': False}
{'a': '0', 'b': '0', 'c': '0', 'd': '1', 'truth': True}
{'a': '0', 'b': '0', 'c': '1', 'd': '0', 'truth': False}
{'a': '0', 'b': '0', 'c': '1', 'd': '1', 'truth': True}
{'a': '0', 'b': '1', 'c': '0', 'd': '0', 'truth': False}
{'a': '0', 'b': '1', 'c': '0', 'd': '1', 'truth': True}
{'a': '0', 'b': '1', 'c': '1', 'd': '0', 'truth': True}
{'a': '0', 'b': '1', 'c': '1', 'd': '1', 'truth': True}
{'a': '1', 'b': '0', 'c': '0', 'd': '0', 'truth': False}
{'a': '1', 'b': '0', 'c': '0', 'd': '1', 'truth': True}
{'a': '1', 'b': '0', 'c': '1', 'd': '0', 'truth': True}
{'a': '1', 'b': '0', 'c': '1', 'd': '1', 'truth': True}
{'a': '1', 'b': '1', 'c': '0', 'd': '0', 'truth': False}
{'a': '1', 'b': '1', 'c': '0', 'd': '1', 'truth': True}
{'a': '1', 'b': '1', 'c': '1', 'd': '0', 'truth': True}
{'a': '1', 'b': '1', 'c': '1', 'd': '1', 'truth': True}


--- OBDD---
[a: 0
        false->[b: 1
                false->[d: 7
                        false->[leave: 15 truth: False
                        ]
                        ,
                        true->[leave: 16 truth: True
                        ]
                ]
                ,
                true->[c: 4
                        false->[d: 7
                                false->[leave: 15 truth: False
                                ]
                                ,
                                true->[leave: 16 truth: True
                                ]
                        ]
                        ,
                        true->[leave: 16 truth: True
                        ]
                ]
        ]
        ,
        true->[c: 4
                false->[d: 7
                        false->[leave: 15 truth: False
                        ]
                        ,
                        true->[leave: 16 truth: True
                        ]
                ]
                ,
                true->[leave: 16 truth: True
                ]
        ]
]


------------------- g := (a and not(c)) or d ------------------------------------------

tabla de verdad:
{'a': '0', 'c': '0', 'd': '0', 'truth': False}
{'a': '0', 'c': '0', 'd': '1', 'truth': True}
{'a': '0', 'c': '1', 'd': '0', 'truth': False}
{'a': '0', 'c': '1', 'd': '1', 'truth': True}
{'a': '1', 'c': '0', 'd': '0', 'truth': True}
{'a': '1', 'c': '0', 'd': '1', 'truth': True}
{'a': '1', 'c': '1', 'd': '0', 'truth': False}
{'a': '1', 'c': '1', 'd': '1', 'truth': True}


--- OBDD---
[a: 0
        false->[d: 3
                false->[leave: 7 truth: False
                ]
                ,
                true->[leave: 8 truth: True
                ]
        ]
        ,
        true->[c: 2
                false->[leave: 8 truth: True
                ]
                ,
                true->[d: 3
                        false->[leave: 7 truth: False
                        ]
                        ,
                        true->[leave: 8 truth: True
                        ]
                ]
        ]
]


Table1:  ['a', 'b', 'c', 'd']
Table2:  ['a', 'c', 'd']
OrderGlobal:  ['a', 'b', 'c', 'd', 'leave']


---------- ROBDD resultante, despues de operar los OBDD de las funciones ----------
[a : 0
        false->[b : 1
                false->[d : 2
                        false->[terminal : 3 truth: 0
                        ]
                        true->[terminal : 4 truth: 1
                        ]
                ]
                true->[c : 5
                        false->[d : 2
                                false->[terminal : 3 truth: 0
                                ]
                                true->[terminal : 4 truth: 1
                                ]
                        ]
                        true->[terminal : 4 truth: 1
                        ]
                ]
        ]
        true->[terminal : 4 truth: 1
        ]
]

```
### Leyendo los OBDD

A continuación se muestra la estructura del ROBDD de la funcion ```g := (a and not(c)) or d``` para la lectura y compresión de la impresión de los ROBDD:

![image](https://drive.google.com/uc?export=view&id=1Yisjs1YL8IqAamxMsdAOqK9nCe1HjjCg)

El identificador único es usado para saber cúal nodo es al que nos referimos, con ello se puede uno percatar las conexiones de los nodos. Si se observa el 
OBDD de la funcion ```g := (a and not(c)) or d``` el nodo c y el nodo b se conectan al mismo nodo d ya que ambos nodos tienen el mismo id único.
A continuación se muestra el ROBDD resultante

![image](https://drive.google.com/uc?export=view&id=1azKQeCnlpIYoq1vBQSRWoIPt1VrrF7Da)

Tambien el ROBDD de la función ```f := (a or b) and c or d```

![image](https://drive.google.com/uc?export=view&id=1Z3gnpPiAV78Z5-i9MmH1s8Lwf03qtB-w)

y el ROBDD de la operacion de los ROBDD de las dos funciones anteriores

![image](https://drive.google.com/uc?export=view&id=1ro-dwbqWRWqnwP4AWwMhCbN4rnCY7Ih2)
