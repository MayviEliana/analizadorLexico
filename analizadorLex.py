import re
import sys
from imp_lexer import *

diccionario = {}

class Pila:

    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        return self.items.pop()

    def pilaVacia(self):
        return self.items == []


class Nodo():

    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def evaluar(arbol):
   
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    return int(arbol.valor)


def armarArbol(pila):
    
    auxPila = Pila()
    izq, der, valor = None, None, ""
    while not len(pila) == 0:

        valorT = pila.pop(0)
        valor=valorT[0]
        
        if valor in "+-*/":
            der = auxPila.desapilar()
            izq = auxPila.desapilar()
            auxPila.apilar(Nodo(valor, izq, der))
            

        elif valor.isdigit() == False:
            if diccionario.has_key(valor):
                valor = diccionario[valor][0]
                auxPila.apilar(Nodo(valor))
                
                
            else:
                auxT = pila.pop(0)
                aux=auxT[0]
                if aux == "=":
                     
                     diccionario[valor] = [evaluar(auxPila.desapilar())]

        else:
            auxPila.apilar(Nodo(valor))
    
            
def usage():
    sys.stderr.write('Usage: imp filename\n')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    filename = sys.argv[1]
    text = open(filename).read()
    tokens = imp_lex(text)
    for token in tokens :
        print token
    

    armarArbol(tokens)
    print diccionario
        
