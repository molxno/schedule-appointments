from singlyLinkedList import singlyLinkedList
from datetime import date, time
from Usuario import Usuario
from Servicio import Servicio
from Empleado import Empleado
from Administrador import Administrador
from Cita import Cita
from typing import Optional

class agendaCitas():
    def __init__(self):
        self.usuarios = singlyLinkedList()
        self.servicios = singlyLinkedList()
        self.citas = singlyLinkedList()

    # -----------------------
    # AGREGAR SERVICIO
    # -----------------------
    def agregarServicio(self, codigo: str, descripcion: str, valorServicio: float, duracion: int,
                        identificacionUsuario: int) -> Servicio:
        if self.buscarServicio(codigo):
            return None
        admin = self.buscarUsuario(identificacionUsuario)
        if not isinstance(admin, Administrador):
            return None
        servicio = Servicio(codigo, descripcion, valorServicio, duracion, admin)
        self.servicios.addFirst(servicio)
        return servicio

    # -----------------------
    # AGREGAR USUARIO
    # -----------------------
    def agregarUsuario(self, identificacion: int, nombre: str, apellido: str, telefono: int, fechaNacimiento: date,
                       tipoUsuario: str, codigoEspecialidad: Optional[str]) -> Usuario:
        if self.buscarUsuario(identificacion):
            return None
        if tipoUsuario.lower() == "administrador":
            usuario = Administrador(identificacion, nombre, apellido, telefono, fechaNacimiento)
        elif tipoUsuario.lower() == "empleado":
            especialidad = self.buscarServicio(codigoEspecialidad)
            if not especialidad:
                return None
            usuario = Empleado(identificacion, nombre, apellido, telefono, fechaNacimiento, especialidad)
        else:
            usuario = Usuario(identificacion, nombre, apellido, telefono, fechaNacimiento)
        self.usuarios.addLast(usuario)
        return usuario

    # -----------------------
    # AGREGAR CITA
    # -----------------------
    def agregarCitas(self, idUsuario: int, idEmpleado: int, codigoServicio: str, hora: time, fecha: date,
                     identificacionAdmin: int) -> Cita:
        if self.buscarCita(idUsuario, hora, fecha):
            return None
        usuario = self.buscarUsuario(idUsuario)
        empleado = self.buscarUsuario(idEmpleado)
        servicio = self.buscarServicio(codigoServicio)
        admin = self.buscarUsuario(identificacionAdmin)
        if not usuario or not empleado or not servicio or not isinstance(admin, Administrador):
            return None
        if usuario.identificacion == empleado.identificacion:
            return None
        if not isinstance(empleado, Empleado) or empleado.especialidad.codigo != servicio.codigo:
            return None

        valor = self.__calcularValorCita(servicio, usuario)
        cita = admin.asignarCita(usuario, empleado, servicio, hora, fecha, valor)
        self.citas.addLast(cita)
        return cita

    # -----------------------
    # CALCULAR VALOR CITA
    # -----------------------
    def __calcularValorCita(self, servicio: Servicio, usuario: Usuario) -> float:
        if isinstance(usuario, Administrador):
            return servicio.valorServicio * 0.5
        elif isinstance(usuario, Empleado):
            return servicio.valorServicio * 0.7
        else:
            return servicio.valorServicio


    # -----------------------
    # BUSCAR SERVICIO
    # -----------------------
    def buscarServicio(self, codigo: str) -> Servicio:
        nodo = self.servicios.first()
        while nodo:
            if nodo.data.codigo == codigo:
                return nodo.data
            nodo = nodo.next
        return None

    # -----------------------
    # BUSCAR USUARIO
    # -----------------------
    def buscarUsuario(self, identificacion: int) -> Usuario:
        nodo = self.usuarios.first()
        while nodo:
            if nodo.data.identificacion == identificacion:
                return nodo.data
            nodo = nodo.next
        return None

    # -----------------------
    # BUSCAR CITA
    # -----------------------
    def buscarCita(self, identificacionUsuario: int, hora: time, fecha: date) -> Cita:
        nodo = self.citas.first()
        while nodo:
            c = nodo.data
            if c.usuario.identificacion == identificacionUsuario and c.hora == hora and c.fecha == fecha:
                return c
            nodo = nodo.next
        return None

    # -----------------------
    # ELIMINAR SERVICIO
    # -----------------------
    def eliminarServicio(self, codigo: str) -> Servicio:
        nodo = self.servicios.first()
        anterior = None
        while nodo:
            if nodo.data.codigo == codigo:
                servicio = nodo.data
                # Marcar como None en citas
                n2 = self.citas.first()
                while n2:
                    if n2.data.servicio and n2.data.servicio.codigo == codigo:
                        n2.data.servicio = None
                    n2 = n2.next
                # Eliminar de la lista
                if anterior:
                    anterior.next = nodo.next
                else:
                    self.servicios.removeFirst()
                return servicio
            anterior = nodo
            nodo = nodo.next
        return None

    # -----------------------
    # ELIMINAR USUARIO
    # -----------------------
    def eliminarUsuario(self, identificacion: int) -> Usuario:
        nodo = self.usuarios.first()
        anterior = None
        while nodo:
            if nodo.data.identificacion == identificacion:
                usuario = nodo.data
                # Marcar como None en citas
                n2 = self.citas.first()
                while n2:
                    if n2.data.usuario and n2.data.usuario.identificacion == identificacion:
                        n2.data.usuario = None
                    if isinstance(usuario,
                                  Empleado) and n2.data.empleado and n2.data.empleado.identificacion == identificacion:
                        n2.data.empleado = None
                    n2 = n2.next
                # Eliminar de la lista
                if anterior:
                    anterior.next = nodo.next
                else:
                    self.usuarios.removeFirst()
                return usuario
            anterior = nodo
            nodo = nodo.next
        return None

    # -----------------------
    # ELIMINAR CITA
    # -----------------------
    def eliminarCita(self, identificador: int) -> Cita:
        nodo = self.citas.first()
        anterior = None
        while nodo:
            if nodo.data.identificador == identificador:
                cita = nodo.data
                if anterior:
                    anterior.next = nodo.next
                else:
                    self.citas.removeFirst()
                return cita
            anterior = nodo
            nodo = nodo.next
        return None

    # -----------------------
    # CANCELAR CITA
    # -----------------------
    def cancelarCita(self, identificacionUsuario: int, identificadorCita: int) -> Cita:
        usuario = self.buscarUsuario(identificacionUsuario)
        if not usuario:
            return None
        nodo = self.citas.first()
        while nodo:
            c = nodo.data
            if c.identificador == identificadorCita:
                if isinstance(usuario, Administrador) or (
                        c.usuario and c.usuario.identificacion == identificacionUsuario):
                    return usuario.cancelarCita(c)
            nodo = nodo.next
        return None

    # -----------------------
    # ATENDER CITA
    # -----------------------
    def atenderCita(self, identificacionUsuario: int, identificadorCita: int):
        usuario = self.buscarUsuario(identificacionUsuario)
        if not isinstance(usuario, Empleado):
            return None
        nodo = self.citas.first()
        while nodo:
            c = nodo.data
            if c.identificador == identificadorCita and c.empleado and c.empleado.identificacion == identificacionUsuario:
                return usuario.atenderCita(c)
            nodo = nodo.next
        return None

