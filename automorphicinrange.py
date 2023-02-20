def automorphic(n):
    square = n * n
    while(n>0):
        if(n%10!=square%10):
            return 0
            n = n//10
            square = square//10
        else:
            return 1
def checkap():
    num = int(input("enter the starting number: "))
    endnum = int(input("enter the ending number: "))
    for i in range(num,endnum+1):
        if(automorphic(i)):
            print("\nautomorphic number",i)
        else:
            print("\nnot a automorphic number",i)
checkap()