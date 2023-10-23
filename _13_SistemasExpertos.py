# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pyknow

from pyknow import *

class Sintomas(Fact):
    pass

class Diagnostico(Fact):
    pass

class SistemaExperto(KnowledgeEngine):
    @Rule(Sintomas(fiebre='alta', dolor_de_garganta='si'))
    def regla_1(self):
        self.declare(Diagnostico(enfermedad='Amigdalitis'))

    @Rule(Sintomas(fiebre='alta', tos='si'))
    def regla_2(self):
        self.declare(Diagnostico(enfermedad='Gripe'))

    @Rule(Sintomas(fiebre='baja'))
    def regla_3(self):
        self.declare(Diagnostico(enfermedad='Resfriado'))

    @Rule(AS.fact << Sintomas(fiebre='alta', tos='no'))
    def regla_4(self, fact):
        self.modify(fact, dolor_de_garganta='si')

engine = SistemaExperto()

# Definir síntomas
sintomas = Sintomas(fiebre='alta', tos='no')

# Ejecutar el sistema experto
engine.reset()
engine.declare(sintomas)
engine.run()

# Obtener el diagnóstico
diagnostico = engine.facts[Diagnostico]
print(f"Diagnóstico: {diagnostico['enfermedad']}")
