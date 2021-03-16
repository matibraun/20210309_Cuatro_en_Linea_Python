import time
import os

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

def checkWinner(board):
    for nroFila in range(0, len(board) - 3):
        for nroCol in range(0, len(board[nroFila])):
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila + 1][nroCol] and board[nroFila][nroCol] == board[nroFila + 2][nroCol] and board[nroFila][nroCol] == board[nroFila + 3][nroCol]:
                return True

    for nroFila in range(0, len(board)):
        for nroCol in range(0, len(board[nroFila]) - 3):
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila][nroCol + 1] and board[nroFila][nroCol] == board[nroFila][nroCol + 2] and board[nroFila][nroCol] == board[nroFila][nroCol + 3]:
                return True

    for nroFila in range(0, len(board) - 3):
        for nroCol in range(0, len(board[nroFila]) - 3):
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila + 1][nroCol + 1] and board[nroFila][nroCol] == board[nroFila + 2][nroCol + 2] and board[nroFila][nroCol] == board[nroFila + 3][nroCol + 3]:
                return True

    for nroFila in range(0, len(board) - 3):
        for nroCol in range(3, len(board[nroFila])):
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila + 1][nroCol - 1] and board[nroFila][nroCol] == board[nroFila + 2][nroCol - 2] and board[nroFila][nroCol] == board[nroFila + 3][nroCol - 3]:
                return True

def checkIfBoardFull(board):
    if None not in board[0]:
        return True

def displayHistoricBoards(historicBoards):
    for board in historicBoards:
        os.system('cls') 
        print('\n'.join([str(line) for line in board]))
        time.sleep(1.3)


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
                'board': action['payload']['board'],
                # 'historicBoards': action['payload']['board'].copy(),
                'turn': 0,
            }


    if state['stage'] == 'Playing':
        if action['type'] == 'CONTINUE_PLAYING':
            return {
                'stage': 'Playing',
                'players': state['players'],
                'board': action['payload']['newBoard'],
                # 'historicBoards': action['payload']['newHistoricBoards'],
                'turn': action['payload']['newTurn'],
            }   

    if state['stage'] == 'Playing':
        if action['type'] == 'THERE_IS_A_WINNER':
            return {
                'stage': 'EndedWithWinner',
                'players': state['players'],
                'board': action['payload']['newBoard'],
                # 'historicBoards': action['payload']['newHistoricBoards'],
                'turn': action['payload']['turn'],
                'message': 'el ganador es ',
            }

    if state['stage'] == 'Playing':
        if action['type'] == 'GAME_FINISHED_WITHOUT_WINNER':
            return {
                'stage': 'EndedWithoutWinner',
                'players': state['players'],
                'board': action['payload']['newBoard'],
                # 'historicBoards': action['payload']['newHistoricBoards'],
                'turn': action['payload']['turn'],
                'message': 'el ganador es ',
            }



    if state['stage'] == 'EndedWithWinner' or state['stage'] == 'EndedWithoutWinner':
        if action['type'] == 'CLOSE_GAME':
            return {
                'stage': 'AfterGameOptions',
                'players': state['players'],
                'board': state['board'],
                # 'historicBoards': state['historicBoards'],
            }


    
    if state['stage'] == 'AfterGameOptions':
        if action['type'] == 'REVIEW_GAME':
            return {
                'stage': 'AfterGameOptions',
                'players': state['players'],
                'board': state['board'],
                # 'historicBoards': state['historicBoards'],
            }

        if action['type'] == 'REMATCH':
            return {
                'stage': 'Playing',
                'players': state['players'],
                'board': state['board'],
                # 'historicBoards': [],
                'turn': 0
            }
    
        if action['type'] == 'NEW_GAME':
            return {
                'stage': 'LoadingPlayers',
                'players': [],
            }

        if action['type'] == 'CLOSE_APP':
            return {
                'stage': 'ClosingApp',
                'players': state['players'],
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
                )

            while option != '1' and option != '2':

                option = input(
                    'El ingreso es incorrecto.\n'
                    '1. Cargar otro jugador\n'
                    '2. Finalizar carga de jugadores\n'
                    )

            if option == '1':
                return crearJugador()
            
            if option == '2':
                return {
                    'type': 'FINISHED_LOADING_PLAYERS'
                }
    
    if state['stage'] == 'LoadingBoard':

        cantFilas = input('Por favor ingrese la cantidad de filas: ')
        cantColumnas = input('Por favor ingrese la cantidad de columnas: ')

        while cantFilas.isnumeric() == False or cantColumnas.isnumeric() == False or int(cantFilas) < 4 or int(cantColumnas) < 4:
            print ('Los valores ingresados son incorrectos.\n')
            cantFilas = input('Por favor ingrese la cantidad de filas: ')
            cantColumnas = input('Por favor ingrese la cantidad de columnas: ')

        filaProvisoria = []
        board = []

        for x in range(int(cantColumnas)):
            filaProvisoria.append(None)

        for x in range(int(cantFilas)):
            board.append(filaProvisoria.copy())

        return {
            'type': 'FINISHED_LOADING_AND_CREATING_BOARD',
            'payload': {
                'board': board,
                }
        }

    if state['stage'] == 'Playing':
        jugada = input('Por favor ingrese el nro de la columna en la que desea poner su ficha: ')

        while jugada.isnumeric() == False or int(jugada) <= 0 or int(jugada) > len(state['board'][0]):
            print('El ingreso es incorrecto.')
            jugada = input('Por favor ingrese el nro de la columna en la que desea poner su ficha: ')
        
        while state['board'][0][int(jugada) - 1] != None:
            print('La columna seleccionada ya esta llena.')
            jugada = input('Por favor ingrese el nro de la columna en la que desea poner su ficha: ')
        

        for numeroFila in reversed(range(0, len(state['board']))):

            if state['board'][numeroFila][int(jugada) - 1] == None:
                state['board'][numeroFila][int(jugada) - 1] = state['players'][state['turn']]['name']
                break
        
        # newHistoricBoards = [state['historicBoards']].append(state['board']) 
        
        newTurn = (state['turn'] + 1) % len(state['players'])

        if checkWinner(state['board']) == True:
            return {
                'type': 'THERE_IS_A_WINNER',
                'payload': {
                    'newBoard': state['board'],
                    # 'newHistoricBoards': newHistoricBoards,
                    'turn': state['turn'],
                }

            }
        
        elif checkIfBoardFull(state['board']) == True:
            return {
                'type': 'GAME_FINISHED_WITHOUT_WINNER',
                'payload': {
                    'newBoard': state['board'],
                    # 'newHistoricBoards': newHistoricBoards,
                    'turn': state['turn'],
                }

            }

        else:
            return {
                'type': 'CONTINUE_PLAYING',
                'payload': {
                    'newBoard': state['board'],
                    # 'newHistoricBoards': newHistoricBoards,
                    'newTurn': newTurn,
                }

            }
    
    if state['stage'] == 'EndedWithWinner' or state['stage'] == 'EndedWithoutWinner':
        return {
            'type': 'CLOSE_GAME',
        }
    
    if state['stage'] == 'AfterGameOptions':

        option = input(
            'Por favor ingrese la opcion seleccionada: \n'
            '1. Visualizar la partida completa.\n'
            '2. Jugar la revancha con los mismos jugadores y tablero.\n'
            '3. Crear una nueva partida.\n'
            '4. Salir del juego.\n'
            )

        while option.isnumeric() == False or int(option) < 1 or int(option) > 4:
            print ('El ingreso es incorrecto')
            option = input(
                'Por favor ingrese la opcion seleccionada: \n'
                '1. Visualizar la partida completa.\n'
                '2. Jugar la revancha con los mismos jugadores y tablero.\n'
                '3. Crear una nueva partida.\n'
                '4. Salir del juego.\n'
                )
        
        if option == '1':
            return {
                'type': 'REVIEW_GAME',
            }

        if option == '2':
            return {
                'type': 'REMATCH',
            }

        if option == '3':
            return {
                'type': 'NEW_GAME',
            }
        
        if option == '4':
            return {
                'type': 'CLOSE_APP',
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

    if state['stage'] == 'EndedWithWinner':
        print(f"El ganador es {state['players'][state['turn']]['name']}!!!!!!!")
        print("Los jugadores fueron:")
        print('\n'.join([str(i['name']) for i in state['players']]))
        print(f"El tablero completo es el siguiente:")
        print('\n'.join([str(i) for i in state['board']]))


    if state['stage'] == 'EndedWithoutWinner':
        print("El juego ha finalizado sin ningun ganador")
        print("Los jugadores fueron:")
        print('\n'.join([str(i['name']) for i in state['players']]))
        print(f"El tablero completo es el siguiente:")
        print('\n'.join([str(i) for i in state['board']]))

    if state['stage'] == 'AfterGameOptions':
        pass

    if state['stage'] == 'ClosingApp':
        print("Gracias por jugar 4 en linea")
        print('\n'.join([str(i['name']) for i in state['players']]))
        exit()



state = {
    'stage': 'LoadingPlayers',
    'players': [],
}

while True:
    render(state)
    action = get_next_action(state)
    state = reducer(state, action)