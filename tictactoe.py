import random
import time
wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def check_game(game: str) -> str:
    """
    Checks the specified game and returns either\n
    a) the symbol (X or O) of the winning player\n
    b) 'DRAW' if the game result is a draw\n
    c) 'CONTINUE' if the game should play on
    """
    for w in wins:
        if game[w[0]] == game[w[1]] == game[w[2]] and game[w[0]] != " ":
            return game[w[0]]
    if not " " in game:
        return "DRAW"
    return "CONTINUE"

def check_2(game: str, turn:str):
    """
    Checks the specified game and returns either\n
    a) the symbol (X or O) of the winning player\n
    b) 'DRAW' if the game result is a draw\n
    c) 'CONTINUE' if the game should play on
    """
    for w in wins:
        if game[w[0]] == game[w[1]] and game[w[1]] != " " and game[w[2]]== " "and game[w[1]] == turn :
            
            return w[2]
        if game[w[0]] == game[w[2]] and game[w[2]] != " " and game[w[1]]== " "and game[w[2]] == turn :
            
            return w[1]
        if game[w[2]] == game[w[1]] and game[w[1]] != " " and game[w[0]]== " "and game[w[1]] == turn :
            
            return w[0]
            
    return "CONTINUE"

def print_game(game: str, index: bool) -> None:
    """
    Prints out the specified game in a human readable format\n
    index (bool) - whether to print spaces as spaces, or the index of the game\n
    Returns the string that was printed
    """
    pgame = f"{game[0:3]}\n{game[3:6]}\n{game[6:9]}\n"
    print(pgame)
    if index:
        pgame = ""
        for i, s in enumerate(game):
            if s == " ":
                pgame += str(i)
            else:
                pgame += s
            if (i+1) % 3 == 0:
                pgame += "\n"
        pgame += "\n"
        print(pgame)
    return pgame

def move(game: str, move: int, turn: str) -> str:
    """
    Makes the specified move in the specified game and returns the new game array\n
    Returns False if the move is invalid\n
    game (str) - the string containing the current state of the game\n
    move (int) - the index of the position in 'game' string that is being requested to be changed\n
    turn (str) - the symbol of the player wanting to make that move ('X' or 'O')
    """
    if game[move] != " ":
        return False
    modgame = ""
    for i, s in enumerate(game):
        if i != move:
            modgame += s
        else:
            modgame += turn
    return modgame

def new_game() -> str:
    return( " " * 9)


gt = 0
while True:
    g = new_game()
    gt=0
    avs = [0,1,2,3,4,5,6,7,8,9]
    tms = []
    yms = []
    mms = []
    m = 0
    print_game(g,True)
    while True:
        gt+=1
        m = int(input('chose number'))
        print_game(g,True)
        g = move(g,m,'X')
        print_game(g,True)
        avs.remove(m)
        tms.append(m)
        yms.append(m)
        if check_game(g)!='CONTINUE':
            print(check_game(g))
            time.sleep(3)
            break
        if gt == 1:
            if 5 in avs:
                g = move(g,5,'O')
                avs.remove(5)
                mms.append(5)
                tms.append(5)
            else:
                g = move(g,3,'O')
                avs.remove(3)
                mms.append(3)
                tms.append(3)               
        elif gt == 2:
            if check_2(g,'X') != 'CONTINUE':
                m = check_2(g,'X')
                g = move(g,m,'O')
                avs.remove(m)
                mms.append(m)
                tms.append(m)
            else:
                if mms[0] == 5:
                    if 0 in avs:
                        m = 0
                        g = move(g,m,'O')
                        avs.remove(m)
                        mms.append(m)
                        tms.append(m)
                    elif 6 in avs:
                        m = 6
                        g = move(g,m,'O')
                        avs.remove(m)
                        mms.append(m)
                        tms.append(m)
                elif mms[0]== 3:
                    if 2 in avs:
                        m = 2
                        g = move(g,m,'O')
                        avs.remove(m)
                        mms.append(m)
                        tms.append(m)
                    elif 8 in avs:
                        m = 8
                        g = move(g,m,'O')
                        avs.remove(m)
                        mms.append(m)
                        tms.append(m)
        else:
            if check_2(g,'X') != 'CONTINUE':
                m = check_2(g,'X')
                g = move(g,m,'O')
                avs.remove(m)
                mms.append(m)
                tms.append(m)
            elif check_2(g,'O') != 'CONTINUE':
                m = check_2(g,'X')
                g = move(g,m,'O')
                avs.remove(m)
                mms.append(m)
                tms.append(m)
            else:
                m = random.choice(avs)
                g = move(g,m,'O')
                avs.remove(m)
                mms.append(m)
                tms.append(m)
                


        print_game(g,True)
        if check_game(g) !='CONTINUE':
            print(check_game(g))
            time.sleep(3)
            break
