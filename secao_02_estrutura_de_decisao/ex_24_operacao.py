"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


from secao_02_estrutura_de_decisao.ex_02_positivo_ou_negativo import positivo_ou_negativo


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    if operacao == '+': 
      result=n_1+n_2
      if result%2 == 0:
        par_impar="par"
      else:
        par_impar="impar"
      if result>=0:
        positivo_negativo="positivo"
      else:
        positivo_negativo="negativo"

      if result//1 == result:
        decimal_inteiro="inteiro"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {par_impar}, {positivo_negativo} e {decimal_inteiro}.")
      else:
        decimal_inteiro="decimal"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {positivo_negativo} e {decimal_inteiro}.")
    elif operacao == '-': 
      result=n_1-n_2
      if result%2 == 0:
        par_impar="par"
      else:
        par_impar="impar"
      if result>=0:
        positivo_negativo="positivo"
      else:
        positivo_negativo="negativo"

      if result//1 == result:
        decimal_inteiro="inteiro"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {par_impar}, {positivo_negativo} e {decimal_inteiro}.")
      else:
        decimal_inteiro="decimal"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {positivo_negativo} e {decimal_inteiro}.")
    elif operacao == '*': 
      result=n_1*n_2
      if result%2 == 0:
        par_impar="par"
      else:
        par_impar="impar"
      
      if result>=0:
        positivo_negativo="positivo"
      else:
        positivo_negativo="negativo"
      if result == 0:
        positivo_negativo="neutro"
      if result//1 == result:
        decimal_inteiro="inteiro"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {par_impar}, {positivo_negativo} e {decimal_inteiro}.")
      else:
        decimal_inteiro="decimal"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {positivo_negativo} e {decimal_inteiro}.")
    elif operacao == '/': 
      result=n_1/n_2
      if result%2 == 0:
        par_impar="par"
      else:
        par_impar="impar"
      if result>=0:
        positivo_negativo="positivo"
      else:
        positivo_negativo="negativo"

      if result//1 == result:
        decimal_inteiro="inteiro"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {par_impar}, {positivo_negativo} e {decimal_inteiro}.")
      else:
        decimal_inteiro="decimal"
        print(f"Resultado: {result:.2f}")
        print(f"Número é {positivo_negativo} e {decimal_inteiro}.")






    