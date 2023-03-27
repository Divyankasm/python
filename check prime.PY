a=0
a=int(input("ENTER ANY NUMBER TO CHECK IT IS PRIME OR NOT"))
for x in range(2,a):
    if a%x==0:
        print("IT IS NOT PRIME") 
        break
else:
    print("IT IS  PRIME")
