# =============================================================
# Momento Evaluativo 2 - Estructura de Datos y Laboratorio
# Listas y Archivos
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# =============================================================

from Cita import Cita
class Usuario():
    def __init__(self, identificacion, nombre, apellido, telefono, fechaNacimiento):
        """
        Parametros:
            identificacion:int
            nombre:str
            apellido:str
            telefono:int
            fechaNacimiento:date 
        """
        
        self.__identificacion=identificacion
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono
        self.__fechaNacimiento=fechaNacimiento

    def cancelarCita(self, cita: Cita):
        """
        Cambia el estado de la cita a 'Cancelada'
        """
        if cita:
            cita.estado = "Cancelada"
            return cita
        return None

    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self,identificacion):
        self.__identificacion=identificacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self,apellido):
        self.__apellido=apellido

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento

    @fechaNacimiento.setter
    def fechaNacimiento(self,fechaNacimiento):
        self.__fechaNacimiento=fechaNacimiento

    def __str__(self):
        return str(self.identificacion)+' '+str(self.nombre)+' '+str(self.apellido)+' '+str(self.telefono)+' '+str(self.fechaNacimiento)

