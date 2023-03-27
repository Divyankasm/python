a=0
t=0
sum=0
a=int(input("ENTER A NUMBER"))
while a!=0:
    t=a%10
    sum=t+sum
    a=a//10
print("SUM OF THE DIGITS OF THE NUMBER IS",sum)             
