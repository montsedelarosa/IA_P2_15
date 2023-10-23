# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install owlready2

from owlready2 import *

# Crear una ontología
onto_path.append("./ontologia")  # Directorio para almacenar la ontología

onto = get_ontology("http://ejemplo.org/ontologia.owl")

# Definir clases y propiedades
with onto:
    class Persona(Thing):
        pass

    class Estudiante(Persona):
        pass

    class Profesor(Persona):
        pass

    class esEstudiante(ObjectProperty):
        domain = [Persona]
        range = [Estudiante]

    class imparte(ObjectProperty):
        domain = [Profesor]
        range = [Estudiante]

# Guardar la ontología
onto.save()

# Cargar la ontología
onto = get_ontology("http://ejemplo.org/ontologia.owl").load()

# Realizar consultas en la ontología
with onto:
    for persona in onto.Persona.instances():
        print(f"Persona: {persona.name}")

    for estudiante in onto.Estudiante.instances():
        print(f"Estudiante: {estudiante.name}")

    for profesor in onto.Profesor.instances():
        print(f"Profesor: {profesor.name}")

    for profesor, estudiante in onto.imparte:
        print(f"{profesor.name} imparte clases a {estudiante.name}")
