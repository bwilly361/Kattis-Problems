n, k = list(map(int, input().split()))

my_list = list(map(int, input().split()))

list_counter = 1

if my_list and k == my_list[0]:
    print("fyrst")
elif len(my_list) > 1 and k == my_list[1]:
    print("naestfyrst")
else:
    for index, value in enumerate(my_list):
        if value == k:
            print(str(index+1) + " fyrst")
            break

