newBoard = [
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, None, None, None, None], 
    [None, None, None, None, None, None, 1, 1, 1, 1], 
]

def checkWinner(board):
    for nroFila in range(0, len(board)):
        for nroCol in range(0, len(board[nroFila])):
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila - 1][nroCol] and board[nroFila][nroCol] == board[nroFila - 2][nroCol] and board[nroFila][nroCol] == board[nroFila - 3][nroCol]:
                print('hay ganador')

            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila][nroCol - 1] and board[nroFila][nroCol] == board[nroFila][nroCol - 2] and board[nroFila][nroCol - 3] == board[nroFila][nroCol]:
                print('hay ganador') 
                
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila - 1][nroCol - 1] and board[nroFila][nroCol] == board[nroFila - 2][nroCol - 2] and board[nroFila - 3][nroCol - 3] == board[nroFila][nroCol]:
                print('hay ganador')
            
            if board[nroFila][nroCol] != None and board[nroFila][nroCol] == board[nroFila + 1][nroCol + 1] and board[nroFila][nroCol] == board[nroFila + 2][nroCol + 2] and board[nroFila + 3][nroCol + 3] == board[nroFila][nroCol]:
                print('hay ganador')



checkWinner(newBoard)