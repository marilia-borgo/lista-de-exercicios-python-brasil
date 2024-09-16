"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    if data == "" or "/" not in data:
         print("'Data inválida'")
    else:

       
        dia, mes, ano = map(int, data.split('/'))
        if mes < 1 or mes > 12 or ano <= 0:
            print("'Data inválida'")
        else:
      
            if mes in (1, 3, 5, 7, 8, 10, 12):
                ultimo_dia = 31

            elif mes == 2:
                if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                    ultimo_dia = 29
                else:
                    ultimo_dia = 28
            else:
                ultimo_dia = 30
            if dia < 1 or dia > ultimo_dia:
                print("'Data inválida'")

            else:
                print("'Data válida'")
