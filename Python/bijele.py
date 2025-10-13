def bijele():
    king, queen, rooks, bishops, knights, pawns = map(int, input().split())

    king_num = 1 - king

    queen_num = 1 - queen

    rooks_num = 2 - rooks

    bishops_num = 2 - bishops

    knights_num = 2 - knights

    pawns_num = 8 - pawns

    print(str(king_num) + ' ' + str(queen_num) + ' ' + str(rooks_num) + ' ' + str(bishops_num) + ' ' + str(knights_num) + ' ' + str(pawns_num))

if __name__ == "__main__":
    bijele()