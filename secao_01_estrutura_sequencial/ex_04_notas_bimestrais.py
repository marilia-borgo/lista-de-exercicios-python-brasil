"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():

    """Escreva aqui em baixo a sua solução"""

    nota1 = int (input('digite a primeira nota'))
    nota2 = int (input('digite a segunda nota'))
    nota3 = int (input('digite a terceira nota'))
    nota4 = int (input('digite a quarta nota'))

    media = (nota1+nota2+nota3+nota4)/4

    print (f'A média anual é {media}')


