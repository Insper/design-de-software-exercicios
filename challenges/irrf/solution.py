salario_bruto = float(input('Digite seu salário bruto: '))
dependentes = int(input('Digite a quantidade de dependentes: '))

if salario_bruto <= 1045:
    contribuicao_inss = 0.075 * salario_bruto
elif salario_bruto <= 2089.60:
    contribuicao_inss = 0.09 * salario_bruto
elif salario_bruto <= 3134.40:
    contribuicao_inss = 0.12 * salario_bruto
elif salario_bruto <= 6101.06:
    contribuicao_inss = 0.14 * salario_bruto
else:
    contribuicao_inss = 671.12

base_de_calculo = salario_bruto - contribuicao_inss - dependentes * 189.59

if base_de_calculo <= 1903.98:
    aliquota = 0
    deducao = 0
elif base_de_calculo <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base_de_calculo <= 3751.05:
    aliquota = 0.15
    deducao = 354.8
elif base_de_calculo <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36

irrf = base_de_calculo * aliquota - deducao

print('Para o salário bruto de {0} e {1} dependentes, o IRRF é R$ {2:.2f}'.
      format(salario_bruto, dependentes, irrf))
