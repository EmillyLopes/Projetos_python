a1,b1,c1 = input().split()
a=float(a1)
b=float(b1)
c=float(c1)
delta= (b**2)-4*a*c
if delta <= 0 or a == 0:
    print("Impossivel calcular")
else:
    R1 = (-b + delta ** (1 / 2)) / (2 * a)
    R2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1,R2))