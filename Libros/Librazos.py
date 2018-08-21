import Libro as lib
import pila as pil

pilaEnc = pil.Pila()
pilaAux = pil.Pila()
pilaCarg = pil.Pila()

archivo = open("libros.csv", "r")
lista = [(x.split(";")[0],x.split(";")[1],x.strip("\n").split(";")[2]) for x in archivo.readlines()]
for x in lista:
        libro_pro = lib.Libro(x[0],x[1],x[2])
        pilaCarg.apilar(libro_pro)

def busqueda_titulo(titulo):
      while pilaCarg.es_vacia()==False:
              elemento = pilaCarg.desapilar()
              if elemento.titulo == titulo:
                  pilaEnc.apilar(elemento)
              else:
                   pilaAux.apilar(elemento)
                   pilaAux==pilaCarg
              if pilaCarg.es_vacia():
                  break

def busqueda_genero(genero):
          while pilaCarg.es_vacia()==False:
               elemento = pilaCarg.desapilar()
               if  elemento.genero == genero: 
                      pilaEnc.apilar(elemento)
               else:
                       pilaAux.apilar(elemento)
                       pilaAux==pilaCarg
               if pilaCarg.es_vacia():
                      break
        
def busqueda_autor(autor):
          while pilaCarg.es_vacia()==False:
               elemento = pilaCarg.desapilar()
               if elemento.autor == autor:
                   pilaEnc.apilar(elemento)
               else:
                       pilaAux.apilar(elemento)
                       pilaAux==pilaCarg
               if pilaCarg.es_vacia():
                      break
        
def imprimirPilaNew(pilaEnc):
    for i in range(0,len(pilaEnc.items)):
        print("Titulo: " + pilaEnc.items[i].titulo + " Genero: " + pilaEnc.items[i].genero +" Autor: "+ pilaEnc.items[i].autor)
        
def imprimirPila():
    contador = len(pilaEnc.items)
    while contador != 0:
        libroAux = pilaEnc.desapilar()
        print("Autor Obra: " + libroAux.autor + ". Titulo Obra: " + libroAux.titulo +". Genero Obra: "+ libroAux.genero+".")
        contador = contador - 1
        if contador == 0:
            break


if __name__== "__main__":
        while True:
                print("Menu Principal, libros")
                opcion = int(input(" 1. Mostrar todos los libros \n 2. Extraer libro por título \n 3. Extraer libros por autor \n 4. Extraer libros por categoría\n 5. Salir\n Escriba su opcion: "))
                if opcion==1:
                        imprimirPilaNew(pilaCarg)
                elif opcion==2:
                        tit = str(input("Escriba el título del libro a buscar: "))
                        busqueda_titulo(tit)
                        imprimirPila()
                elif opcion==3:
                        aut = str(input("Escriba el autor del libro(s) a buscar: "))
                        busqueda_autor(aut)
                        imprimirPila()
                elif opcion==4:
                        gen = str(input("Escriba el genero de libros a buscar: " ))
                        busqueda_genero(gen)
                        imprimirPila()
                elif opcion==5:
                        break
