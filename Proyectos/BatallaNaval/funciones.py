# Presentacion de Batalla Naval
# Jugadores: Jugador 1 vs Jugador 2
# o jugador 1 vs CPU
# Si es jugador1 vs jugador 2 un barco de 3 casillas
# jugador 1 5 barcos de una casilla y cpu barco de 3 casillas random
# Los barcos de 3 casillas horizontal o vertical
# El mapa es de 6x6 una matriz
# Casilla Vacia " ",casilla disparada "X", casilla con barco "B"

def crearTablero(jugador):
    tablero = []
    for i in range(6):
        fila = []
        for j in range(6):
            if j == 0:
                fila.append(f"{i+1}|")
            fila.append("|_|")
        tablero.append(fila)
    ultFila = []
    for l in range(7):
        if l == 0:
            ultFila.append(f"{jugador}")
        else:
            ultFila.append(f"|{l}|")
    tablero.append(ultFila)
    return tablero


def imprimirTablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


def colocarBarcoCasilla(tablero, jugador,tamano):
    fila = 0
    col = 0
    print("Coloca tu Barco")
    while True:
        casilla = input("¿En que casilla quieres colocar la pieza?\n(Ej:2-2 o 1 1)\n----->")
        fila = int(casilla[0])
        fila -= 1
        casilla_str = list(casilla)
        casilla_str.append("-")
        casilla_str.append("-")
        for num in "123456789":
            if casilla_str[2] == num:
                col = int(casilla_str[2])
            elif casilla_str[1] == num:
                col = int(casilla_str[1])

        if tablero[fila][col] == "|_|":
            colocarBarcoDireccion(tablero,fila,col,jugador,tamano)
            break
        else:
            print("!!! ---- No es una casilla valida ---- !!!")
    return True
    
def colocarBarcoDireccion(tablero,fila, col,jugador,tamanoBarco):
    dir = 5
    while dir != 0:
        dir=int(input("""
¿En que direccion colocamos el barco?
    1.Horizontal (Hacia la derecha)
    2.Vertical (Hacia abajo)
    0.Para cambiar casilla\n
----->"""))
        if dir == 1:
            if tablero[fila][col+2] == "|_|":
                tablero[fila][col] = jugador
                tablero[fila][col+1] = jugador
                tablero[fila][col+2] = jugador
                return True
            else:
                "No es posible colocarlo en esa direccion"
        elif dir == 2:
            if tablero[fila+2][col] == "|_|":
                tablero[fila][col] = jugador 
                tablero[fila+1][col] = jugador
                tablero[fila+2][col] = jugador
                return True
            else:
                "No es posible colocarlo en esa direccion"
        elif dir == 0:
            colocarBarcoCasilla(tablero,0)
        else: print("No es una opcion valida")
        
def turnoJugador(tablero,jugador):
    print(f"----------------------------\nTurno de {jugador}\n----------------------------")
    imprimirTablero(tablero)
    print(f"----------------------------\n¡Su tablero señor!\n----------------------------")
    return True

def revisarCasilla(tableroContrario,jugadorContrario,vidaContrario):
    fila = 0
    col = 0
    print("Preparen cañones")
    while True:
        casilla = input("¿En que dirección mi capitán?\n(Ej:2-2 o 1 1)\n----->")
        fila = int(casilla[0])
        fila -= 1
        casilla_str = list(casilla)
        casilla_str.append("-")
        casilla_str.append("-")
        for num in "123456789":
            if casilla_str[2] == num:
                col = int(casilla_str[2])
            elif casilla_str[1] == num:
                col = int(casilla_str[1])
                
        if tableroContrario[fila][col] == "|_|":
            tableroContrario[fila][col] = "|O|"
            print(f"""
----------------------------\n
AGUA!!! seguiremos intentando\n
----------------------------\n""")
            imprimirTablero(tableroContrario)
            print("""
----------------------------\n
Vida restante del enemigo: {vidaContrario}\n
----------------------------\n
""")
            return vidaContrario
        elif tableroContrario[fila][col] == jugadorContrario:
            tableroContrario[fila][col] = "|X|"
            vidaContrario -= 1
            print(f"""
----------------------------\n
HEMOS DADO A UN ENEMIGO AUUU\n
----------------------------\n""")
            imprimirTablero(tableroContrario)
            print("""
----------------------------\n
Vida restante del enemigo: {vidaContrario}\n
----------------------------\n
""")
            return vidaContrario
        else:
            print("\n!!! ---- No es posible llegar hasta ahi, ¡Señor! ---- !!!\n")
            revisarCasilla(tableroContrario,jugadorContrario,vidaContrario)

# def verificarGanador(vidaContrario):
#     if vidaContrario == 0:
#         return True
#     return False

def ganaste(tablero,jugador,perdedor):
    print("\n----------BATALLA NAVAL----------\n")
    imprimirTablero(tablero)
    print(f"{perdedor} Ha sido derrotado")
    print("\n----------BATALLA NAVAL----------\n")
    print(f"""
----------------------------
\n¡Felicidades! {jugador} Has ganado.\n
----------------------------
    """)
    return True

def checkVida(tablero,vida):
    #HardCODED
    vida = 3
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "|X|":
                vida -= 1
    if vida <= 0:
        return True
    return False

def vamoAJuga(tablero1,tablero2,jugador1,jugador2,nombreJugador1,nombreJugador2,vidaJugador1,vidaJugador2):
    while True:
        #Turno jugador 1
        turnoJugador(tablero1,nombreJugador1)
        vidaJugador2 = revisarCasilla(tablero2,jugador2,vidaJugador2)
        if checkVida(tablero2,vidaJugador2):
        #if verificarGanador(vidaJugador2):
            ganaste(tablero2,nombreJugador1,nombreJugador2)
            return True
            
        #Turno jugador 2
        turnoJugador(tablero2,nombreJugador2)
        vidaJugador1 = revisarCasilla(tablero1,jugador1,vidaJugador1)
        if checkVida(tablero1,vidaJugador1):
        #if verificarGanador(vidaJugador1):
            ganaste(tablero1,nombreJugador2,nombreJugador1)
            return True