import math

days = int(input())
first_day_km = float(input())
final = 0
total_km = first_day_km
total = 0
first = 0
name = 0
for num in range(days):
    increase_percentage = int(input())
    first = total_km
    total_km += first * (increase_percentage / 100)
    total += total_km
name = first_day_km + total
difference = abs(name - 1000)
if name >= 1000:
    print(f"You've done a great job running {math.ceil(difference)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(difference)} more kilometers")