price_tshirt = float(input())
needed_money = float(input())

price_shorts = price_tshirt * 0.75
price_socks = price_shorts * 0.20
price_boots = (price_shorts + price_tshirt) * 2
total_price = price_tshirt + price_shorts + price_socks + price_boots
sum_percent = total_price * 0.85
diff = abs(sum_percent - needed_money)
if sum_percent >= needed_money:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_percent:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
