# 1. Создайте программу для игры в ""Крестики-нолики"".

map = list(range(1, 10))

def print_map():
    print(map[0], end=' ')
    print(map[1], end=' ')
    print(map[2])
    
    print(map[3], end=' ')
    print(map[4], end=' ')
    print(map[5])
    
    print(map[6], end=' ')
    print(map[7], end=' ')
    print(map[8])

variable = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
def result():
    win = ''
    for i in variable:
        if map[i[0]] == 'X' and map[i[1]] == 'X' and map[i[2]] == 'X':
            win = 'X'
        if map[i[0]] == 'O' and map[i[1]] == 'O' and map[i[2]] == 'O':
            win = 'O'
    return win

def step_map(step, char):
    ind = map.index(step)
    map[ind] = char
    
game_over = False
player_1 = True

while game_over == False:
    print_map()
    if player_1 == True:
        char = 'X'
        step = int(input('Ход первого игрока: '))
    else:
        char = 'O'
        step = int(input('Ход второго игрока: '))
    
    step_map(step, char)
    win = result()
    
    if win != '':
        game_over = True
    else:
        game_over = False
    
    player_1 = not(player_1)
    
print_map()
print('Победил', win)