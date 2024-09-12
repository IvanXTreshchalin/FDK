def F(n):
    if n<=1:
        return 1
    else:
        if n%2==1:
            return 4*n+F(n-1)-F(2)
        elif n%2==0:
            return 3*F(n-1)
print(F(35))

print('Иван Трещалин пидорас ')
        
