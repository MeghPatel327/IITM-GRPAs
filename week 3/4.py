# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None 
all = None
min = None 

task = input()



if task == 'factors':
    n = int(input().strip())
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    for factor in factors:
        print(factor)
elif task == 'find_min':
    n = int(input().strip())
    numbers = []
    for _ in range(n):
        numbers.append(int(input().strip()))
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    print(minimum)
elif task == 'prime_check':
    n = int(input().strip())
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    print(is_prime)
elif task == 'is_sorted':
    s = input().strip()
    sorted_order = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            sorted_order = False
            break
    print(sorted_order)
elif task == 'any_true':
    n = int(input().strip())
    any_divisible_by_3 = False
    for _ in range(n):
        number = int(input().strip())
        if number % 3 == 0:
            any_divisible_by_3 = True
            break
    print(any_divisible_by_3)
elif task == 'manhattan':
    x, y = 0, 0
    while True:
        direction = input().strip()
        if direction == 'STOP':
            break
        elif direction == 'UP':
            y += 1
        elif direction == 'DOWN':
            y -= 1
        elif direction == 'LEFT':
            x -= 1
        elif direction == 'RIGHT':
            x += 1
    manhattan_distance = abs(x) + abs(y)
    print(manhattan_distance)
else:
    print("Invalid task")
