lst=[]
n=a=d=0
print("ENTER LENGTH OF LIST")
d=int(input())
print("ENTER ",d ,"NUMBER")
for x in range(0,d):
    n=int(input())
    lst.append(n)
a=int(input("ENTER ANY NUMBER TO COUNT ITS OCCURRENCE"))
print("IT OCCURS",lst.count(a),"TIMES")