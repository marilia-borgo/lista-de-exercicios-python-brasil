"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato ( 5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""


def calcular_assalto_no_salario():
     horas_trabalhadas = float (input('digite a quantidade de horas trabalhadas:'))
     preco_hora = float (input('digite o preço da hora:'))

     salario_bruto = horas_trabalhadas*preco_hora
     ir= salario_bruto * (11/100)
     inss=salario_bruto * (8/100)
     sind=salario_bruto * (5/100)
     salario_liquido= salario_bruto - ir - inss - sind

     print("+ Salário Bruto :", "%.2f" % salario_bruto)
     print("- IR (11%) : R$", "%.2f" % ir)
     print("- INSS (8%) : R$", "%.2f" % inss)
     print("- Sindicato ( 5%) : R$", "%.2f" % sind)
     print("= Salário Liquido : R$", "%.2f" % salario_liquido)
