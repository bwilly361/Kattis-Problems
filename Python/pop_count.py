def pop_count():
    kernal_count = 0
    kernals = input()
    kernals_list = list(kernals)

    for i in kernals_list:
        if i == '1':
            kernal_count += 1
        else:
            continue

    print(kernal_count)

if __name__ == '__main__':
    pop_count()