n=int(input("ENTER NUMBER TO WHICH FABONICCI SERIES IS TO BE PRINTED"))
x=0
y=1
z=0
while z<=n:
    print(z)
    x=y
    y=z
    z=x+y
