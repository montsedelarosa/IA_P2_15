# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class MarcoPersona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"

# Crear instancias de marcos (situaciones)
persona1 = MarcoPersona("Juan Pérez", 30, "Ingeniero")
persona2 = MarcoPersona("Ana García", 25, "Médico")

# Imprimir la información de las situaciones
print("Persona 1:")
print(persona1)
print("\nPersona 2:")
print(persona2)
