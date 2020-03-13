#-*-UTF-8-*-
#Nombre:service_parking.py
#objetivo:establece las funciones del parkeo 
#Creador:Diego Diaz
#Fecha:13/03/2020
from cars import Cars

class Service_parking:
    """
    Clase donde se encuentran todas los servicios 
    y/o lo neceserio para del programa
    """
    def __init__(self):
        """incializa todas los procesos"""
        self.my_parking = list()

    def add_car(self, placa="", marca="", modelo="", tipo_vehiculo="",cobro=float):
        """Agrega un vehiculo a la lista"""
        self.my_parking.append(Cars(placa ,modelo, tipo_vehiculo,cobro))
    
    def car_collection(self, placa, marca, modelo, tipo_vehiculo,cobro,estado):
        """cobro de la estadia del coche"""
        car = self._search_car(placa)

        if car:
            car.placa=placa
            car.marca=marca
            car.modelo=modelo
            car.tipo_vehiculo=tipo_vehiculo
            car.cobro=cobro
            car.estado=estado
            return True
        else:
            print("No existe un carro con la placa: {0}"
                  .format(placa))
            return False

    def _search_car(self, placa):
        """Busca el automovil por la placa"""
        for crs in self.my_parking:
            if str(crs.placa) == str(placa):
                return crs
        
        return None

    def sumatory_cost(self):
        """Suma la ganacias de todos los coches parkeados"""
        total=0.0
        for x in self.my_parking:
            total=x.costo=total

        print("La ganancia total es de: ",total)