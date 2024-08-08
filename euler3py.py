# Problem: Largest prime factor of 600851475143
# Date: 07/08/2024
#13195 5 7 13 29

a=108
l1=[]
l2=[]
for i in range(2,a):
    for c in range(1,i+1):
        if i%c==0:
            l2.append(c)
    if l2==[1,i] and a%i==0:
        l1.append(i)
    l2=[]

print("Largest prime factor of", a, "is", l1[-1])
