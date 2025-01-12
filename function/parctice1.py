cities=["Dhaka","Sylhet","Gazipur","barisal"]
heros=["Ibna Hiasam","Battani","Omor khoiyam"]


def print_len(iteam):
    print(len(iteam))
    
    
def print_list(iteam):
    for i in iteam:
        print(i,end=" ")
    print()
def fac( i):
    if i<=1:
        return i
    return i*fac(i-1)

def cal_fact(i):
    fact=1
    for j in range(1,i+1):
        fact*=j
    print(fact) 

def usd_inr(i):
    print (i," USD =",i*83,"INR")


print_len(cities)
print_list(cities)
print_len(heros)
print_list(heros)

val=fac(5)
print(val)
cal_fact(10)
usd_inr(54)
