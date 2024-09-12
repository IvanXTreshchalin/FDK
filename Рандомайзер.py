from random import random
n=random ()*900+100
n=int(n)
print ( " Выберите число ", n )
a=n%10
b=n%100//10
c=n//100
print ( " Эти цифры ", c, ",", b, ",", a )
