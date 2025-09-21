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

class Cita():
    generadorIdentificador=0
    def __init__(self, usuario, servicio, empleado, fecha, hora, valorPagar):
        """
        Parametros:
            usuario:Usuario
            servicio:Servicio
            empleado:Empleado
            fecha:date
            hora:time
            valorPagar:float
        """
        Cita.generadorIdentificador+=1
        self.__identificador=Cita.generadorIdentificador
        self.__usuario=usuario
        self.__servicio=servicio
        self.__empleado=empleado
        self.__fecha=fecha
        self.__hora=hora
        self.__estado="Agendada"
        self.__valorPagar=valorPagar
        

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self,identificador):
        self.__identificador=identificador

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self,usuario):
        self.__usuario=usuario

    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self,servicio):
        self.__servicio=servicio

    @property
    def empleado(self):
        return self.__empleado

    @empleado.setter
    def empleado(self,empleado):
        self.__empleado=empleado

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self,fecha):
        self.__fecha=fecha

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self,hora):
        self.__hora=hora

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self,estado):
        self.__estado=estado

    @property
    def valorPagar(self):
        return self.__valorPagar

    @valorPagar.setter
    def valorPagar(self,valorPagar):
        self.__valorPagar=valorPagar

    def __str__(self):
        return str(self.identificador)+' '+str(self.usuario)+' '+str(self.servicio)+' '+str(self.empleado)+' '+str(self.fecha)+' '+str(self.hora)+' '+str(self.estado)+' '+str(self.valorPagar)

