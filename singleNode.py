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

class singleNode():
    def __init__(self,o=None):
        self.__data=o
        self.__next=None
    
    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.__next
    
    @data.setter 
    def data(self,obj):
        self.__data=obj
        
    @next.setter 
    def next(self,n):
        self.__next=n