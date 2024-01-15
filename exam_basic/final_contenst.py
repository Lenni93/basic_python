dancers = int(input())
points = float(input())
season = input()
place = input()
rewards = 0
if place == "Bulgaria":
    rewards = dancers * points
    if season == "summer":
        rewards -= rewards * 0.05
    elif season == "winter":
        rewards -= rewards * 0.08
elif place == "Abroad":
    rewards = dancers * points + (dancers * points * 0.5)
    if season == "summer":
        rewards -= rewards * 0.1
    elif season == "winter":
        rewards -= rewards * 0.15

charity = rewards * 0.75
per_dancer = (rewards - charity) / dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {per_dancer:.2f}")