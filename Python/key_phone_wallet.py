def keyphonewallet():
    my_stuff = []
    required_things = ['keys', 'phone', 'wallet']

    count = int(input())
    required_things_found = 3

    for i in range(count):
        thing = input()
        my_stuff.append(thing)

    for item in required_things:
        if item not in my_stuff:
            print(item)
            required_things_found -= 1

    if required_things_found == 3:
        print('ready')

if __name__ == "__main__":
    keyphonewallet()