def thirteen_floors():
    floor = int(input())

    if floor >= 13:
        floor += 1
    else:
        pass
    
    print(floor)

if __name__ == '__main__':
    thirteen_floors()