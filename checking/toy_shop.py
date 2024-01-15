price_trip = float(input())
amount_puzzle = int(input())
amount_Talking_dolls = int(input())
amount_teddy_baer = float(input())
amount_minion = float(input())
amount_trucks = float(input())

Total = ((amount_puzzle * 2.60) + (amount_Talking_dolls * 3) + (amount_teddy_baer * 4.10) + (amount_minion * 8.20) + (amount_trucks * 2))
amount_toy = amount_Talking_dolls + amount_minion + amount_trucks + amount_puzzle + amount_teddy_baer
if amount_toy >= 50:
    Total = Total - (Total * 0.25)

Total = Total - (Total * 0.10)

diff = abs(Total - price_trip)
if Total >= price_trip:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")


