import numpy as np
x=np.random.randint(1,26,1000)
z=np.unique(x)
n=len(z)
#z is the array of outcomes

#probability of getting odd number
a=z%2
count=np.count_nonzero(a==1)
print(count/n)

#probability of getting number divisible by both 2 and 3
b=z%6
count=np.count_nonzero(b==0)
print(count/n)

#probability of getting number less than 16
count=np.count_nonzero(z<16)
print(count/n)           
