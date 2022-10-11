# 3.1 Создайте программу для игры в ""Крестики-нолики"".

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("Выш ход," + turn + ".Куда поставить знак?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Эта позиция уже занята.\nКуда поставить знак?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard[
                '9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard[
                '6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard[
                '3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard[
                '7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard[
                '8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard[
                '9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard[
                '3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard[
                '9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nКонец игры.\n")
                print(" **** " + turn + " победа. ****")
                break

        if count == 9:
            print("\nКонец игры.\n")
            print("Ничья!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Хотите сыграть ещё раз?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()