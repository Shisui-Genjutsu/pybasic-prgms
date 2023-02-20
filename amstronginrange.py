a = int(input("enter startinge number: "))
y = int(input("enter ending number: "))
for i in range(a,y+1):
    temp = a
    n=0
    while a>0:
            n = n + 1
            a = a//10
    a = temp
    amst =0
    while a> 0:
        r = a%10
        c = r**n
        amst = amst + c
        a = a//10
    a = temp
    if a == amst:
        print("amstrong number",a)
    else:
        print("not an amstrong number",a)
    a = a + 1
