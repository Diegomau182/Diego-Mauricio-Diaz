#-*-UTF-8-*-
#Nombre:cars.py
#objetivo:Establece la tupla donde se guarda la informacion del vehiculo
#Creador:Diego Diaz
#Fecha:13/03/2020
from datetime import datetime, timedelta


class Cars:
    """
    inicializa un carro mediante la placa marca modelo
    tipo_vehiculo, hora_ingreso, estado.
    """
    def __init__(self,placa="", marca="", modelo="", tipo_vehiculo="",cobro=float,etado=bool):
        self.placa=placa
        self.marca=marca
        self.modelo=modelo
        self.tipo_vehiculo=tipo_vehiculo
        self.hora_ingreso=datetime.time.today()
        self.estado = True
        self.plus_five_hours = (datetime.now() + timedelta(hours=5))
        self.cobro=cobro
