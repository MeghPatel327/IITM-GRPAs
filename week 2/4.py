# If the operation name is not any of the above print "Invalid Operation".

def odd_num_check():
    number = int(input(""))
    return "yes" if number % 2 != 0 else "no"

def perfect_square_check():
    number = int(input(""))
    return "yes" if number ** 0.5 == int(number ** 0.5) else "no"

def vowel_check():
    text = input("").lower()
    return "yes" if "a" in text or "e" in text or "i" in text or "o" in text or "u" in text else "no"

def divisibility_check():
    number = int(input(""))
    if number%2 == 0 and number%3 == 0:
        return "divisible by 2 and 3"
    return "divisible by 2" if number % 2 == 0 else "divisible by 3" if number % 3 == 0 else "divisible by 2 and 3" if number % 6 == 0 else "not divisible by 2 and 3"

def palindrominator():
    text = input("")
    return text + text[-2::-1]

def simple_interest():
    principal_amount = int(input(""))
    n_years = int(input(""))

    if n_years < 10:
        return round(principal_amount * 0.05 * n_years)
    else:
        return round(principal_amount * 0.08 * n_years)

name = input()

if name == "odd_num_check":
    print(odd_num_check())
elif name == "perfect_square_check":
    print(perfect_square_check())
elif name == "vowel_check":
    print(vowel_check())
elif name == "divisibility_check":
    print(divisibility_check())
elif name == "palindrominator":
    print(palindrominator())
elif name == "simple_interest":
    print(simple_interest())
else:
    print("Invalid Operation")