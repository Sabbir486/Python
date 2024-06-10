# Quiz solution---->

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 = int(time.strftime('%H'))
timestamp1 = int(input("Enter hour: "))
print(timestamp1)
# timestamp2 = int(time.strftime('%M'))
# print(timestamp2)
# timestamp3 = int(time.strftime('%S'))
# print(timestamp3)

if(timestamp1>5 and timestamp1<12):
    print("Good Morning")
elif(timestamp1>=12 and timestamp1<18):
    print("Good Noon")
elif(timestamp1>=18 and timestamp1<=24):
    print("Good Night")
else:
    print("Unknown Time")

