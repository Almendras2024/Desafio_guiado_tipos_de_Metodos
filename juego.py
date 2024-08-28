from personaje import Personaje
import random

print("¡Bienvenido a Gran Realidad!\n")
nombre = input("Por favor indique el nombre de su personaje:\n")

p = Personaje(nombre)
print(p.estado)

print("\n¡Oh no!, ¡Ha aparecido un Orco!")
o = Personaje("Orco")

print(p.estado)
print(o.estado)

probabilidad_ganar = p.get_probabilidad_ganar(p.nivel, o.nivel)

opcion_personaje = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
""""Se correge el nombre del módulo random que está mal escrito como ramdon.
    Se Cambia el mensaje de bienvenida para solicitar el nombre del personaje del jugador, no del orco.
    Se corrige la llamada al método mostrar_dialogo_opcion para que sea un método de instancia, no de clase.
    Se asegura de que la probabilidad de ganar se calcule correctamente y se pase el personaje orco como argumento, no el personaje del jugador.
    Se Correge la lógica de actualización del estado después de cada enfrentamiento.
    Se Corregir errores tipográficos como primt que debería ser print.
    El bucle while permita al jugador continuar luchando o huir según su elección."""

while opcion_personaje == 1:
    aleatorio = random.uniform(0, 1)

    if aleatorio <= probabilidad_ganar:
        resultado = "G"
    else:
        resultado = "P"

    if resultado == "G":
        print(
            "\n¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!\n"
        )
        p.estado = 50
        o.estado = -30

    else:
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!\n"
        )
        p.estado = -30
        o.estado = 50

    print(p.estado)
    print(o.estado)

    probabilidad_ganar = p.get_probabilidad_ganar(p.nivel, o.nivel)
    opcion_personaje = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
print("\nDont worry, ¡Lo dejaste atras!\n")