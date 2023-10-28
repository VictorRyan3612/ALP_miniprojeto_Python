from Funcoes import Funcoes_Menus
from os import system
import pickle
############## Dividas

def divida_cadastrar():
  # dividas_dicionario = {}
  # dividas_principal = []
  # divida = []
  Q_dividas = int(input(f'Quantas dividas você quer cadastrar?\n'))
  
  mes = input('As dividas são de qual mês?\n')
  for i in range(1, Q_dividas + 1):
    # divida = []
    print('\n')
    nomeDivida = input(f'Nome da dívida {i}:\n')
    valor = int(input(f'Quanto é o valor de {nomeDivida}?\n'))
    
    # divida.append(nomeDivida)
    # divida.append(valor)
    # dividas_principal.append(divida)
    # dividas_dicionario [mes] = dividas_principal
    dividas_dicionario [mes] = [nomeDivida,valor]
#Escrever
  # with open('divida.dat', 'ab') as arq_divida:
  #   arquivo = str(dividas_dicionario) + '\n'
  #   pickle.dump(arquivo, arq_divida)
  #   #arq_divida.write(arquivo)
  #   # pickle.dump(dividas_dicionario, arq_divida)
  # input('\nAperte ENTER para continuar\n')


### Vizualizar
def divida_vizualizar():
  print('Módulo de relatório\n')
  
  try: #Exibir de arquivo
    with open('divida.dat', 'rb') as arq_divida:
      print(pickle.load(arq_divida))
      
      
  except:
    system('clear')
    print('Arquivo ainda não existe')
  print('\n\n\n')
  input('Aperte ENTER para continuar\n')


### Pesquisar
'''
def divida_pesquisar():
  print('Pesquisa')
  divida_busca = input('Digite o nome buscar:\n')
  achou = False
  for divida_busca in :
      if divida_busca.upper() in pessoa[0].upper():
        achou = True
        print()
        print("Mês:\t", pessoa[0])
        print("Conta:\t", pessoa[1])
        print("Valor:\t", pessoa[2])
        print()
      if not achou:
        print("Nome não encontrado!")
      print()
'''
## Divida principal
def divida_editar():
  print()
def divida_excluir():
  print()
def modulo_divida():
  system('clear')
  operacao = ''
  while operacao != '0':
    Funcoes_Menus.menu_Dividas()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      divida_cadastrar()
      system('clear')

    elif operacao == '2':
      divida_vizualizar()
      system('clear')

    elif operacao == '3':
      divida_pesquisar()

    elif operacao == '4':
      divida_editar()

    elif operacao == '5':
      divida_excluir()
    
    elif operacao == '0':
      system('clear')
