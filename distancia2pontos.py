x, y = input().split()
x1,y1= float(x), float(y)
px, py = input().split()
x2, y2 = float(px), float(py)
d=((x2-x1)**2 + (y2-y1)**2)**(1/2)
print("{:.4f}".format(d))