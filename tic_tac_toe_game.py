class Tablero:
    def __init__(self, name):
        self.name = name
        self.__options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, player):
        if self.__options[player.decision - 1] == 'X' or self.__options[player.decision - 1] == 'O':
            print('\n Opción NO válida.')
        else:
            self.__options[player.decision - 1] = player.mark

    def __casilla(self, player1, player2):
        o = 0
        while o < 1 or o > 9:
            print(self)
            o = input('\n ¿Cuál casilla?: ').strip()
            try:
                o = int(o)
            except:
                print('\n NO es válida.')
                o = 0
                continue

            if o > 9 or o < 1:
                print('\n Fuera del rango.')
                continue

        if player1.turno():
            player1.decision = o
            self.options = player1
        else:
            player2.decision = o
            self.options = player2

    def __turno(self, player1, player2):
        j = input('\n Nombre del jugador: ').strip()
        while j != player1.name and j != player2.name:
            print(f'\n El jugador {j} no existe.')
            j = input('\n Nombre del jugador: ').strip()

        print(player1.mi_turno() if j == player1.name else player2.mi_turno())

    def indicaciones(self, player1, player2):
        o = input('''\n Opciones:
         \t1. Seleccionar casilla.
         \t2. ¿Es mi turno?
         \t : ''').strip()
        while o != '1' and o != '2':
            print('\n Opción no válida.')
            o = input('''\n Opciones:
             \t1. Seleccionar casilla.
             \t2. ¿Es mi turno?
             \t : ''').strip()

        if o == '1':
            self.__casilla(player1, player2)
        else:
            self.__turno(player1, player2)

    def __str__(self):
        return f'''
        {self.__options[0]}|{self.__options[1]}|{self.__options[2]}
        -----
        {self.__options[3]}|{self.__options[4]}|{self.__options[5]}
        -----
        {self.__options[6]}|{self.__options[7]}|{self.__options[8]}
        '''

class Juego:
    turnos = 9
    marks = []
    players = []

    def __init__(self, mark):
        assert mark.upper() == 'X' or mark.upper() == 'O', f'Mark "{mark}" is not valid.'
        assert not mark in Juego.marks, f'Mark "{mark}" is not available.'

        self.mark = mark.upper()
        Juego.marks.append(mark.upper())

    def __turnos_restantes(self, tabl):
        total = tabl.options.count('X') + tabl.options.count('O')
        Juego.turnos = 9 - total

    def __resultado_condiciones(self, tabl):
        if (tabl.options[0] == tabl.options[1] and tabl.options[1] == tabl.options[2]) or (tabl.options[0] == tabl.options[3] and tabl.options[3] == tabl.options[6]) or (tabl.options[0] == tabl.options[4] and tabl.options[4] == tabl.options[8]) or (tabl.options[6] == tabl.options[4] and tabl.options[4] == tabl.options[2]) or (tabl.options[6] == tabl.options[7] and tabl.options[7] == tabl.options[8]) or (tabl.options[2] == tabl.options[5] and tabl.options[5] == tabl.options[8]):
            return True
        else:
            return False

    def resultado(self, tabl):
        if Juego.turnos > 6:
            self.__turnos_restantes(tabl)
            return False
        else:
            if self.__resultado_condiciones(tabl):
                return True

            self.__turnos_restantes(tabl)
            return False

class Jugador(Juego):
    def __init__(self, name, mark, pos):
        super().__init__(
            mark
        )

        assert pos == 2 or pos == 1, f'Position {pos} not valid. Just 1 or 2.'
        assert len(Juego.players) <= 2, 'There are already two players.'

        self.name = name
        self.__pos = pos

        Juego.players.append(self)

    @property
    def pos(self):
        return self.__pos

    def turno(self):
        if self.pos % 2 == Juego.turnos % 2:
            return True
        else:
            return False

    def mi_turno(self):
        return f'\n Tu turno, {self.name}.' if self.turno() else f'\n No es tu turno, {self.name}.'


if __name__ == '__main__':

    t1 = Tablero('Gato')
    p1= Jugador(input('Jugador 1: ').strip(), input('X u O: ').strip(), 1)
    m2 = 'O' if p1.mark == 'X' else 'X'
    p2 = Jugador(input('Jugador 2: ').strip(), m2, 2)

    while Juego.turnos > 0:
        print(t1)
        print(f'\n Turnos restantes: {Juego.turnos}')
        t1.indicaciones(p1, p2)
        result = p1.resultado(t1)
        if result: break

    if not result:
        print('\n EMPATOTE.')
    else:
        if p1.turno():
            print(f'\n GANÓ EL PERRO DE {p1.name}')
        else:
            print(f'\n GANÓ EL PERRO DE {p2.name}')

    print(t1)
