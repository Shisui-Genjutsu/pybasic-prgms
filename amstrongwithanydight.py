a = [int(a) for a in input("enter the number: ")]
temp  = a
amst = 0
n =len(a)
for i in range(n):
    amst = amst + (a[i])**n
temp = [str(temp) for temp in temp]
temp = int(''.join(temp))
a = temp
if a == amst:
    print("amstrong number")
else:
    print("not an amstrong number")

