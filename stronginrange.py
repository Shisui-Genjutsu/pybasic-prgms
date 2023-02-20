#n = int(input("enter the number: "))
y = int(input("enter the starting number: "))
x = int(input("enter the ending number: "))


def isStrong(n):
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
        return True
    #else :
        #return False
        
    
def strongNumbers(x):
    for i in range(y,x+1):
        if (isStrong(i)):
            print("\nstrong number: ",i, end='')
        else:
            print("\nnot a strong number: ",i, end='')

    
strongNumbers(x)
