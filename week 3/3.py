task = input()


if task == 'permutation':
    s = input().strip()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j: # Ensure no repetition of characters
                print(s[i] + s[j])
elif task == 'sorted_permutation':
    s = input().strip()
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] <= s[j]: # Ensure no repetition and print only if sorted
                print(s[i] + s[j])
elif task == 'repeat_the_repeat':
    n = int(input())
    for _ in range(n):
        print("".join(map(str, range(1, n + 1))))
elif task == 'repeat_incrementally':
    n = int(input())
    for i in range(1, n + 1):
        print("".join(map(str, range(1, i + 1))))
elif task == 'increment_and_decrement':
    n = int(input())
    for i in range(1, n + 1):
        line = "".join(map(str, range(1, i + 1)))
        line += line[-2::-1] # reverse the line excluding the last character
        print(line)
else:
    print("Invalid task")