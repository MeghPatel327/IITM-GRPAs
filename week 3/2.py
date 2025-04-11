# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    for i in range(1,n+1):
        result*=i
        i+=1
    print(result)
elif task == 'even_numbers':
    n = int(input())
    for i in range(0,n+1,2):
        print(i)
        i+=2

elif task == 'power_sequence':
    n = int(input())
    result = 1
    for i in range(1,n+1):
        print(result)
        result*=2
        i+=1

elif task == 'sum_not_divisible':
    n = int(input())
    sum = 0
    for i in range(n):
        if i%4 != 0 and i%5 != 0:
            sum+=i
    print(sum)

elif task == 'from_k':
    n = int(input())
    k = int(input())
    count = 0
    for num in range(k, 0, -1):
        if count >= n:
            break
        if '5' not in str(num) and '9' not in str(num) and num % 2 != 0:
            print(str(num)[::-1])
            count += 1

elif task == 'string_iter':
    s = input()
    for i in range(0,len(s)):
        if i != 0:
            print(int(s[i]) * int(s[i-1]))
        else:
            print(s[i])

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for  i in lst:
        print(f"{i} - type: {type(i)}")
else:
    print("Invalid")