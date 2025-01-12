def sum_n(n):
    if(n==0):
        return 0
    return sum_n(n-1)+n 

print(sum_n(100))

def prnt(i,a):
    if(i==len(a)):
        return
    print(a[i])
    prnt(i+1,a)

a=["s","a","f","u"]

prnt(0,a)
