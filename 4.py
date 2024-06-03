min_value=100*100
max_value=999*999
palindromes=[]

for i in range(min_value,max_value):
    if str(i)==str(i)[::-1]:
        palindromes.append(i)

result=[]
for i in palindromes:
    for j in range(100,1000):
     if i%j==0 and len(str(int(i/j)))==3:
        result.append(i)
print(max(result))
