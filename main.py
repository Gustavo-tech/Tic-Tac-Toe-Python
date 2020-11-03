# Atualiza os pontos do jogo
def update_points(current_player: int = None, points: list = None):
    if current_player == 0:
        points[0] += 1
    else:
        points[1] += 1

# Mostra as estátisticas do jogo
def show_winner_stats(current_player: int = None, player_names: list = None, rounds: int = None, points: list = None):
    print("\n")
    print("----------- Game stats --------------")
    print(f"{player_names[current_player]} VENCEU!!!!!")
    print(f"Foram jogados {rounds} rounds para acabar a partida")
    print(f"{player_names[0]} {points[0]} X {player_names[1]} {points[1]}")

# Converte se a pessoa deseja continuar o jogo
def convert_continue(text: str = None):
    text = text.upper()

    if text == "YES":
        return True
    else:
        return False

# Converte a linha para o número correto
def convert_line(line: str = None):
    line = int(line)
    line -= 1
    return str(line)

# Converte a coluna para número
def convert_column(column: str = None):
    if column == 'A':
        return '0'
    elif column == 'B':
        return '1'
    elif column == 'C':
        return '2'
    else:
        return None

# Valida a posição desejada pelo jogador
def validate_position(table: list = None, position: str = None):
    valid = True

    if position is None:
        valid = False

    if position[1] is None:
        valid = False

    if table[int(position[0])][int(position[1])] != '|  -  |':
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
    players_texts = ['|  X  |', '|  O  |']

    somebody_won = False
    for player_text in players_texts:
        # Verifica todas as linhas
        if table[0][0] == table[0][1] == table[0][2] == player_text:
            somebody_won = True
        elif table[1][0] == table[1][1] == table[1][2] == player_text:
            somebody_won = True
        elif table[2][0] == table[2][1] == table[2][2] == player_text:
            somebody_won = True

        # Verifica todas as colunas
        elif table[0][0] == table[1][0] == table[2][0] == player_text:
            somebody_won = True
        elif table[0][1] == table[1][1] == table[2][1] == player_text:
            somebody_won = True
        elif table[0][2] == table[1][2] == table[2][2] == player_text:
            somebody_won = True

        # Verifica as diagonais
        elif table[0][0] == table[1][1] == table[2][2] == player_text:
            somebody_won = True
        elif table[2][0] == table[1][1] == table[0][3] == player_text:
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


players_names = save_player_name()
players_points = [0, 0]

continue_game = True
game_finished = False

while continue_game:

    current_round = 0
    current_player = 0
    table = [['|  -  |', '|  -  |', '|  -  |'],
             ['|  -  |', '|  -  |', '|  -  |'],
             ['|  -  |', '|  -  |', '|  -  |']]

    while not game_finished:
        print("\n")
        current_round += 1
        print_board(table)
        current_player = check_current_player(current_round, current_player)

        position = input("Digite a linha e coluna que deseja preencher: ").upper()
        position = position.replace(position[0], convert_line(position[0]))
        position = position.replace(position[1], convert_column(position[1]))
        valid_position = validate_position(table, position)

        while not valid_position:
            print("Jogada inválida, por favor escolha novamente")
            position = input("Digite a linha e coluna que deseja preencher: ")
            valid_position = validate_position(table, position)

        if current_player == 0:
            table[int(position[0])][int(position[1])] = '|  X  |'
        else:
            table[int(position[0])][int(position[1])] = '|  O  |'

        if current_round >= 5:
            game_finished = check_player_play(table)

            if game_finished:
                update_points(current_player, players_points)

    print_board(table)
    show_winner_stats(current_player, players_names, current_round, players_points)
    continue_game_string = input("Continuar jogo? YES/NO: ")
    continue_game = convert_continue(continue_game_string)

    if continue_game:
        game_finished = False
