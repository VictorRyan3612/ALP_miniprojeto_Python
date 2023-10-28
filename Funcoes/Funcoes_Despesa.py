from Funcoes import Funcoes_Menus
from os import system
############ Despesa
def despesa_cadastrar():
  print()

def despesa_vizualizar():
  print()

def despesa_pesquisar():
  print()
def modulo_despesa():
  system('clear')
  operacao = ''
  while operacao != '0':
    Funcoes_Menus.menu_Despesas()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      despesa_cadastrar()
        

    elif operacao == '2':
      despesa_vizualizar()


    elif operacao == '3':
      despesa_pesquisar()
      
    elif operacao == '0':
      system('clear')
      print()
