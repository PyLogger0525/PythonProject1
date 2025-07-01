# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
#
# board = list(range(1, 10))
#
#
# def d_board(board):
#     print('-' * 13)
#     for i in range(3):
#         print("|", board[0 + i], "|", board[1 + i], "|", board[2 + i], "|")
#         print('-' * 13)
#
# d_board(board)
#
# def player_input(input_pos):
#     valid = False
#     while not valid:
#         player_answer = input('Куда ставим: ' + input_pos + '?')
#         try:
#             player_answer = int(player_answer)
#         except:
#             print('Некорректный ввод')
#         if player


numbers = '1 2 2 5 5 3 5 4'
num = numbers.split()
num1=set(num)
s=len(num1)
print(s)