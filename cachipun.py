# Importar libreria para randomizar
import random

# Posibles jugadas aleatorias
jugadas_aleatorias = ["piedra", "papel", "tijeras"]

# Selección de jugada de la computadora
elemento_aleatorio = random.choice(jugadas_aleatorias)

# Pedir jugar al usuario
jugada_usuario = input("Para jugar elige piedra, papel o tijeras: ").lower() #Evitamos errores en la escritura

# Proceso
if jugada_usuario not in jugadas_aleatorias:
    print("Jugada no válida. Por favor elige entre piedra, papel o tijeras.")
else:
    print(f"Tú elegiste: {jugada_usuario}")
    print(f"La computadora eligió: {elemento_aleatorio}")

    # Resultado
    if jugada_usuario == elemento_aleatorio:
        print("¡Es un empate!")
    elif (jugada_usuario == "piedra" and elemento_aleatorio == "tijeras") or \
         (jugada_usuario == "papel" and elemento_aleatorio == "piedra") or \
         (jugada_usuario == "tijeras" and elemento_aleatorio == "papel"):
        print("¡Tú ganas, muchas felicidades!")
    else:
        print("La computadora gana, vuelve a intentarlo.")
