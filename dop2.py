def binary(n):
    res= ""
    while n>0:
        remainder=n%2
        n=n//2
        res+=str(remainder)
        
a=binary(5)
print(a)