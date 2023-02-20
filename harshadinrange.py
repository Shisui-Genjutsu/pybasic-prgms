#n = int(input("enter the number"))
def harshad(n):
    sum  =0
    res = n
    while(n>0):
        r = n%10
        sum = sum + r
        n = n//10
    n =res
    har = n%sum
    if har == 0:
       return True
    else:
        return False
def checkhar():
    num = int(input("enter the strating number"))
    endnum = int(input("enter the strating number"))
    for i in range(num,endnum+1):
        if harshad(i):
            print("\nharshad number",i)
        else:
            print("\nnot aharshad number",i)
checkhar()

    
 