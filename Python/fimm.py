def fimm():
    year = int(input())

    if year >= 2021:
        years_since = (year + 1) - 2021
        inflation = years_since * 100
        price = inflation + 1000
    else:
        price = 1000

    print(price)


if __name__ == '__main__':
    fimm()