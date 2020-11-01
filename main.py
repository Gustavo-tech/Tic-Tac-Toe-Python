# Converte a coluna para número
def convert_column(column: str = None):
    if column == 'A':
        return 0
    elif column == 'B':
        return 1
    elif column == 'C':
        return 2
    else:
        return None

# Valida a posição desejada pelo jogador
def validate_position(table: list = None, position: str = None):
    valid = True
    if position is None:
        valid = False
    else:
        position[1] = convert_column(position[1])

    if position[1] is None:
        valid = False

    return valid

# Salva o nome dos jogadores
def save_player_name():
    player1_name = input('Jogador 1, digite seu nome: ')
    player2_name = input('Jogador 2, digite seu nome: ')

    return [player1_name, player2_name]


# Verifica o atual jogador
def check_current_player(current_round: int = None, current_player: int = None):

    if current_round != 1:
        if current_player == 0:
            current_player += 1
        else:
            current_player -= 1
    return current_player

# Verifica se alguém ganhou o jogo
def check_player_play(table: list = None):

    somebody_won = False

    # Verifica todas as linhas
    if table[1][1] == table[1][2] == table[1][3]:
        somebody_won = True
    elif table[2][1] == table[2][2] == table[2][3]:
        somebody_won = True
    elif table[3][1] == table[3][2] == table[3][3]:
        somebody_won = True

    # Verifica todas as colunas
    elif table[1][1] == table[2][1] == table[3][1]:
        somebody_won = True
    elif table[1][2] == table[2][2] == table[3][2]:
        somebody_won = True
    elif table[1][3] == table[2][3] == table[3][3]:
        somebody_won = True

    # Verifica as diagonais
    elif table[1][1] == table[2][2] == table[3][3]:
        somebody_won = True
    elif table[1][3] == table[2][2] == table[3][1]:
        somebody_won = True

    return somebody_won


# Imprime o tabuleiro
def print_board(table: list = None):
    print("      Col A  Col B  Col C")
    for line in range(0, 3):
        print(f"Lin {line + 1}", end="")
        for column in range(0, 3):
            if column == 2:
                print(table[line][column])
            else:
                print(table[line][column], end="")


table = [['|  -  |', '|  -  |', '|  -  |'],
        ['|  -  |', '|  -  |', '|  -  |'],
        ['|  -  |', '|  -  |', '|  -  |']]

players_name = save_player_name()
players_points = [0, 0]

continue_game = True
game_finished = False

while continue_game:

    current_round = 1
    current_player = 0
    while not game_finished:
        print("\n")
        print_board(table)
        current_player = check_current_player(current_round, current_player)

        position = input("Digite a linha e coluna que deseja preencher: ")




        break
    break
