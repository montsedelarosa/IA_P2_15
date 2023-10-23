# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import numpy as np

# Definir el espacio muestral
espacio_muestral = np.arange(1, 7)

# Definir un evento específico (por ejemplo, obtener un 3)
evento = 3

# Calcular la probabilidad del evento
probabilidad = np.sum(espacio_muestral == evento) / len(espacio_muestral)

# Mostrar el resultado
print(f"La probabilidad de obtener un {evento} en un dado justo es: {probabilidad:.2f}")
