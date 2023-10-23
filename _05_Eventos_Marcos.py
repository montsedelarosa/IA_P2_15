# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class EventoMarco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

    def agregar_atributo(self, nombre, valor):
        self.atributos[nombre] = valor

    def __str__(self):
        atributos_str = ', '.join([f'{nombre}={valor}' for nombre, valor in self.atributos.items()])
        return f'{self.nombre}({atributos_str})'

class SistemaEventosMarco:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def notificar_eventos(self):
        for evento in self.eventos:
            print(f'Evento Marco: {evento}')

# Crear eventos marco
evento1 = EventoMarco('Evento1')
evento1.agregar_atributo('Atributo1', 'Valor1')
evento1.agregar_atributo('Atributo2', 'Valor2')

evento2 = EventoMarco('Evento2')
evento2.agregar_atributo('Atributo3', 'Valor3')

# Crear un sistema de eventos marco
sistema_eventos = SistemaEventosMarco()

# Agregar eventos al sistema
sistema_eventos.agregar_evento(evento1)
sistema_eventos.agregar_evento(evento2)

# Notificar los eventos
sistema_eventos.notificar_eventos()
