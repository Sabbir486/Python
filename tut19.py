# Break and Continue---->

for i in range (12):
    if(i == 10):
        break
    print("5 X", i, "=", 5 * (i))
    
print('Skip the loop\n')


for i in range (12):
    if(i == 5):
        print('Skip the iteration')
        continue
    print("5 X", i, "=", 5 * (i))
    

