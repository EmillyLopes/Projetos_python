A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
Atri = A * C / 2
Acir = 3.14159 * C ** 2
Atrap = (A + B) * C / 2
Aquad = B ** 2
Aret = A * B
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(Atri, Acir,
                                                                                                         Atrap, Aquad,
                                                                                                         Aret))
