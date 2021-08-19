a1,b1,c1= input().split()
a= int(a1)
b= int(b1)
c= int(c1)
MAB= (a+b+abs(a-b))/2
MAC= (MAB+c+abs(MAB-c))/2
if MAB  > c:
    print ("{} eh o maior".format(int(MAB)))
else:
    print ("{} eh o maior".format(int(MAC)))