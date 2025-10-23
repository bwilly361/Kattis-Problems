def job_expenses():
    n = int(input())

    budget = list(map(int, input().split()))

    total = 0

    for price in budget:
        #print(price)
        if price < 0:
            price = abs(price)
            #print(price)
            total += price

    print(total)

if __name__ == '__main__':
    job_expenses()