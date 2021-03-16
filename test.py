import time
import os

historicBoards = [
    [
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
        [None, None, None, None, None, None, None, None, None,],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
        [1, 1, 1, 1, 1, 1, 1, 1, 1,],
    ],
    [
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
        [2, 2, 2, 2, 2, 2, 2, 2, 2,],
    ],
    [
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
        [3, 3, 3, 3, 3, 3, 3, 3, 3,],
    ],
    [
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
        [4, 4, 4, 4, 4, 4, 4, 4, 4,],
    ],
]


def displayHistoricBoards(historicBoards):
    for board in historicBoards:
        os.system('cls') 
        print('\n'.join([str(line) for line in board]))
        time.sleep(1.3)
        

displayHistoricBoards(historicBoards)