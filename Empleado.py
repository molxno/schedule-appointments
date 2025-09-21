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

from Usuario import Usuario

class Empleado(Usuario):
    def __init__(self, identificacion, nombre, apellido, telefono, fechaNacimiento, especialidad):
        """
        Parametros: 
            identificacion:int
            nombre:str
            apellido:str
            telefono:str
            fechaNacimiento:date
            especialidad:Servicio
        """
        
        super().__init__(identificacion, nombre, apellido, telefono, fechaNacimiento)
        self.__especialidad=especialidad

    def atenderCita(self, cita):
        """
        Cambia el estado de la cita a 'Atendida'
        """
        if cita:
            cita.estado = "Atendida"
            return cita
        return None
        
    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self,especialidad):
        self.__especialidad=especialidad

    def __str__(self):
        return str(self.identificacion)+' '+str(self.nombre)+' '+str(self.apellido)+' '+str(self.telefono)+' '+str(self.fechaNacimiento)+' '+str(self.especialidad)

