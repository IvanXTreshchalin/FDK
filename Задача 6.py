for i in range (1,10000):
    x=i
    a=0
    b=0
    while x>0:
        a=a+1
        b=b+(9-x%10)
        x=x//10
    if a==3 and b==9:
        print(i)
