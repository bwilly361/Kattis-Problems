import re

def phd():
    counter = int(input())

    for i in range(counter):
        problem = input()
        if problem == 'P=NP':
            print('skipped')
        else:
            numbers = re.findall('(\d+)', problem)
            num_int = list(map(int, numbers))
            sum = 0
            for i in range(len(num_int)):
                sum += num_int[i]
            print(sum)              


if __name__ == '__main__':
    phd()