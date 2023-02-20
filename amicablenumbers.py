x = int(input("enter the 1st number: "))
y = int(input("enter the 2nd number: "))
sum  =0
sumot= 0
for i in range(1,x):
    if(x%i == 0):
        sum += i
for j in range(1,y):
    if(y%j == 0):
        sumot += j
if (x == sumot) & (y == sum):
    print("\namicable numbers: ",x," ",y)
else:
    print("\nnot a amicable numbers: ",x," ",y)
