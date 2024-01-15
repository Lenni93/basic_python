import math
name_serial = input()
continue_serial = int(input())
continue_break = int(input())
time_break = continue_break / 8
time_rest = continue_break / 4

final_time = continue_break - time_rest - time_break

diff = abs(final_time - continue_serial)
rounded_diff = math.ceil(diff)
if final_time > continue_serial:
    print(f"You have enough time to watch {name_serial} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {rounded_diff} more minutes.")
