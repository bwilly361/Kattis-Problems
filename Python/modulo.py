def modulo():
    unique_nums = []
    for _ in range(10):
        num = int(input())
        modular = num % 42
        #print('modulo: ' + str(modular))
        if modular not in unique_nums:
            unique_nums.append(modular)

    #print(unique_nums)
    print(len(unique_nums))

if __name__ == '__main__':
    modulo()