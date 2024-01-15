budget_movie = float(input())
destination = input()
season = input()
amount_days = int(input())
price = 0
percent = 0
if season == "Winter":
    if destination == "Dubai":
        price = 45000 * amount_days
    elif destination == "Sofia":
        price = 17000 * amount_days
    elif destination == "London":
        price = 24000 * amount_days

if season == "Summer":
    if destination == "Dubai":
        price = 40000 * amount_days
    elif destination == "Sofia":
        price = 12500 * amount_days
    elif destination == "London":
        price = 20250 * amount_days

if destination == 'Sofia':
    price += (price * 0.25)
if destination == 'Dubai':
    price -= (price * 0.30)

diff = abs(budget_movie - price)

if budget_movie > price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
