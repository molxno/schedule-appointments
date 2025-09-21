class Servicio():
    def __init__(self, codigo: str, descripcion: str, valorServicio: float, duracion: int, creador):
        """
        Parametros:
            codigo:str
            descripcion:str
            valorServicio:float
            duracion:int
            creador:Administrador  -> usuario que crea el servicio
        """
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__valorServicio = valorServicio
        self.__duracion = duracion
        self.__creador = creador  # referencia al Administrador

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @property
    def valorServicio(self):
        return self.__valorServicio

    @valorServicio.setter
    def valorServicio(self, valorServicio):
        self.__valorServicio = valorServicio

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    @property
    def creador(self):
        return self.__creador

    @creador.setter
    def creador(self, creador):
        self.__creador = creador

    def __str__(self):
        return f"{self.codigo} {self.descripcion} {self.valorServicio} {self.duracion} (creado por {self.creador.nombre})"
