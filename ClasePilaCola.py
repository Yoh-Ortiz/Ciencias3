class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []


class Libro:

    def __init__(self,titulo,autor,genero):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        
class Moto ():
    placa = ""
    FichaPropiedad = ""
    Horario = ""
    CodigoCarnet = ""

cola = Cola()
archivo = open("libros.csv", "r")
lista = [(x.split(";")[0],x.split(";")[1],x.split(";")[2]) for x in archivo.readlines()]
for x in lista:
        cola.encolar(x)
print(archivo.read(5))
while True:
    opcion = int(input(" 1. Mostrar todos los libros \n 2.Extraer libro por título \n 3. Extraer libros por autor \n 4. Extraer libros por categoría \n 5. consultar libros extraidos \n 6. apilar libros extraidos \n 7. Salir \n"))
    print("Accion:",opcion)
    if (opcion==4):
        break
    elif opcion==1:
        while cola.es_vacia() != True:
                print(cola.desencolar())
    elif opcion==2:
        colaTitulos = Cola()
        print(cola.items)
    elif opcion==3:
        colaAutores = Cola()
        print(cola.items)
    elif opcion==4:
        colaCategoria = Cola()
        print(cola.items)
    elif opcion==6:
        archivo = open("libros.csv", "r")
        lista = [(x.split(";")[0],x.split(";")[1],x.split(";")[2]) for x in archivo.readlines()]
        for x in lista:
            cola.encolar(x)
