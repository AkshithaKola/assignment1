# z is the number of favourable outcomes
# a,b,c are variables to count odd numbers, numbers divisible by two and three, numbers less than 16

#probability of odd numbers
z=0
for a in range(0,26):
 if a%2==1:
  z=z+1

# probability of numbers divisible by both 2 and 3 
print(z/25)
z=0
for b in range(1,26):
 if b%6==0:
  z=z+1

# probability of numbers less than 16 
print(z/25)
z=0
for c in range(1,26):
 if c<16:
  z=z+1


print(z/25)
