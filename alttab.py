# WAP for ALT+ TAB
n1 =[1,2,3,4]
n2=3
#o/P=>[3,1,2,4]

index=n2-1
temp =n1[n2-1]

while(index>0):
    n1[index]=n1[index-1]
    index =index-1
n1[0]=temp

print(n1)