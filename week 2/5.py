main_dish = input()
time_of_day = int(input())
has_voucher = False if input() == "False" else True
is_card_payment = False if input() == "False" else True

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else:
    print("Invalid main dish")
    exit() 

total_cost = cost

if time_of_day >= 12 and time_of_day <= 15:
    total_cost = total_cost * (1 - 0.15)

if has_voucher:
    total_cost = total_cost * (1 - 0.1)

if is_card_payment:
    total_cost = total_cost * (1 + 0.05)

print(f"{total_cost:.02f}")