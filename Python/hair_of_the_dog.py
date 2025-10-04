x = int(input())
schedule = []
hangover_count = 0

for i in range(x):
    day = input()
    schedule.append(day)

for i in range(len(schedule) - 1):
    if schedule[i] == 'drunk' and schedule[i + 1] == 'sober':
        hangover_count += 1

print(hangover_count)
        