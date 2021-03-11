def crearJugador ():
    name = input('Ingrese el nombre del jugador: ')
    color = input('Ingrese el color del jugador: ')
    return {
        'type': 'SET_PLAYER_NAME_AND_COLOR',
        'payload': {
            'name': name,
            'color': color,
        }
    }


def checkWinner (board):
    for fila in board:
        for posicion in fila:
            if posicion != None and posicion == board[fila + 1][posicion] and posicion == board
                
                
                
                
                
                pass



def reducer(state, action):
    if state['stage'] == 'LoadingPlayers':
        if action['type'] == 'SET_PLAYER_NAME_AND_COLOR':
            return {
                **state,
                'players': [
                    *state['players'],
                    {'name': action['payload']['name'], 'color': action['payload']['color']}
                ],
            }

        if action['type'] == 'FINISHED_LOADING_PLAYERS':
            return {
                'stage': 'LoadingBoard',
                'players': state['players'],
            }

    if state['stage'] == 'LoadingBoard':
        if action['type'] == 'FINISHED_LOADING_AND_CREATING_BOARD':
            return {
                'stage': 'Playing',
                'players': state['players'],
                'board': action['payload']['tablero'],
                'turn': 0
            }
    
    if state['stage'] == 'Playing':
        if action['type'] == 'CONTINUE_PLAYING':
            return {
                'stage': 'Playing',
                'players': state['players'],
                'board': action['payload']['newBoard'],
                'turn': action['payload']['newTurn'],
            }   


    return state




def get_next_action(state):

    if state['stage'] == 'LoadingPlayers':
        if not state['players']:
            return crearJugador();
        
        else:

            option = input(
                '1. Cargar otro jugador\n'
                '2. Finalizar carga de jugadores\n'
                );

            while option != '1' and option != '2':

                option = input(
                    'El ingreso es incorrecto.\n'
                    '1. Cargar otro jugador\n'
                    '2. Finalizar carga de jugadores\n'
                    );

            if option == '1':
                return crearJugador();
            
            if option == '2':
                return {
                    'type': 'FINISHED_LOADING_PLAYERS'
                };
    
    if state['stage'] == 'LoadingBoard':

        cantFilas = input('Por favor ingrese la cantidad de filas: ')
        cantColumnas = input('Por favor ingrese la cantidad de columnas: ')

        while cantFilas.isnumeric() == False or cantColumnas.isnumeric() == False:
            print ('Los valores ingresados son incorrectos.\n')
            cantFilas = input('Por favor ingrese la cantidad de filas: ')
            cantColumnas = input('Por favor ingrese la cantidad de columnas: ')

        filaProvisoria = []
        tablero = []

        for x in range(int(cantColumnas)):
            filaProvisoria.append(None)

        for x in range(int(cantFilas)):
            tablero.append(filaProvisoria.copy())

        return {
            'type': 'FINISHED_LOADING_AND_CREATING_BOARD',
            'payload': {
                'tablero': tablero
                }
        }

    
    if state['stage'] == 'Playing':
        jugada = input('Por favor ingrese el nro de la columna en la que desea poner su ficha: ')

        while jugada.isnumeric() == False or int(jugada) <= 0 or int(jugada) > len(state['board'][0]):
            print('El ingreso es incorrecto.')
            jugada = input('Por favor ingrese el nro de la columna en la que desea poner su ficha: ')
        
        newBoard = state['board'].copy()

        for numeroFila in reversed(range(0, len(newBoard))):

            if newBoard[numeroFila][int(jugada) - 1] == None:
                newBoard[numeroFila][int(jugada) - 1] = state['turn']
                break
        
        newTurn = (state['turn'] + 1) % len(state['players'])

        return {
            'type': 'CONTINUE_PLAYING',
            'payload': {
                'newBoard': newBoard,
                'newTurn': newTurn,
            }

        }


def render(state):
    if state['stage'] == 'LoadingPlayers':
        print(*state['players'], sep = "\n")

    if state['stage'] == 'LoadingBoard':
        print(*state['players'], sep = "\n")
    
    if state['stage'] == 'Playing':
        print(state['players'][state['turn']]['name'])
        for i in range(0, len(state['board'][0])):
            print(f'{i + 1}. Columna {i + 1}')

        print(*state['board'], sep='\n')


state = {
    'stage': 'LoadingPlayers',
    'players': [],
}

while True:
    render(state)
    action = get_next_action(state)
    state = reducer(state, action)