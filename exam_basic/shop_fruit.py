price_strawberry = float(input())
quantity_banana = float(input())
quantity_orange = float(input())
quantity_raspberry = float(input())
quantity_strawberry = float(input())

price_raspberry = price_strawberry / 2
price_orange = price_raspberry - (price_raspberry * 0.4)
price_banana = price_raspberry - (0.80 * price_raspberry)
sum_raspberry = quantity_raspberry * price_raspberry
sum_orange = quantity_orange * price_orange
sum_banana = quantity_banana * price_banana
sum_strawberry = quantity_strawberry * price_strawberry
total_sum = (sum_strawberry + sum_banana + sum_raspberry + sum_orange)
print(f'{total_sum:.2f}')

