a1,b1,c1 = input().split()
a=float(a1)
b=float(b1)
c=float(c1)
#delta= (b**2)-4*a*c
x1 = (-b + (b**2)-4*a*c ** (1 / 2)) / (2 * a)
x2 = (-b - (b**2)-4*a*c ** (1 / 2)) / (2 * a)
if delta == 0 :
    #print ("o valor de a deve ser diferente de 0")
#elif delta <0:
    #print("sem raízes  reais")
#else:

print (x1, x2)