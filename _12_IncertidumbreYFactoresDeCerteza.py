# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pyswip

from pyswip import Prolog

# Crear un objeto Prolog
prolog = Prolog()

# Definir reglas con factores de certeza
prolog.assertz("(fiebre(Y) :- temperatura_alta(Y) : 0.8)")
prolog.assertz("(fiebre(Y) :- sudoracion(Y) : 0.6)")
prolog.assertz("(temperatura_alta(juan) : 0.7)")
prolog.assertz("(sudoracion(juan) : 0.5)")
prolog.assertz("(temperatura_alta(maria) : 0.6)")

# Realizar consultas bajo incertidumbre
for resultado in prolog.query("fiebre(juan)"):
    print("¿Juan tiene fiebre?")
    print(f"Respuesta: Sí, con un factor de certeza de {resultado['0']:.2f}\n")

for resultado in prolog.query("fiebre(maria)"):
    print("¿Maria tiene fiebre?")
    print(f"Respuesta: Sí, con un factor de certeza de {resultado['0']:.2f}\n")
