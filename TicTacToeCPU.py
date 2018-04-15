
theBoard = {'topL':'   ','topM':'   ','topR':'   ',
            'midL':'   ','midM':'   ','midR':'   ',
            'lowL':'   ','lowM':'   ','lowR':'   '}
def WinCondition():
    #checks for 3 in a row
    global R
    global turn
    global winner
    j = turn
    if theBoard['topL']==j and theBoard['topM']==j and theBoard['topR']==j:
    
        
        R = 0
        
        winner = turn
    elif theBoard['topL']==j and theBoard['midL']==j and theBoard['lowL']==j:
        
        R = 0
        
        
        winner = turn
    elif theBoard['midL']==j and theBoard['midM']==j and theBoard['midR']==j:
        
        R = 0
        
        
        winner = turn
    elif theBoard['lowL']==j and theBoard['lowM']==j and theBoard['lowR']==j:
        R = 0
        
        
        winner = turn
    elif theBoard['topM']==j and theBoard['midM']==j and theBoard['lowM']==j:
        
        R = 0
        
        
        winner = turn
    elif theBoard['topR']==j and theBoard['midR']==j and theBoard['lowR']==j:  
        R = 0
        
        
        winner = turn
    elif theBoard['topL']==j and theBoard['midM']==j and theBoard['lowR']==j:
        R = 0
        
        
        winner = turn

    elif theBoard['topR']==j and theBoard['midM']==j and theBoard['lowL']==j: 
        R = 0
        
        
        winner = turn
def Oblock():
    #checks for 2 X's in a row
    global move
    j = ' X '
    if theBoard['topL']==j and theBoard['topM']==j and theBoard['topR']=='   ':
        move = 'topR'
    elif theBoard['topL']==j and theBoard['topR']==j and theBoard['topM']=='   ':
        move = 'topM'
    elif theBoard['topM']==j and theBoard['topR']==j and theBoard['topL']=='   ':
        move = 'topL'
    elif theBoard['topL']==j and theBoard['midL']==j and theBoard['lowL']=='   ':
        move = 'lowL'
    elif theBoard['topL']==j and theBoard['lowL']==j and theBoard['midL']=='   ':
        move = 'midL'
    elif theBoard['midL']==j and theBoard['lowL']==j and theBoard['topL']=='   ':
        move = 'topL'
    elif theBoard['midL']==j and theBoard['midM']==j and theBoard['midR']=='   ':
        move = 'midR'
    elif theBoard['midL']==j and theBoard['midR']==j and theBoard['midM']=='   ':
        move = 'midM'
    elif theBoard['midM']==j and theBoard['midR']==j and theBoard['midL']=='   ':
        move = 'midL'
    elif theBoard['lowL']==j and theBoard['lowM']==j and theBoard['lowR']=='   ':
        move = 'lowR'
    elif theBoard['lowL']==j and theBoard['lowR']==j and theBoard['lowM']=='   ':
        move = 'lowM'
    elif theBoard['lowM']==j and theBoard['lowR']==j and theBoard['lowL']=='   ':
        move = 'lowL'
    elif theBoard['topM']=='   ' and theBoard['midM']==j and theBoard['lowM']==j:
        move = 'topM'
    elif theBoard['topM']==j and theBoard['midM']=='   ' and theBoard['lowM']==j:
        move = 'midM'
    elif theBoard['topM']==j and theBoard['midM']==j and theBoard['lowM']=='   ':
        move = 'lowM'
    elif theBoard['topR']==j and theBoard['midR']==j and theBoard['lowR']=='   ':
        move = 'lowR'
    elif theBoard['topR']==j and theBoard['midR']=='   ' and theBoard['lowR']==j:
        move = 'midR'
    elif theBoard['topR']=='   ' and theBoard['midR']==j and theBoard['lowR']==j:
        move = 'topR'
    elif theBoard['topL']==j and theBoard['midM']==j and theBoard['lowR']=='   ':
        move = 'lowR'
    elif theBoard['topL']==j and theBoard['midM']=='   ' and theBoard['lowR']==j:
        move = 'midM'
    elif theBoard['topL']=='   ' and theBoard['midM']==j and theBoard['lowR']==j:
        move = 'topL'
    elif theBoard['topR']==j and theBoard['midM']==j and theBoard['lowL']=='   ':
        move = 'lowL'
    elif theBoard['topR']==j and theBoard['midM']=='   ' and theBoard['lowL']==j:
        move = 'midM'
    elif theBoard['topR']=='   ' and theBoard['midM']==j and theBoard['lowL']==j:
        move = 'topR'
def Owin():
    #checks for 2 O's in a row
    global move
    j = ' O '
    if theBoard['topL']==j and theBoard['topM']==j and theBoard['topR']=='   ':
        move = 'topR'
    elif theBoard['topL']==j and theBoard['topR']==j and theBoard['topM']=='   ':
        move = 'topM'
    elif theBoard['topM']==j and theBoard['topR']==j and theBoard['topL']=='   ':
        move = 'topL'
    elif theBoard['topL']==j and theBoard['midL']==j and theBoard['lowL']=='   ':
        move = 'lowL'
    elif theBoard['topL']==j and theBoard['lowL']==j and theBoard['midL']=='   ':
        move = 'midL'
    elif theBoard['midL']==j and theBoard['lowL']==j and theBoard['topL']=='   ':
        move = 'topL'
    elif theBoard['midL']==j and theBoard['midM']==j and theBoard['midR']=='   ':
        move = 'midR'
    elif theBoard['midL']==j and theBoard['midR']==j and theBoard['midM']=='   ':
        move = 'midM'
    elif theBoard['midM']==j and theBoard['midR']==j and theBoard['midL']=='   ':
        move = 'midL'
    elif theBoard['lowL']==j and theBoard['lowM']==j and theBoard['lowR']=='   ':
        move = 'lowR'
    elif theBoard['lowL']==j and theBoard['lowR']==j and theBoard['lowM']=='   ':
        move = 'lowM'
    elif theBoard['lowM']==j and theBoard['lowR']==j and theBoard['lowL']=='   ':
        move = 'lowL'
    elif theBoard['topM']=='   ' and theBoard['midM']==j and theBoard['lowM']==j:
        move = 'topM'
    elif theBoard['topM']==j and theBoard['midM']=='   ' and theBoard['lowM']==j:
        move = 'midM'
    elif theBoard['topM']==j and theBoard['midM']==j and theBoard['lowM']=='   ':
        move = 'lowM'
    elif theBoard['topR']==j and theBoard['midR']==j and theBoard['lowR']=='   ':
        move = 'lowR'
    elif theBoard['topR']==j and theBoard['midR']=='   ' and theBoard['lowR']==j:
        move = 'midR'
    elif theBoard['topR']=='   ' and theBoard['midR']==j and theBoard['lowR']==j:
        move = 'topR'
    elif theBoard['topL']==j and theBoard['midM']==j and theBoard['lowR']=='   ':
        move = 'lowR'
    elif theBoard['topL']==j and theBoard['midM']=='   ' and theBoard['lowR']==j:
        move = 'midM'
    elif theBoard['topL']=='   ' and theBoard['midM']==j and theBoard['lowR']==j:
        move = 'topL'
    elif theBoard['topR']==j and theBoard['midM']==j and theBoard['lowL']=='   ':
        move = 'lowL'
    elif theBoard['topR']==j and theBoard['midM']=='   ' and theBoard['lowL']==j:
        move = 'midM'
    elif theBoard['topR']=='   ' and theBoard['midM']==j and theBoard['lowL']==j:
        move = 'topR'        
def printBoard(board):
    #prints the board
    print(board['topL']+'|'+ board['topM']+'|'+ board['topR'])
    print('---+---+---')
    print(board['midL']+'|'+ board['midM']+'|'+ board['midR'])
    print('---+---+---')
    print(board['lowL']+'|'+ board['lowM']+'|'+ board['lowR'])
R = 581
winner = 'No one'
turn = ' X '
print('Moves are done using the following commands:')
x=1
for each in theBoard:
	if x<=3:
		print(each+', ',end='')
	x+=1
	if x==4:
		print('',end='\n')
		x=1
print('Who should go first? (X or O)')
firstturn = input()
if firstturn == 'O':
    turn = ' O '
for i in range(9):
    if turn == ' X ':
        printBoard(theBoard)
        print('Turn for:' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        WinCondition()
        if R == 0:
            break
        turn = ' O '
    elif turn == ' O ':
        if i == 0:
            move = 'topL'
        elif i == 2:
            if theBoard['midM'] == ' X ':
                move = 'lowR'
            else:
                if theBoard['topM'] != ' X ' and theBoard['topR'] != ' X ':
                    move = 'topR'
                else:
                    move = 'lowL'
        elif i == 4:
            if theBoard['midM'] == ' X ':
                if theBoard['lowL'] == ' X ':
                    move = 'topR'
                    Owin()
                elif theBoard['topR'] == ' X ':
                   move = 'lowL'
                   Owin()
                else:
                    Oblock()
                    Owin()
            elif theBoard['midL'] == ' X ' and theBoard['lowL'] == ' O ':
                move = 'midM'
                Owin()
            elif theBoard['topM'] == ' X ' and theBoard['topR'] == ' O ':
                move = 'midM'
                Owin()
            else:
                Oblock()
                Owin()
        elif i == 6:
            Oblock()
            Owin()
        elif i == 8:
            move = 'A'
            Oblock()
            Owin()
        elif i == 1:
            if theBoard['midM'] != ' X ':
                move = 'midM'
            else:
                move = 'topL'
        elif i == 3:
            if theBoard['midM'] == ' O ':
                if theBoard['topL'] != ' X ' and theBoard['topR'] != ' X ' and theBoard['lowL'] != ' X ' and theBoard['lowR'] != ' X ':
                    if theBoard['lowM'] != ' X ' and theBoard['midR'] != ' X ':
                        if theBoard ['topM'] != ' X 'and theBoard['topL'] != ' X ':
                            move = 'topL'
                        else:
                            move = 'topR'
                    elif theBoard['topM'] != ' X ':
                        move = 'topM'
                    else:
                        move = 'lowM'
                else:
                    print('ERROR')
                    break
                #can't figure this out RN. Just let the CPU go first.
            else:
                move = 'midM'
                Oblock()
                Owin()
        else:
            Oblock()
            Owin()
        if move == 'A':
            break
        theBoard[move] = turn
        WinCondition()
        if R == 0:
            break
        turn = ' X '
printBoard(theBoard)

print('Game Over. ' + winner + ' won!')
