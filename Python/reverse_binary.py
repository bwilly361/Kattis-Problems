def reverse_binary():
    num = int(input())

    bin_num = format(num, 'b')

    bin_list = list(bin_num)

    bin_list.reverse()

    bin_list = ''.join(bin_list)

    new_int = int(bin_list, 2)

    print(new_int)

if __name__ == '__main__':
    reverse_binary()