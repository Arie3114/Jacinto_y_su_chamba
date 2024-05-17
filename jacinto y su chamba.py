import datetime

class Persona:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Identificación: {self.identificacion}"

class Empleado(Persona):
    def __init__(self, nombre, identificacion, numero_empleado):
        super().__init__(nombre, identificacion)
        self.numero_empleado = numero_empleado

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Número de Empleado: {self.numero_empleado}"

class Cliente(Persona):
    def __init__(self, nombre, identificacion, codigo_cliente):
        super().__init__(nombre, identificacion)
        self.codigo_cliente = codigo_cliente

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Código de Cliente: {self.codigo_cliente}"

persona = Persona("Paola Lopez", "0953405250")
empleado = Empleado("Jacinto Torres", "0053405248", "Ja095")
cliente = Cliente("Jose Balazos", "0953405249", "Jo096")

print("Información de la Persona:")
print(persona.mostrar_informacion())

print("\nInformación del Empleado:")
print(empleado.mostrar_informacion())

print("\nInformación del Cliente:")
print(cliente.mostrar_informacion())
