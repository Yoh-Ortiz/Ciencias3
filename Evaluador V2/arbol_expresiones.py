from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/=":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "=":
        return evaluar(arbol.izq)
    return int(arbol.valor)

class diccionario():
    def __init__(self, lista=None):
        self.lista=[]
    def agregar(string,int):
        self.lista.append((string,int))

dic = diccionario()
pilaEnc = Pila()
resp = []

archivo = open("expresiones.in", "r")
lista = []
lista_esc =[]
for x in  archivo.readlines():
    lista.append(x.strip("\n"))
archivo.close()
for x in lista:
        exp = x.split(" ")
        convertir(exp, pilaEnc)
        respuesta =(evaluar(pilaEnc.desapilar()))
        print(respuesta)
        lista_esc.append(str(respuesta))

arc_salida=open("expresiones.out","w")
for i in range(0,len(lista_esc)):
    arc_salida.write(lista_esc[i]+"\n")
    
arc_salida.close()
