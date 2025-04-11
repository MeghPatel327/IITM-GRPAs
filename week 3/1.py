# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n: # the terminal condition
        total += n # add n to the total
        n = int(input())  # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while 1 : # repeat forever since we are breaking inside
        line = input()
        if line == 'END' : # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price += quantity * price # accumulate the total price
    print(total_price)

elif task == "only_ed_or_ing":
    while 1 :
        line = input()
        if line == 'END' or line == 'STOP':
            break
        else:
            if line[-3:] == 'ing' or line[-2:] == 'ed':
                print(line)

elif task == "reverse_sum_palindrome":
    num1 = str(input())
    while num1 != '-1':
        sum = 0
        i=0
        num = str(int(num1) + int(num1[::-1]))
        if num == num[::-1]:
            print(num1)
        else:
            while i < len(num) :
                sum += int(num[i])
                i += 1
        num1 = str(input())

elif task == "double_string":
    line = input()
    while line != '':
        print(line*2)
        line = input()

elif task == "odd_char":
    out_string = ''
    line = input()
    while True:
        i = 0
        while i < len(line):
            if i % 2 == 0:
                out_string += line[i]
            i += 1
        out_string += " "
        if "." in line:
            break
        line = input()
    print(out_string)

elif task == "only_even_squares":
    num = input()
    while True:
        if str(num) == 'NAN':
            break
        else:
            num = int(num)
        if num % 2 == 0:
            print(num*num)
        num = input()

elif task == "only_odd_lines":
    lines = []
    i = 1
    while 1:
        line = input()
        if line == 'END':
            break
        if i % 2 == 1:
            lines.append(line)
        i+=1
    print("\n".join(lines[::-1]))