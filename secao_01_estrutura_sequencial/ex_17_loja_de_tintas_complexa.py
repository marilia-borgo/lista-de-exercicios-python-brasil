"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 18 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.7 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 3.3 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 3.3 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.3 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.9 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.9 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    import math

    m2 = float(input('informe a quantidade de METRO QUADRADO (m²) a ser pintado: '))
    consumo_litro = m2 / 6
    print("Você deve comprar", "%.0f" % consumo_litro,"litros de tinta.")
    qtd_latas18 = consumo_litro / 18
    qtd_latas36 = consumo_litro / 3.6
    print('a quantidade de GALOES de 18 LITROS a ser usado é: {}'.format(math.ceil(qtd_latas18)))
    print('a quantidade de LATAS de 3,6 LITROS a ser usado é: {}\n'.format(math.ceil(qtd_latas36)))
    valor_total18 = math.ceil(qtd_latas18) * 80
    valor_total36 = math.ceil(qtd_latas36) * 25
    print('o valor total em GALOES de 18 LITROS é: R${}'.format(valor_total18))
    print('o valor total em LATAS de 3,6 LITROS é: R$ {}\n'.format(valor_total36))
    print('considerando o menor desperdíciode tinta, temos: \n')

    qtd_latas_mistas18 = ((consumo_litro * 0.10) + consumo_litro) / 18
    qtd_litros18 = math.trunc(qtd_latas_mistas18) * 18
    resto18 = ((consumo_litro * 0.10) + consumo_litro) - qtd_litros18
    qtd_latas_mistas36 = resto18 / 3.6
    qtd_latas_mistas_total = math.trunc(qtd_latas_mistas18) + math.ceil(qtd_latas_mistas36)
    valor_misto18 = math.trunc(qtd_latas_mistas18) * 80
    valor_misto36 = math.ceil(qtd_latas_mistas36) * 25
    total_misto = valor_misto18 + valor_misto36

    print('quantidade de latas de 18 litros: {}'.format(math.trunc(qtd_latas_mistas18)))
    print('qtd latas de 3,6: {}'.format(math.ceil(qtd_latas_mistas36)))
    print('qtd latas mistas: {}'.format(qtd_latas_mistas_total))
    print('\no valor total considerando GALOES e LATAS é (acresentando 10% de quebra): R$ {}'.format(total_misto))