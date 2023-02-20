x = int(input("enter start number: "))
y = int(input("enter end number: "))
div = 0
i =1
for x in range(x,y+1):
   
    for i in range(i,x+1):
        if(x%i == 0):
            div+=1
            
    if (div==2):
        print("\n",x,"prime number\n", end = '')
    else:
        div = 0
        i =1
        print("\n",x,"not a prime")

    