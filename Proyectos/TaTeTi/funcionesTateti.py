import random

def crearTablero(jugador,tamaño):
    tablero = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            if j == 0:
                fila.append(f"{i+1}|")
            fila.append("|_|")
        tablero.append(fila)
    ultFila = []
    for l in range(tamaño+1):
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
        
def ocuparCasilla(tablero, jugador):
    #Verificacion loca por si no leen
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
            #print("fila: ",fila,"columna: ",col)
            #print("casilla: ",tablero[fila][col])
            tablero[fila][col] = jugador
            #print("casilla: ",tablero[fila][col])
            imprimirTablero(tablero)
            return True
    else:
        print("\n!!! ---- No es una casilla valida ---- !!!\n")
        ocuparCasilla(tablero,jugador)

def ocuparCasillaPC(tablero, jugador):
    fila = random.randint(0,2)
    col = random.randint(1,3)
    if tablero[fila][col] == "|_|":
            tablero[fila][col] = jugador
            return True
    else:
        ocuparCasillaPC(tablero,jugador)

def verificarGanador(tablero, jugador):
    # Verificar columnas
    #print("chequeando fila")
    for i in range(len(tablero)-1):
        check1 = 0
        for j in range(1,len(tablero)):
            #print("fila:",i,"columna: ",j,"casilla: ",tablero[i][j])
            if tablero[i][j] == jugador:
                check1 +=1
        if check1 == 3:
            #print("Se encontraron tres fichas en la fila", i)
            break
    print(check1)

    # Verificar filas
    #print("Chequeando columna")
    for j in range(1, len(tablero)):
        check2 = 0
        for i in range(len(tablero)-1):
            #print("Fila:", i, "Columna:", j, "Casilla:", tablero[i][j])
            if tablero[i][j] == jugador:
                check2 += 1
        if check2 == 3:
            #print("Se encontraron tres fichas en la columna", j)
            break


    # Verificar diagonal principal
    check3 = 0
    for i in range(len(tablero)-1):
        j=i+1
        #print("fila:",i,"columna: ",j,"casilla: ",tablero[i][j])
        if tablero[i][j] == jugador:
            check3 +=1
    # Verificar diagonal traspuesta
    check4 = 0
    for i in range(len(tablero)-1):
        j=i+1
        #print("fila:",i,"columna: ",len(tablero)-j,"casilla: ",tablero[i][len(tablero)-j])
        if tablero[i][len(tablero)-j] == jugador:
            check4 +=1
    #print(check1,check2,check3,check4)
    return True if (check1 == 3 or check2 == 3 or check3 == 3 or check4 == 3) else False

def ganaste(tablero,jugador):
    print("\n----------TA-TE-TI----------\n")
    imprimirTablero(tablero)
    print("\n----------TA-TE-TI----------\n")
    print(f"""
----------------------------
\n¡Felicidades! {jugador} Has ganado.\n
----------------------------
    """)
    return True

def empate(tablero):
    print("\n----------TA-TE-TI----------\n")
    imprimirTablero(tablero)
    print("\n----------TA-TE-TI----------\n")
    print("""\n
----------------------------
"EMPATE. ¿Un nuevo reto?"
----------------------------
""")
    return True

def turnoJugador(jugador):
    print(f"----------------------------\nTurno de {jugador}\n----------------------------")
    return True
    
def tableroLleno(tablero):
    if all(tablero[i][j] != "|_|" for i in range(len(tablero)) for j in range(len(tablero))):
        return True
    return False