budget = float(input())
number_night = float(input())
price_per_night = float(input())
percent_extra_expenses = int(input())
total_amount = percent_extra_expenses / 100 * budget
discount = 1
if number_night > 7:
    discount = 0.95

total_night = (price_per_night * number_night) * discount + total_amount

diff = abs(budget - total_night)
if total_night <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")

