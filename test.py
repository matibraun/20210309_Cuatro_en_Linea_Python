turno = 0
jugadores = ['ju1', 'ju2', 'ju3', 'ju4']
print(jugadores[turno])
while True:
    input('pres enter para prox turno')
    turno += 1
    print (jugadores[turno % len(jugadores)])
    