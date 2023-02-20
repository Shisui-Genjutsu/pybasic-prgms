n = int(input("enter the number: "))
fact =1
stnum =0
temp =n
for j in range(0,len(str(n))):
    fact =1
    r = n%10
    for i in range(1,r+1):
        fact = fact * i
    stnum = stnum + fact
    n = n//10
    #print(fact)
n = temp
if n == stnum:
    print("\nstrong number", stnum)
else :
    print("\nnot a strong number", stnum)