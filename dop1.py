def to_ten(a):
    b=len(a)
    c=int(a)
    sum=0
    while c>0:
        k=c%10
        s=(2**b)*k
        b-=1
        sum+=s
        c=c//10
    return sum
a=input()
print(to_ten(a))