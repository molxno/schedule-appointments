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
from Servicio import Servicio
from Cita import Cita

class Administrador(Usuario):
    def __init__(self, identificacion, nombre, apellido, telefono, fechaNacimiento):
        """
        Parametros:
            identificacion:int
            nombre:str
            apellido:str
            telefono:int
            fechaNacimiento:date
        """
        super().__init__(identificacion, nombre, apellido, telefono, fechaNacimiento)

    def crearServicio(self, codigo, descripcion, valorServicio, duracion):
        """
        Retorna un objeto de tipo Servicio creado por este Administrador
        """
        return Servicio(codigo, descripcion, valorServicio, duracion, self)

    def asignarCita(self, usuario, empleado, servicio, horario, fecha, valor):
        """
        Retorna un objeto de tipo Cita
        """
        return Cita(usuario, servicio, empleado, fecha, horario, valor)