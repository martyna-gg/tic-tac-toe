game = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

#  Print Board
def board():
    print('---------')
    print('| ' + game[0][0] + ' ' + game[0][1] + ' ' + game[0][2] + ' |')
    print('| ' + game[1][0] + ' ' + game[1][1] + ' ' + game[1][2] + ' |')
    print('| ' + game[2][0] + ' ' + game[2][1] + ' ' + game[2][2] + ' |')
    print('---------')

board()

#  Check if 'a' wins
def win(a):
    for x in range(3):
        if ((game[x][0] == game[x][1] == game[x][2] == a) or
        (game[0][x] == game[1][x] == game[2][x] == a) or
        (game[0][0] == game[1][1] == game[2][2] == a) or
        (game[0][2] == game[1][1] == game[2][0] == a)):
            return True


def moves(n):               
    new_move = []
    move = input('give me two coordinates of your  next move, please:').split()
    while new_move == []:
        try:
            new_move.append(int(move[0]))
            new_move.append(int(move[1]))
        except ValueError:
            print('You should enter numbers!')
            new_move = []
            move = input('give me two coordinates of your  next move, please:').split()
        except IndexError:
            print('You should enter two numbers!')
            new_move = []
            move = input('give me two coordinates of your  next move, please:').split()
        else:
            if new_move not in [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]:
                print('Coordinates should be from 1 to 3!')
                new_move = []
                move = input('give me two coordinates of your  next move, please:').split()
            else:
                if game[new_move[0]-1][new_move[1]-1] != ' ':
                    print('This cell is occupied! Choose another one!')
                    new_move = []
                    move = input('give me two coordinates of your  next move, please:').split()
                else:
                    game[new_move[0]-1][new_move[1]-1] = n
                    board()
i=0                    
turns=['X','O']
while not all([bool(game[i][j] != ' ') for i in range(3) for j in range(3)]):
    moves(turns[i%2])
    if win(turns[i%2]):
        print(turns[i%2], 'wins')
        break
    i+=1

if all([bool(game[i][j] != ' ') for i in range(3) for j in range(3)]):
    print('Draw')
    