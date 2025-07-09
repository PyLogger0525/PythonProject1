
board=list(range(1,10))                                                                                                 # создаем список от 1 до 10


def board_size(board):
    print("-" * 18)
    for i in range(3):                                                                                                  # циклом разбиваем список board на поле из 3 столбцов, т.е. формируем поле 3х3
        print("| ", board[0+i*3], "| ", board[1+i*3], " | ", board[2+i*3], " | ")
        print("-"*18)

def pos_input(board_position):
    pos=False
    while not pos:
        player_pos = input("Введите число, игрок:" + board_position + " ")
        try:
            player_pos = int(player_pos)
        except:
            print("Введен не подходящий символ")
            continue
        if player_pos>=1 and player_pos<=9:
            if (str(board[player_pos -1]) not in "XO"):
                board[player_pos - 1] = board_position
                pos=True
            else:
                print("Клетка занята!")
        else:
            print("Введите число от 1 до 9")

def win_board(board):
    win_comb= ((0, 1, 2), (0, 3, 6), (1, 4, 7), (2, 5, 8), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6))
    for i in win_comb:                                                                                                  # циклом проверяем выигрышные комбинации (координаты)
        if board[i[0]] == board[i[1]] == board[i[2]]:                                                                   # если символы совпадают с символом на первой координате, он возвращается как выигрышный
            return board[i[0]]
    return False

def main(board):
    counter=0
    win=False
    while not win:
        board_size(board)
        if counter%2 == 0:
            pos_input("X")
        else:
            pos_input("O")
        counter+=1
        if counter>4:
            if win_board(board):
                print(win_board(board), "Вы выиграли")
                win=True
                break
        if counter == 9:
            print("Ничья")
            break
    board_size(board)
main(board)