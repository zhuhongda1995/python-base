import random

xmax = 100
ymax = 100

x = 0
y = 0

p = float(input("what is the p"))
color = 1
for i in range(100):
    if color is 1:
        x = x + 1

        a = random.random()

        if a < p:
            color = 2
        else:
            color = 1

        print(x, y, color)