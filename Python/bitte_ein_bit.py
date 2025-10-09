import random

def bitte():
    num = int(input())
    num_list = [int(digit) for digit in str(num)]
    random_bit = random.choice(num_list)
    print(random_bit)

if __name__ == '__main__':
    bitte()