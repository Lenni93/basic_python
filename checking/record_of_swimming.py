import math
record_of_second = float(input())
distance_of_meter = float(input())
time_of_second = float(input())

Time = (distance_of_meter * time_of_second)
daily = math.floor(distance_of_meter / 15)
daily = daily * 12.5

Record_time = Time + daily

diff = abs(Record_time - record_of_second)

if Record_time >= record_of_second:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {Record_time:.2f} seconds.")


