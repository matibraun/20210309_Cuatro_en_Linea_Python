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


action = crearJugador()

print(action['type'])