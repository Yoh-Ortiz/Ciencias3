import Libro as lib
import cola as col

colaEnc = col.Cola()
colaAux = col.Cola()
colaCarg = col.Cola()

archivo = open("libros.csv", "r")
lista = [(x.split(";")[0],x.split(";")[1],x.split(";")[2]) for x in archivo.readlines()]
for x in lista:
        libro_pro = lib.Libro(x[0],x[1],x[2])
        colaCarg.encolar(libro_pro)

def busqueda_titulo(titulo):
      while colaCarg.es_vacia()==False:
              elemento = colaCarg.desencolar()
              if elemento.titulo == titulo:
                  colaEnc.encolar(elemento)
              else:
                   colaAux.encolar(elemento)
              if colaCarg.es_vacia():
                  break

def busqueda_autor(autor):
  while colaCarg.es_vacia()==False:
       elemento = colaCarg.desencolar()
       if elemento.autor == autor:
           colaEnc.encolar(elemento)
       else:
               colaAux.encolar(elemento)
       if colaCarg.es_vacia():
              break

def busqueda_genero(genero):
  while colaCarg.es_vacia()==False:
       elemento = colaCarg.desencolar()
       if  elemento.genero == genero: 
              colaEnc.encolar(elemento)
       else:
               colaAux.encolar(elemento)
       if colaCarg.es_vacia():
              break

def imprimirCola():
    contador = len(colaEnc.items)
    #print (contador)
    while contador != 0:
        libroAux = colaEnc.desencolar()
        print("Autor Obra: " + libroAux.autor + " Titulo Obra: " + libroAux.titulo +" Genero Obra: "+ libroAux.genero)
        contador = contador - 1
        if contador == 0:
            break


if __name__== "__main__":
        print("Menu Principal")
        opcion = int(input(" 1. Mostrar todos los libros \n 2. Extraer libro por título \n 3. Extraer libros por autor \n 4. Extraer libros por categoría\n"))
        print("Accion:",opcion)
        if opcion==1:
            while colaCarg.es_vacia() != True:
                print(colaCarg.desencolar().titulo)
        elif opcion==2:
             busqueda_titulo("El buit")
             imprimirCola()
        elif opcion==3:
             busqueda_autor("Anna Llenas\n")
             imprimirCola()
        elif opcion==4:
             busqueda_genero("relatos")
             imprimirCola()
       


