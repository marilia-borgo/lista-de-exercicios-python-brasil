"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investigar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
    """Escreva aqui em baixo a sua solução"""
    if telefonou=='Sim':
      telefonou_v=1
    else:
      telefonou_v=0

    if estava_no_local=='Sim':
      estava_no_local_v=1
    else:
      estava_no_local_v=0
      
    if mora_perto=='Sim':
      mora_perto_v=1
    else:
      mora_perto_v=0

    if devia=='Sim':
      devia_v=1
    else:
      devia_v=0

    if trabalhou=='Sim':
      trabalhou_v=1
    else:
      trabalhou_v=0
    
    soma_respostas = telefonou_v+estava_no_local_v+mora_perto_v+devia_v+trabalhou_v
    if soma_respostas < 2:
      print("'Inocente'")
    elif soma_respostas == 2:
      print("'Suspeito'")
    elif  soma_respostas==3 or soma_respostas==4:
      print("'Cúmplice'")
    elif soma_respostas == 5:
      print("'Assassino'")

    
    
