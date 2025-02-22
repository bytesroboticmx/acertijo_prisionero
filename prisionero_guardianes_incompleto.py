#Nombre:
#Matricula:
#Fecha:
import random

class Guardian:
    def __init__(self, siempre_verdad):
        self.siempre_verdad = siempre_verdad  # True = dice la verdad, False = miente

    def answer(self, puerta_correcta, otro_guardian):
        # Simulación de la pregunta: "Si le pregunto al otro guardián cuál es la puerta correcta, ¿qué me diría?"
        puerta_incorrecta = 2 - puerta_correcta  # Si la puerta correcta es 1, la incorrecta es 2 y viceversa
        
        if self.siempre_verdad:
            return otro_guardian.real_responder(puerta_incorrecta)
        else:
            return 2 - otro_guardian.real_responder(puerta_incorrecta)

    def real_answer(self, puerta_correcta):
        return puerta_correcta if self.siempre_verdad else 2 - puerta_correcta

# Asignar aleatoriamente la puerta de la libertad (1 o 2)


# Crear dos guardianes, uno verdadero y uno mentiroso

# Elegir un guardián aleatoriamente para hacerle la pregunta

# El prisionero hace la pregunta y obtiene la respuesta

#Imprimir las respuestas del guardian consultado.