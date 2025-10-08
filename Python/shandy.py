def shandy():
    b = int(input())
    l = int(input())

    if b == 0 or l == 0:
        print(0)
    else:
        if b > l:
            small_num = l
        else:
            small_num = b
            
        shandies = small_num * 2
        print(shandies)

if __name__ == "__main__":
    shandy()