def turn_it_up():
    n = int(input())

    volume = 7

    for i in range(n):
        request = input()
        if request == 'Skru op!':
            if volume < 10:
                volume += 1
                #print('volume up to ' + str(volume))
            else:
                pass
        else:
            if volume > 0:
                volume -= 1
            else:
                pass
            #print('volume down ' + str(volume))

    print(volume)

if __name__ == "__main__":
    turn_it_up()