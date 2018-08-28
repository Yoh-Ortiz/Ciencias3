from pila import *
from arbol import *


def tupla(valor, letra):
    tuplas_enc.append((letra, valor))

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-/*=":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)

         

def evaluar(arbol):
    conjunto= "abc"
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor in conjunto:
         for i in range(len(tuplas_enc)):
            if tuplas_enc[i][0] == arbol.valor:
                return tuplas_enc[i][1]
    if arbol.valor == "=":
        return tupla(evaluar(arbol.izq), arbol.der.valor)
    return int(arbol.valor)

pilaEnc = Pila()
resp = []
tuplas_enc =[]
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
        
        
arc_salida=open("expresiones.out","w")
for i in range(0,len(tuplas_enc)):
    arc_salida.write(tuplas_enc[i][0]+"="+str(tuplas_enc[i][1])+"\n")
    
arc_salida.close()
print (tuplas_enc)
