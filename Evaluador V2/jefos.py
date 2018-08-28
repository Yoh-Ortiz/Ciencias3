from pila import *
from arbol import *

def tupla(valor, letra):
    rtasTuplas.append((letra, valor))

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
    abc = "abcdefghijklmnopqrstuvwxyz"
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor in abc:
        for i in range(len(rtasTuplas)):
            if rtasTuplas[i][0] == arbol.valor:
                return rtasTuplas[i][1]
    if arbol.valor == "=":
        return tupla(evaluar(arbol.izq), arbol.der.valor)
    return int(arbol.valor)
    
pila = Pila()

rtasTuplas=[]

archivoEntrada = open("expresiones.in", "r")
lineasArchivo = archivoEntrada.readlines()

for lineas in lineasArchivo:
    lineas = lineas.strip("\n")
    print(lineas.split(" "))
    convertir(lineas.split(" "), pila)
    evaluar(pila.desapilar())

archivoSalida=open("expresiones.out","w")


for i in range(len(rtasTuplas)):
    archivoSalida.write(rtasTuplas[i][0]+" = " + str(rtasTuplas[i][1]) +"\n")
    
archivoSalida.close()
print (rtasTuplas)
