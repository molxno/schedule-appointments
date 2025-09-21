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

from datetime import date, time, datetime
from agendaCitas import agendaCitas

agenda = agendaCitas()

# ==============================
# LECTURA DE USUARIOS
# ==============================
try:
    with open("Usuarios.csv", "r", encoding="latin-1") as file:
        next(file)  # saltar encabezado
        for linea in file:
            datos = linea.strip().split(";")  # <- separador correcto
            identificacion = int(datos[0])
            nombre = datos[1]
            apellido = datos[2]
            telefono = int(datos[3])
            fechaNacimiento = datetime.strptime(datos[4], "%d/%m/%Y").date()
            tipoUsuario = datos[5]
            codigoEspecialidad = datos[6] if len(datos) > 6 and datos[6] else None

            agenda.agregarUsuario(identificacion, nombre, apellido, telefono,
                                  fechaNacimiento, tipoUsuario, codigoEspecialidad)
except Exception as e:
    print("Error de lectura en Usuarios.csv:", e)

# ==============================
# LECTURA DE SERVICIOS
# ==============================
try:
    with open("Servicios.csv", "r", encoding="latin-1") as file:
        next(file)  # saltar encabezado
        for linea in file:
            datos = linea.strip().split(";")  # <- separador correcto
            codigo = datos[0]
            descripcion = datos[1]
            valorServicio = float(datos[2])
            duracion = int(datos[3])
            identificacionUsuario = int(datos[4])

            agenda.agregarServicio(codigo, descripcion, valorServicio, duracion, identificacionUsuario)
except Exception as e:
    print("Error de lectura en Servicios.csv:", e)

# ==============================
# LECTURA DE CITAS
# ==============================
try:
    with open("Citas.csv", "r", encoding="latin-1") as file:  # <- también latin-1
        next(file)  # saltar encabezado
        for linea in file:
            datos = linea.strip().split(";")  # <- separador correcto
            codigoServicio = datos[0]
            idEmpleado = int(datos[1])
            idUsuario = int(datos[2])
            fecha = datetime.strptime(datos[3], "%d/%m/%Y").date()
            hora = datetime.strptime(datos[4], "%H:%M").time()
            identificacionAdmin = int(datos[5])

            agenda.agregarCitas(idUsuario, idEmpleado, codigoServicio, hora, fecha, identificacionAdmin)
except Exception as e:
    print("Error de lectura en Citas.csv:", e)

"""
ZONA DE PRUEBAS
"""

print("\n===== ZONA DE PRUEBAS =====")

# 1. Agregar usuarios
print("\n-- PRUEBAS USUARIOS --")
u1 = agenda.agregarUsuario(1, "Carlos", "Pérez", 3001234567, date(1980,5,20), "Administrador", None)
u2 = agenda.agregarUsuario(2, "Ana", "Gómez", 3017654321, date(1995,7,15), "Cliente", None)
print("Usuario administrador creado:", u1)
print("Usuario cliente creado:", u2)

# Intento de usuario duplicado
u3 = agenda.agregarUsuario(1, "Luis", "Torres", 3020001111, date(1990,1,1), "Cliente", None)
print("Intento usuario duplicado (espera None):", u3)

# 2. Agregar servicios
print("\n-- PRUEBAS SERVICIOS --")
s1 = agenda.agregarServicio("S1", "Consulta general", 100000, 30, 1) # lo crea admin
s2 = agenda.agregarServicio("S2", "Odontología", 150000, 45, 1)
print("Servicio 1 creado:", s1)
print("Servicio 2 creado:", s2)

# Intento servicio duplicado
s3 = agenda.agregarServicio("S1", "Duplicado", 50000, 15, 1)
print("Intento servicio duplicado (espera None):", s3)

# 3. Agregar empleado (requiere servicio existente)
print("\n-- PRUEBAS EMPLEADO --")
emp1 = agenda.agregarUsuario(3, "Pedro", "Ramírez", 3059876543, date(1990,12,10), "Empleado", "S1")
print("Empleado creado:", emp1)

# Intento de empleado con especialidad inexistente
emp2 = agenda.agregarUsuario(4, "Laura", "Martínez", 3102223333, date(1992,3,8), "Empleado", "S99")
print("Intento empleado con especialidad inexistente (espera None):", emp2)

# 4. Agregar citas
print("\n-- PRUEBAS CITAS --")
c1 = agenda.agregarCitas(2, 3, "S1", time(10,0), date(2025,9,30), 1)  # admin asigna
print("Cita creada:", c1)

# Intento de cita duplicada (usuario ya tiene misma hora y fecha)
c2 = agenda.agregarCitas(2, 3, "S1", time(10,0), date(2025,9,30), 1)
print("Intento cita duplicada (espera None):", c2)

# Intento de que el empleado se atienda a sí mismo
c3 = agenda.agregarCitas(3, 3, "S1", time(11,0), date(2025,9,30), 1)
print("Intento empleado atendiéndose a sí mismo (espera None):", c3)

# 5. Buscar
print("\n-- PRUEBAS BÚSQUEDA --")
print("Buscar usuario (id=2):", agenda.buscarUsuario(2))
print("Buscar servicio (S1):", agenda.buscarServicio("S1"))
print("Buscar cita (usuario=2, fecha=2025-09-30, hora=10:00):", agenda.buscarCita(2, time(10,0), date(2025,9,30)))

# 6. Cancelar y atender (ANTES de eliminar)
print("\n-- PRUEBAS CANCELAR / ATENDER --")
c4 = agenda.agregarCitas(2, 3, "S1", time(12,0), date(2025,9,30), 1)
print("Cita creada para cancelar:", c4)

cancel = agenda.cancelarCita(2, c4.identificador if c4 else -1)
print("Cancelar cita por cliente:", cancel)

c5 = agenda.agregarCitas(2, 3, "S1", time(13,0), date(2025,9,30), 1)
print("Cita creada para atender:", c5)

atender = agenda.atenderCita(3, c5.identificador if c5 else -1)
print("Atender cita por empleado:", atender)

# 7. Eliminación (después de cancelar/atender)
print("\n-- PRUEBAS ELIMINACIÓN --")
elimServ = agenda.eliminarServicio("S2")
print("Eliminar servicio S2:", elimServ)

elimCita = agenda.eliminarCita(c1.identificador if c1 else -1)
print("Eliminar cita:", elimCita)

elimUser = agenda.eliminarUsuario(2)
print("Eliminar usuario cliente (id=2):", elimUser)