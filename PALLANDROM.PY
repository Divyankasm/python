n=0
t=0
rev=0
d=0
n=int(input("ENTER ANY NUMBER"))
t=n
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
if rev==t:
    print("IT IS PALLANDROM")
else:
    print("IT IS NOT PALLANDROM")
    