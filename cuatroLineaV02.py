def reducer(state, action):
    if state['stage'] == 'LoadingPlayers':
        if action['type'] == 'SET_PLAYER_NAME_AND_COLOR':
            return {
                **state,
                'players': [
                    *state['players'],
                    {'name': action['payload']['name'], 'color': action['payload']['color']}
                ],
            };

        elif action['type'] == 'SET_BOARD':
            state['stage'] = 'LoadingBoard'

    return state


def crearJugador ():
    name = input('Ingrese el nombre del jugador: ')
    color = input('Ingrese el color del jugador: ')
    return {
        'type': 'SET_PLAYER_NAME_AND_COLOR',
        'payload': {
            'name': name,
            'color': color,
        }
    };

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
                    'type': 'SET_BOARD'
                };
    
    if state['stage'] == 'LoadingBoard':

        filas = input('Por favor ingrese la cantidad de filas: ');
        columnas = input('Por favor ingrese la cantidad de columnas: ');

        while filas.isnumeric() == False or columnas.isnumeric() == False:
            print ('Los valores ingresados son incorrectos.\n')
            filas = input('Por favor ingrese la cantidad de filas: ');
            columnas = input('Por favor ingrese la cantidad de columnas: ');


    

def render(state):
    if state['stage'] == 'LoadingPlayers':
        print(*state['players'], sep = "\n");



state = {
    'stage': 'LoadingPlayers',
    'players': [],
}

while True:
    print(render(state))
    action = get_next_action(state)
    state = reducer(state, action)