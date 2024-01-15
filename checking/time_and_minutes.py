hours = int(input())
minutes = int(input())
totalTime = (hours * 60) + minutes + 15
outHours = totalTime // 60
outMinutes = totalTime % 60
if outHours > 23:
    outHours = 0
print(f"{outHours}:{outMinutes:02}")
# // how many times is deviding from 60 as example 120 // 60 = 2 times
# from % after 60 how many left
# // how many minutes in total
# % 60 minutes and ... seconds