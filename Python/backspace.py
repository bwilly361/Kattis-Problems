def backspace():
    string = list(input())
    new_string = []

    for char in string:
        if char == '<':
            new_string.pop()
        else:
            new_string.append(char)

    print(''.join(new_string))

if __name__ == '__main__':
    backspace()