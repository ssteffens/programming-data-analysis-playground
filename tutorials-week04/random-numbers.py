# https://www.geeksforgeeks.org/random-seed-in-python/

import random

for i in range(5):
    random.seed(20)

    print(random.randint(1, 1000))

print("\n")


random.seed(3)
print(random.randint(1, 1000))

random.seed(3)
print(random.randint(1, 1000))

print(random.randint(1, 1000))
print(random.randint(1, 1000))