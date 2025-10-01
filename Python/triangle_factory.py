my_list = []

a = int(input())
my_list.append(a)

b = int(input())
my_list.append(b)

c = int(input())
my_list.append(c)

my_list.sort()

highest_num = my_list[-1]

if highest_num < 90:
    print('Spetsig Triangel')
elif highest_num == 90:
    print('Ratvinklig Triangel')
else:
    print('Trubbig Triangel')



