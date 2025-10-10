def eye_of_sauron():
    eye = input()
    eye_list = list(eye)
    eye_length = len(eye_list)

    left_side_length = eye_list.index('(')

    right_parenth = eye_list.index(')') + 1
    right_side_length = eye_length - right_parenth

    if left_side_length == right_side_length:
        print('correct')
    else:
        print('fix')

if __name__ == "__main__":
    eye_of_sauron()