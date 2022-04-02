#include <stdio.h>

int main() {

int a,b,c;
float prob;
//total number of integers from 1 to 25 = 25

//probability of event = number of favourable outcomes/number of total outcomes

//number of odd numbers from 1 to 25 = a
//number of integers divisible by 2 and 3 in 1 to 25 = b
//number of integers less than 16

a=13;
b=4;
c=15;

//probability of odd numbers
prob=a/(float)25;
printf("%f\n",prob);

//probability of b
prob=b/(float)25;
printf("%f\n",prob);

//probability of c
prob=c/(float)25;
printf("%f\n",prob);

return 0;
}



