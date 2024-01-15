Budget = float(input())
amount_static = int(input())
price_a_clothes = float(input())
decor_price = Budget * 0.1
discount_clothes = amount_static * price_a_clothes
if amount_static >= 150:
    discount_clothes = (discount_clothes * 0.90)

discountSum = discount_clothes + decor_price

diff = abs(Budget - discountSum)

if Budget >= discount_clothes:
    print("Action!")
    print(f'''Wingard starts filming with {diff:.2f} leva left.''')
else:
    print("Not enough money!")
    print(f'''Wingard needs {diff:.2f} leva more.''')
