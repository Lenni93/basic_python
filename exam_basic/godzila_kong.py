budget = float(input())
number_statis = int(input())
price_per_a_statistic = float(input())
discount = 0
total = 0
decor = budget * 0.10
sum_clothes = number_statis * price_per_a_statistic
if number_statis >= 150:
    sum_clothes -= (0.10 * sum_clothes)


total_money = sum_clothes + decor
diff = abs(budget - total_money)
if budget >= total_money:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
