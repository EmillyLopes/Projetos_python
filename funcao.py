def calcular_pagamento (str_horas, str_hora):
  horas = float(str_horas)
  taxa = float(str_hora)
  if horas <= 40:
    salario = horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

str_horas= input('Digite as horas: ')
str_taxa=input('Digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa)
print('O valor de seus rendimentos é R$',total_salario)