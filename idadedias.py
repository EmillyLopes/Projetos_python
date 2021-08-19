x= int(input())
a= x / 365
m= (x % 365)/30
d= (x % 365) % 30
print("{:.0f} ano(s)\n{:.0f} mes(es)\n{:.0f} dia(s)".format(int(a,m,d)))