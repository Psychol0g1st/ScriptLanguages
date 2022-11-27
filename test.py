from random import seed
from random import random
import random

coin1 = []
coin2 = []
coin3 = []
counter = 0
for i in range(100_000_000):
    coin1.append(random.randrange(2))
    coin2.append(random.randrange(2))
    coin3.append(random.randrange(2))
    if(coin1[i] or coin2[i] or coin3[i]):
        counter += 1 
print(100_000_000/counter)