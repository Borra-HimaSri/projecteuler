n = 4000000
a = 1
b = 2
total = 0
while b <= n:  
    if b % 2 == 0:
        total += b
    a, b = b, a + b
print(total)
