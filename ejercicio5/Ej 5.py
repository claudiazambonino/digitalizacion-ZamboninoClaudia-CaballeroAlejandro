print("Piedra, papel, y tijeras")

jugador1 = input("jugador1: Introduce PIEDRA, PAPEL O TIJERAS: ")
jugador2 = input("jugador2: Introduce PIEDRA, PAPEL O TIJERAS: ")

if (jugador1=="PIEDRA" and jugador2=="PIEDRA") or (jugador1=="PAPEL" and jugador2=="PAPEL") or (jugador1=="TIJERAS" and jugador2=="TIJERAS"):
    print("Empate, los dos habeís seleccionado {jugador1}")
elif jugador1=="PIEDRA" and jugador2=="TIJERA":
    print("Jugador1 usa piedra y las tijeras del Jugador2 se rompen en pedazos!")
elif jugador2=="PIEDRA" and jugador1=="TIJERA":
    print("Jugador2 usa piedra y las tijeras del Jugador1 se rompen en pedazos!")

elif jugador1=="TIJERA" and jugador2=="PAPEL":
    print("Jugador1 usa TIJERA y el papel del Jugador2 se corta a pedazitos!")
elif jugador2=="TIJERA" and jugador1=="PAPEL":
    print("Jugador2 usa TIJERA y el papel del Jugador1 se corta a pedazitos!")

elif jugador1=="PAPEL" and jugador2=="PIEDRA":
    print("La piedra de jugador2 impacta en jugador1 sin ningún efecto, gana jugador1.")
elif jugador2=="PAPEL" and jugador1=="PIEDRA":
    print("La piedra de jugador2 impacta en jugador1 sin ningún efecto, gana jugador1.")