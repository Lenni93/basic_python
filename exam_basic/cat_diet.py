fats = int(input())
proteins = int(input())
carbs = int(input())
total_calories = int(input())
water = int(input())


fatsGR = ((fats / 100) * 2500) / 9

proteinGR = ((proteins / 100) * 2500) / 4

carbGR = ((carbs / 100) * 2500) / 4


weight = fatsGR + proteinGR + carbGR

weightPerGr = 2500 / weight


oneGR = weightPerGr * (1 - water / 100)
print(f"{oneGR:.4f}")

