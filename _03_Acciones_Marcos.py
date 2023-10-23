# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class Marco:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.propiedades = {}

    def agregar_propiedad(self, nombre, valor):
        self.propiedades[nombre] = valor

    def obtener_propiedad(self, nombre):
        if nombre in self.propiedades:
            return self.propiedades[nombre]
        else:
            return None

    def ejecutar_accion(self, accion):
        if accion == "imprimir":
            self.imprimir_informacion()
        elif accion == "calcular":
            self.calcular_valor()

    def imprimir_informacion(self):
        print(f"Nombre del marco: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print("Propiedades:")
        for nombre, valor in self.propiedades.items():
            print(f"{nombre}: {valor}")

    def calcular_valor(self):
        if "valor1" in self.propiedades and "valor2" in self.propiedades:
            valor1 = self.obtener_propiedad("valor1")
            valor2 = self.obtener_propiedad("valor2")
            suma = valor1 + valor2
            self.agregar_propiedad("suma", suma)
            print(f"La suma de {valor1} y {valor2} es: {suma}")

# Crear un marco
mi_marco = Marco("Marco1", "Un ejemplo de marco")

# Agregar propiedades
mi_marco.agregar_propiedad("propiedad1", "Valor1")
mi_marco.agregar_propiedad("propiedad2", "Valor2")
mi_marco.agregar_propiedad("valor1", 5)
mi_marco.agregar_propiedad("valor2", 7)

# Ejecutar una acción
mi_marco.ejecutar_accion("imprimir")

# Ejecutar otra acción
mi_marco.ejecutar_accion("calcular")
