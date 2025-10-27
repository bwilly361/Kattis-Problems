def stafur():
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    letter = input()

    if letter in vowels:
        print('Jebb')
    elif letter in consonants:
        print('Neibb')
    else:
        print('Kannski')

if __name__ == '__main__':
    stafur()