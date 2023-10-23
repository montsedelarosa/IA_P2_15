# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pyke

from pyke import knowledge_engine

# Definir una base de conocimiento
engine = knowledge_engine.engine(__file__)

# Definir reglas
engine.prove_1('es_humano', 'juan')
engine.prove_1('es_humano', 'maria')
engine.prove_1('es_humano', 'ana')

engine.prove_1('es_mortal', 'juan')
engine.prove_1('es_mortal', 'maria')
engine.prove_1('es_mortal', 'ana')

engine.prove_1('padre', 'juan', 'maria')
engine.prove_1('padre', 'juan', 'ana')

engine.prove_1('abuelo', 'abraham', 'juan')
engine.prove_1('abuelo', 'abraham', 'maria')
engine.prove_1('abuelo', 'abraham', 'ana')

# Realizar consultas
def consulta(resultado):
    for i, r in enumerate(resultado):
        print(f'Resultado {i + 1}: {r}')

# Consultar hechos
consulta(engine.prove_all('es_humano($x)'))

# Consultar reglas
consulta(engine.prove_all('abuelo($x, $y)'))
