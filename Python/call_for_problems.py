def call_for_problems():
    n = int(input())
    problems = []

    for i in range(n):
        problem = int(input())
        problems.append(problem)

    candiate_problems = 0

    for i in problems:
        if i % 2 == 0:
            continue
        else:
            candiate_problems += 1

    print(candiate_problems)

if __name__ == "__main__":
    call_for_problems()