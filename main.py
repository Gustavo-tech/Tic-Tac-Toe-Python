def print_board(table : list = None):

    for line in range(0, 3):
        for column in range(0, 3):

            if column == 2:
                print(table[line][column])
            else:
                print(table[line][column], end="")


table = [['|  -  |', '|  -  |', '|  -  |'],
        ['|  -  |', '|  -  |', '|  -  |'],
        ['|  -  |', '|  -  |', '|  -  |']]

player1_name = input('Jogador 1, digite seu nome: ')
player2_name = input('Jogador 2, digite seu nome: ')

players_points = [0, 0]

continue_game = True
game_finished = False

while continue_game:

    current_round = 1
    current_player = 1

    while not game_finished:
        print_board(table)

        if current_round != 1:
            if current_player == 1:
                current_player += 1
            else:
                current_player -= 1

        break
    break
