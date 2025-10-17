import math
n = 256
j = 1
while j <= math.log(n,2):
    print(j)
    j = j*2




n = 10
i = n
j = 2
while i > 0:
    while j < n:
        print(i + j)
        j *= 2
    i -= 1
