#n = int(input("enter the number"))
def abundant(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    if sum > n:
        return True
    else:
        return False
def checkabun():
    num = int(input("enter the starting number: "))
    endnum = int(input("enter the ending number:  "))
    for i in range(num,endnum+1):
        if abundant(i):
            print("\nabundant number: ",i)
        else:
            print("\nnot a abundant number: ",i)
checkabun()