#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the 10 001st prime number? 
import math
def is_prime(number):
    if number%2==0:
        return False
    for i in range(2,int(math.sqrt(number)+1)):
        if number%i==0:
         return False
    return True

n=2
count=1
while count<10001:
    n=n+1
    if is_prime(n):
        count+=1
print(n)