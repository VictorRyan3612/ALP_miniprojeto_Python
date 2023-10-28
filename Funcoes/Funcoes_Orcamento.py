from Funcoes import Funcoes_Menus
from os import system
############## Orcamento
def orcamento_cadastrar():
  print()

def orcamento_vizualizar():
  print()

def orcamento_pesquisar():
  print()

def modulo_orcamento():
  system('clear')
  operacao = ''
  while operacao != '0':
    Funcoes_Menus.menu_Orcamento()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      orcamento_cadastrar()
        

    elif operacao == '2':
      orcamento_vizualizar()


    elif operacao == '3':
      orcamento_pesquisar()
      
    elif operacao == '0':
      system('clear')
      print()

  