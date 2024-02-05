import funciones as fn

opcion = 5;
#Menu
while opcion != 0:
    opcion= int(input("""
----------------------------
Bienvenido a BATALLA NAVAL
----------------------------
Que modo de juego desea jugar?
1. Jugador 1 vs Jugador 2
2. Jugador 1 vs CPU (En desarrollo)
0. Salir
------>"""))
    if opcion == 1:
        jugador1 = "|B|"
        #Para vereificar la cantidad de barco activo
        vidaJugador1 = 3
        print("Seleccionó. Jugador 1 vs Jugador 2 \n-----------------------------")
        tablero1 = fn.crearTablero("J1");
        print("\n-----------------------------\nTablero Jugador 1\n-----------------------------")
        fn.imprimirTablero(tablero1);
        fn.colocarBarcoCasilla(tablero1,jugador1,3)
        fn.imprimirTablero(tablero1);
        
        jugador2 = "|N|"
        #Para vereificar la cantidad de barco activo
        vidaJugador2 = 3
        tablero2 = fn.crearTablero("J2");
        print("\n-----------------------------\nTablero Jugador 2\n-----------------------------")
        fn.imprimirTablero(tablero2);
        fn.colocarBarcoCasilla(tablero2,jugador2,3)
        fn.imprimirTablero(tablero2);
        
        #Fichas colocadas VAMO A JUGA
        fn.vamoAJuga(tablero1,tablero2,jugador1,jugador2,"Jugador 1","Jugador 2",vidaJugador1,vidaJugador2)
        continue
    if opcion == 2:
        print("\n-----------------------------")
        print("Seleccionó. Jugador 1 vs CPU \n-----------------------------")
        print("Estamos desarrollando esta funcionalidad")
        print("Pronto podras jugar con la maquina")
        continue
    if opcion == 0:
        print("Seleccionó. Salir \n-----------------------------")
        print("Gracias por jugar")
        print("Vuelva pronto")
        break
    else:
        print("Opcion inválida")