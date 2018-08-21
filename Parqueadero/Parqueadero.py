import Moto as vehiculo
import cola as col

colaEnc = col.Cola()

def imprimirCola(colaEnc):
    for i in range(0,len(colaEnc.items)):
        print("Placa: " + colaEnc.items[i].placa + " Ficha: " + colaEnc.items[i].FichaPropiedad +" Horario: "+ colaEnc.items[i].Horario + " Código: "+ colaEnc.items[i].CodigoCarnet)

def borrarAtendido():
    contador = len(colaEnc.items)   
    moto = colaEnc.desencolar()
    print("Placa: " + moto.placa + " Ficha: " + moto.FichaPropiedad +" Horario: "+ moto.Horario + " Código: "+ moto.CodigoCarnet)
if __name__== "__main__":
        print("Menu Principal")
        while True:
                opcion = int(input(" 1. Agregar Vehiculo \n 2. Mostrar Vehiculos \n 3. Atender \n "))
                print("Accion:",opcion)
                if opcion==1:
                      placa  = input("\n Ingrese placa: ")  
                      ficha_prop = input("\n Ingrese su ficha de propiedad: ")
                      horario = input("\n Ingrese horario entrada: ")
                      codigo = input("\n Ingrese código carnet: ")
                      moto = vehiculo.Moto(placa,ficha_prop,horario,codigo)
                      colaEnc.encolar(moto)
                elif opcion==2:
                     imprimirCola(colaEnc)
                elif opcion==3:
                     borrarAtendido()
       


