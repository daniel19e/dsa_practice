import math
while True:
    hours = int(input("Enter hours"))
    minutes = int(input("Enter minutes"))
    if hours > 0 or minutes > 0 or minutes < 60:
        break
    else:
        print('wrong input')

charge=0

total_time = (hours*60+minutes)-30

while total_time>=1440:
    charge+=12
    total_time -= 1440

twenty_mins = math.ceil(total_time / 20)

if total_time > 240:
    charge += 12
else:
    charge += twenty_mins

print(charge)