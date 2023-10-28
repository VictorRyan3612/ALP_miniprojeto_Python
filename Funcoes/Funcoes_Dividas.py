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
  if mes not in dividas_dicionario:
    for i in range(1, Q_dividas + 1):
      divida = []
      print('\n')
      nomeDivida = input(f'Nome da dívida {i}:\n')
      valor = int(input(f'Quanto é o valor de {nomeDivida}?\n'))
  
    
      divida += [nomeDivida,valor]
      matriz += [divida]
  else:
    print('\n')
    for i in range(1, Q_dividas + 1):
      divida = []
      nomeDivida = input(f'Nome da dívida {i}:\n')
      valor = int(input(f'Quanto é o valor de {nomeDivida}?\n'))
      
    with open('divida.dat', 'rb') as arq_divida:
      dividas_dicionario = pickle.load(arq_divida)
    
  
    matriz += dividas_dicionario[mes]
    divida += [nomeDivida,valor]
    matriz.extend([divida])
    
  
    
  dividas_dicionario [mes] = matriz
  
  with open('divida.dat', 'wb') as arq_divida:
    pickle.dump(dividas_dicionario, arq_divida)
    
  input('Tecle ENTER para continuar!')


def divida_salvar():
  with open('divida.dat', 'wb') as arq_divida:
    pickle.dump(dividas_dicionario, arq_divida)

def divida_vizualizar():
  print('Todas as dívidas:\n')

  with open('divida.dat', 'rb') as arq_divida:
    dividas_dicionario = pickle.load(arq_divida) 
    
    for mes in dividas_dicionario.keys():
      print(f'{mes}: = {dividas_dicionario[mes]}')

		
  print('\n')
  input('Aperte ENTER para continuar\n')


### Pesquisar
  
def divida_pesquisar():
  print('Pesquisa')
  print('\n')
  mes = input('Digite o mês buscar:\n')
  
  achou = False
  while achou == False:
    if mes in dividas_dicionario:
      achou = True
      
      print('\n')
      print('Mês:\t',mes)
      print('Conta:\t',dividas_dicionario[mes][0][0])
      print('Valor:\t', dividas_dicionario[mes][0][1])
      print('\n')
      
    if not achou:
      print('Mês não encontrado!')
    print()
  input('Aperte ENTER para continuar\n')
  
def divida_editar():
  print('\n')
  divida_vizualizar()
  mes = input('Mês da conta que deseja alterar:\n')
  print('\n')
  achou = False
  while achou == False:
    if mes in dividas_dicionario:
      achou = True
      nomeDivida = input('Novo nome da conta:\n')
      valor = input('Novo valor da conta:\n')
      dividas_dicionario[mes] = [nomeDivida, valor]
      print('Conta alterado com sucesso...')
      divida_salvar()
      
    else:
      print('Mês não encontrato!')
  input('Tecle ENTER para continuar!')
  

def divida_excluir():
  print('\n')
  divida_vizualizar()
  mes = input('Nome da conta a excluir:\n')
  
  achou = False
  while achou == False:
    if mes in dividas_dicionario:
      achou = True
      
      del dividas_dicionario[mes]
      print('Mês excluído com sucesso...')
      divida_salvar()
    else:
      print('Mês não encontrado!')
    input('Tecle ENTER para continuar!')

''''''

##############################
##### Programa Principal #####
##############################
try:
  arq_divida = open('divida.dat', 'rb')
  dividas_dicionario = pickle.load(arq_divida)
  arq_divida.close()
except:
  arq_divida = open('divida.dat', 'wb')
  arq_divida.close()
  dividas_dicionario = {}



## Divida principal
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
      system('clear')

    elif operacao == '4':
      divida_editar()
      system('clear')
      
    elif operacao == '5':
      divida_excluir()
      system('clear')
    elif operacao == '0':
      system('clear')