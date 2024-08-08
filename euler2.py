# Problem: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Date: 07/08/2024

l=[1,2]
sum=0

while sum<4000000:
    sum=l[-1]+l[-2]
    l.append(sum)

result=0

for i in l:
    if i%2==0:
        result+=i

print(result)
