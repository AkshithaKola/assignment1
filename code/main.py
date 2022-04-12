import numpy as np
x=np.random.uniform(1,26,1000)
y=np.floor(x)
z=np.unique(y)
n=len(z)
#z is the array of outcomes

#probability of getting odd number
count=0
for i in range(0,n):
    if z[i]%2==1:
        count=count+1

print(count/25)

#probability of getting number divisible by both 2 and 3
count=0
for i in range(0,n):
    if z[i]%6==0:
        count=count+1

print(count/25)

#probability of getting number less than 16
count=0
for i in range(0,n):
    if z[i]<16:
        count=count+1

print(count/25)        

