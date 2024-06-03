
import math
n = 600851475143
list = []
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        flag = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            list.append(i)

max_factor = max(list)
print(max_factor)
