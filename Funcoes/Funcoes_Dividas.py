from Funcoes import Funcoes_Menus
from os import system
import pickle



############## Dividas
## Funções

def divida_cadastrar():
  global dividas_dicionario
  
  mes = input('As dividas são de qual mês?\n')
  Q_dividas = int(input(f'Quantas dividas você quer cadastrar?\n'))
  
  matriz = []
  
  for i in range(1, Q_dividas + 1):
    divida = []
    print('\n')
    nomeDivida = input(f'Nome da dívida {i}:\n')
    valor = int(input(f'Quanto é o valor de {nomeDivida}?\n'))

  
    divida += [nomeDivida,valor]
    matriz += [divida]
  dividas_dicionario [mes] = matriz

  
  arq_divida = open("divida.bin", "wb")
  pickle.dump(dividas_dicionario, arq_divida)
  arq_divida.close()
  

### Vizualizar
def divida_vizualizar():
  print('Módulo de relatório\n')
  
  arq_divida = open("divida.bin", "rb")
  arquivo2 = pickle.load(arq_divida)
  arq_divida.close()
  print(arquivo2)

  with:
    
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

##############################
##### Programa Principal #####
##############################

try:
  arq_divida = open("divida.bin", "rb")
  dividas_dicionario = pickle.load(arq_divida)
  arq_divida.close()
except:
  arq_divida = open("divida.bin", "wb")
  arq_divida.close()
  dividas_dicionario = {}



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

## Salvando em arquivo
# arq_divida = open("divida.bin", "ab")
# pickle.dump(dividas_dicionario, arq_divida)
# arq_divida.close()