# Quiz---> Good Morning

import time
timestamp = time.strftime('%H:%M:%S')

print(timestamp)
timestamp = int(time.strftime('%H'))

print(timestamp)
timestamp = int(time.strftime('%M'))

print(timestamp)
timestamp = int(time.strftime('%S'))

if(timestamp>1 and timestamp<5):
    print("Good Morning")
elif(timestamp>=5 and timestamp<12):
    print("Good Afternoon")
else:
    print("Good Night")

