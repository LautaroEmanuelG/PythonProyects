import funcionesTateti as fn
opcion = 6;
#Menu
while True:
    opcion = int(input("""
----------------------------
Bienvenido a un TA-TE-TI 
----------------------------
Que modo de juego desea jugar?
1. Jugador 1 (X) vs Jugador 2 (O)
2. Jugador 1 (X) vs PC (O)
3. Salir
------>"""))
    if opcion == 1:
        jugador1 = "|X|"
        jugador2 = "|O|"
        print("Seleccionó. Jugador 1 (X) vs Jugador 2 (O) \n-----------------------------\nCOMENCEMOS\n-----------------------------")
        tablero = fn.crearTablero("LG",3)
        
        while True:
            fn.imprimirTablero(tablero)
            fn.turnoJugador("Jugador 1")
            fn.ocuparCasilla(tablero,jugador1)
            if fn.verificarGanador(tablero,jugador1):
                fn.ganaste(tablero,"Jugador 1")
                break
            if fn.tableroLleno(tablero):
                fn.empate(tablero)
                break
            #Tuerno jugador 2
            fn.ocuparCasilla(tablero,jugador2)
            fn.turnoJugador("Jugador 2")
            if fn.verificarGanador(tablero,jugador2):
                fn.ganaste(tablero,"Jugador 2")
                break
            if fn.tableroLleno(tablero):
                fn.empate(tablero)
                break
            
    elif opcion == 2:
        jugador1 = "|X|"
        pc = "|O|"
        print("Seleccionó. Jugador 1 (X) vs PC (O) \n-----------------------------\nCOMENCEMOS\n-----------------------------")
        tablero = fn.crearTablero("LG",3)
        
        while True:
            fn.imprimirTablero(tablero)
            #Turno jugador 1
            fn.turnoJugador("Jugador 1")
            fn.ocuparCasilla(tablero,jugador1)
            if fn.verificarGanador(tablero,jugador1):
                fn.ganaste(tablero,"Jugador 1")
                break
            if fn.tableroLleno(tablero):
                fn.empate(tablero)
                break
            
            #Turno PC
            fn.ocuparCasillaPC(tablero,pc)
            fn.turnoJugador("PC")
            if fn.verificarGanador(tablero,pc):
                fn.ganaste(tablero,"PC")
                break
            if fn.tableroLleno(tablero):
                fn.empate(tablero)
                break
    elif opcion == 3:
        print("Seleccionó. Salir \n-----------------------------\nGracias por jugar\n-----------------------------")
        exit()
    else:
        print("Seleccionó. Opcion invalida \n-----------------------------\nElige otra opción\n-----------------------------")