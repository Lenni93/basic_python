Budget = float(input())
amount_video_card = int(input())
amount_processor = int(input())
amount_ram_memory = int(input())

n = amount_video_card * 250
m = amount_processor * (n * 0.35)
p = amount_ram_memory * (n * 0.10)

total = n + p + m
if amount_video_card > amount_processor:
    total = total * 0.85

diff = abs(Budget - total)
if Budget >= total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

