print("Вас приветсвует игра крестики-нолики!")
print("Правила классические")
print("Для хода введите номер строки и солбца через пробел, а затем нажмите enter")


def print_board(board):
    print("  0 1 2")
    for i in range(3):
        row = f"{i} " + " ".join(board[i])
        print(row)


def check_winner(board, player):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combination in winning_combinations:
        if all(board[row][col] == player for row, col in combination):
            return True
    return False


def is_draw(board):
    return all(cell != '-' for row in board for cell in row)


def get_move(player):
    while True:
        try:
            move = input("Игрок " + player + ", ваш ход: ")
            row, col = map(int, move.split())
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Координаты должны быть от 0 до 2.")
        except ValueError:
            print("Пожалуйста, введите два числа через пробел и нажмите Enter.")


def play_game():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = get_move(current_player)
        if board[row][col] == '-':
            board[row][col] = current_player
        else:
            print("Эта ячейка уже занята. Повторите попытку")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print("Игрок " + current_player + " победил!")
            break
        if is_draw(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

def ask_restart():
    while True:
        answer = input("Ещё партию? Введите (y/n) и нажмите Enter: ").lower()
        if answer in ['y']:
            return True
        elif answer in ['n']:
            return False
        else:
            print("Введите 'n' для да или 'n' для нет.")

if __name__ == "__main__":
    while True:
        play_game()
        if not ask_restart():
            print("Спасибо за игру!")
            break