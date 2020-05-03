import random

k = random.sample(range(100),5)

for i in range(1,10):
    if i%2==0:
        print(i,end=' ')

if len(k) == 5:
    print("meow")