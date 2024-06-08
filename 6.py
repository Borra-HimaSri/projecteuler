#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum=0
for i in range(101):
 sum=sum+i
sum_square=sum*sum
print("square of sum of 100 numbers:",sum_square)

temp=0
for i in range(101):
  i=i*i
  temp=temp+i
print("sum of square of 100 numbers:",temp)
print("differencebetween the sum of the squares of the first one hundred natural numbers and the square of the sum is ",sum_square-temp)
