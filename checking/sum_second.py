import math
first_run = int(input())
second_run = int(input())
third_run = int(input())
total = first_run + second_run + third_run
minutes = total // 60
seconds = total % 60
minutes = math.floor(minutes)
if seconds < 10:

   print(f'{minutes}:0{seconds}')
else:
   print(f'{minutes}:{seconds}')
