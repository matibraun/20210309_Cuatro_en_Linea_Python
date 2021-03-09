'''
type State = LoadingPlayers | LoadingBoard | Playing | Ended;

type LoadingPlayers = {
    stage: 'LoadingPlayers';
    players: Array<PartialPlayer>;
;

type PartialPlayer = {
    name: string | null;
    color: string | null
};

type LoadingBoard = {
    stage: 'LoadingBoard';
    players: Array<Player>;
    rows: number | null;
    cols: number | null;
}

type Playing = {
    stage: 'Playing';
    players: Array<Player>;
    board: Board;
    turn: number;
}

type Board = Array<Array<number | null>>;

type Player = {
    name: string;
    color: string;
}

type Ended = {
    stage: 'Ended',
    players: Array<Player>;
    winner: number;
}

//---------------- ACTIONS

type Action = SetPlayerNameAction | SetPlayerColorAction | ...;

type SetPlayerNameAction = {
    type: 'SET_PLAYER_NAME',
    payload: { name: string; }
}

type SetPlayerColorAction = {
    type: 'SET_PLAYER_COLOR',
    payload: { color: string; }
}

'''

def reducer(state, action):
    if state['stage'] == 'LoadingPlayers':
        if action['type'] == 'SET_PLAYER_NAME':
            return {
                **state,
                'players': [
                    *state['players'],
                    {'name': action['payload']['name'], 'color': None}
                ],
            }

    return state


def render(state):
    # Se ocupa de mostrar el estado actual en pantalla. Es el artista, el que dibuja
    # Por ejemplo, si el estado es playing, dibuja el tablero y el turno.
    # Si el estado es LoadingPlayers, muestra los jugadores ya cargados.
    players_str = '\n'.join([player['name'] for player in state['players']])
    print(f'El estado es stage: {state["stage"]} players: {players_str}')


def get_next_action(state):
    # Aca por ejemplo, podes imprimir una lista numerada de las posibles
    # acciones, dado el estado actual, y segun el numero que elija, pedirle la info 
    # necesaria para completar la accion, y devolver un diccionario con el type y payload
    # correcto
    name = input('Ponga el nombre')
    return {
        'type': 'SET_PLAYER_NAME',
        'payload': {
            'name': name,
        }
    }


######

state = {
    'stage': 'LoadingPlayers',
    'players': [],
}

while True:
    print(render(state))
    action = get_next_action(state)
    state = reducer(state, action)
