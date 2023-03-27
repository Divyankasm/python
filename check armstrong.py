sum=0
d=0
n=0
t=0
c=0
j=int(input("LENGTH OF NUMBER"))
n=int(input("INPUT A NUMBER TO CHECK WHETHER IT IS ARMSTRONG OR NOT"))
t=n
while n!=0:
    d=n%10
    c=d**j
    sum=sum+c
    n=n//10
    
if sum==t:
         print(t,"IS AN ARMSTRONG NUMBER")
else:
         print(t,"IS NOT AN ARMSTRONG NUMBER")



