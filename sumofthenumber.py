"""n = int(input("enter the number: "))
sum =0
temp = n
while n>0:
    r = n%10
    sum = sum + r
    n = n//10

print(sum)"""
n = [int (d) for d in input("enter the number: ")]
sum = 0
for i in range(0,len(n)):
    sum = sum + n[i]
print(sum)


