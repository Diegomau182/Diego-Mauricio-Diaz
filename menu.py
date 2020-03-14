#-*-UTF-8-*-
#Nombre:menu.py
#objetivo:Establece el menu donde mandara a llamar todas funciones
#Creador:Diego Diaz
#Fecha:13/03/2020
import sys
import os
import platform
from service_parking import Service_parking
class Menu:
    """
    se mandan a llamar todas las funciones del servicio
    y se agregan otras mas
    """
    def __init__(self):
        """Incializa los valores"""
        self.service_parking=Service_parking()
        self.options = {"1": self.add_car,
                        "2": self.car_collection,
                        #"3": self.ticket_car,
                        #"4": self.gain,
                        #"5": self.show_cars,
                        "6": self.close
                        }

    def display_menu(self):
        self.clear_screen()
        """muestra un menu de las opciones"""
        print("""
                        Bienvenido          
                    1. agrega un carro
                    2. estable el costo
                    3. muestra la salida(ticket)
                    4. ganancias
                    5. ver los que Entran y salen
                    6.salir

                        """)

    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiona Enter para continuar")

    def clear_screen(self):
        """
        Verifica mediante la librería platform el sistema operativo
        del usuario y limpia la pantalla dependiendo del SO utilizado.
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")


    def run(self):
        """ Método de entrada para la aplicación """
        while True:
            self.display_menu()
            choise = input("Ingrese una opción: ")
            action = self.options.get(choise)

            if action:
                action()
            else:
                print("¡{0} no es una opción válida!".format(choise))
    
    def add_car(self):
        """Metodo donde se ingresa la informacion del carro"""
        self.clear_screen()
        placa = input("ingrese la placa del vehiculo: ")
        marca = input("ingrese la marca del vehiculo: ")
        modelo = input("ingrese el modelo del vehiculo: ")
        tipo = input("Su vehiculo es carro(si o no): ")
        if str(tipo) == str("si"):
            tipo_vehiculo="carro"
        else:
            tipo_vehiculo="moto"
        self.service_parking.add_car(placa,marca,modelo,tipo_vehiculo)

    def car_collection(self):
        """agrega el costo del tiempo que estuvo"""


    def close(self):
        """cierra el programa"""
        print("Gracias por usar nuestros servicios")
        sys.exit()

if __name__ == "__main__":
    menu = Menu()
    menu.run()   