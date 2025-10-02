vowels = ['a', 'e', 'i', 'o', 'u']
vowels_y = ['a', 'e', 'i', 'o', 'u', 'y']
vowel_count = 0
vowel_count_y = 0
my_string = input().lower()

my_string_list = list(my_string)

for x in my_string_list:
    if x in vowels:
        vowel_count += 1
    
for x in my_string_list:
    if x in vowels_y:
        vowel_count_y += 1

print(str(vowel_count) + ' ' + str(vowel_count_y))