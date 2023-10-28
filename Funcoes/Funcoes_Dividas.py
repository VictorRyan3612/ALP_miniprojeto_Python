from Funcoes import Funcoes_Menus
from os import system
import pickle

meses = ('Janeiro','Fevereiro','Março', 'Abril','Maio','Junho','Julho','Agosto','Setembro','outubro','novembro','dezembro',1,2,3,4,5,6,7,8,9,10,11,12)

############## Dividas
##### Funções

# Cadastrar
def divida_cadastrar():
  global dividas_dicionario
  global meses

  
  # Validação de mes
  mes = input('As dividas são de qual mês?\n')
  mes.capitalize()
  if mes.isnumeric() and (mes != '0'):
    mes = int(mes)
    mes = meses[mes-1]
    print('\n')
  while mes not in meses:
    mes = input(f'Digite um mês válido:\n').capitalize()
    if mes.isnumeric() and (mes != '0'):
      mes = int(mes)
      mes = meses[mes-1]
      print('\n')

      

  # Validação de Quantidade de dividas
  Q_dividas = input(f'Quantas dividas você quer cadastrar?\n')
  Q_dividas_B = Q_dividas.isnumeric()
  while Q_dividas_B == False:
    Q_dividas = input(f'Digite um numero válido:\n')
    Q_dividas_B = Q_dividas.isnumeric()
  Q_dividas = int(Q_dividas)
    
  matriz = []


  
   # mes ainda não existe no dicionário ↓
  if mes not in dividas_dicionario: # mes ainda não existe no dicionário
    for i in range(1, Q_dividas + 1):
      divida = []
      print('\n')

      
      nomeDivida = input(f'Nome da dívida {i}:\n')

        
      # Validação de valor
      valor = input(f'Quanto é o valor de {nomeDivida}?\n')
      valor_B = valor.isnumeric()
      while valor_B == False:
        valor = input(f'Digite um valor válido:\n')
        valor_B = valor.isnumeric()
      valor = int(valor)

      
    
      divida += [nomeDivida,valor]
      matriz += [divida]

      
    # mes já existe no dicionário ↓
  else:
    print('\n')
    for i in range(1, Q_dividas + 1):
      divida = []
      nomeDivida = input(f'Nome da dívida {i}:\n')


      valor = input(f'Quanto é o valor de {nomeDivida}?\n')
      valor_B = valor.isnumeric()
      while valor_B == False:
        valor = input(f'Digite um valor válido:\n')
        valor_B = valor.isnumeric()
      valor = int(valor)
      
    with open('divida.dat', 'rb') as arq_divida:
      dividas_dicionario = pickle.load(arq_divida)
    
  
    matriz += dividas_dicionario[mes]
    divida += [nomeDivida,valor]
    matriz.extend([divida])
    
  
    
  dividas_dicionario [mes] = matriz
  
  with open('divida.dat', 'wb') as arq_divida:
    pickle.dump(dividas_dicionario, arq_divida)
    
  input('Tecle ENTER para continuar!')
''''''

# Salvar
def divida_salvar():
  with open('divida.dat', 'wb') as arq_divida:
    pickle.dump(dividas_dicionario, arq_divida)

def divida_vizualizar():
  print('Todas as dívidas:\n')
  try:
    with open('divida.dat', 'rb') as arq_divida:
      dividas_dicionario = pickle.load(arq_divida) 
      
      for mes in dividas_dicionario.keys():
        print(f'{mes}: = {dividas_dicionario[mes]}')
  except:
    print('Não há dívidas registradas')
		
  print('\n')
  input('Aperte ENTER para continuar\n')
''''''

# Pesquisar
def divida_pesquisar():
  print('Pesquisa')
  print('\n')
  mes = input('Digite o mês buscar:\n')
  try:
    achou = False
    if mes in dividas_dicionario:
      achou = True
    
      print('\n')
      print('Mês:\t',mes)
      print('Conta:\t',dividas_dicionario[mes][0])
      print('Valor:\t', dividas_dicionario[mes][1])
      print('\n')
    
    else:
      achou = False
    if achou == False:
      print('Mês não encontrato!')
  except:
    print('Mês não encontrato!')
  
  input('Aperte ENTER para continuar\n')
''''''

# Editar
def divida_editar():
  print('\n')
  divida_vizualizar()
  mes = input('Mês da conta que deseja alterar:\n')
  print('\n')

  try:
    achou = False
    
    if mes in dividas_dicionario:
      achou = True
      
      nomeDivida = input('Novo nome da conta:\n')
      valor = input('Novo valor da conta:\n')
      dividas_dicionario[mes] = [nomeDivida, valor]
      print('Conta alterado com sucesso...')
      divida_salvar()
      
    else:
      achou = False
    if achou == False:
      print('Mês não encontrato!')
  except:
    print('Mês não encontrato!')
    
  input('Tecle ENTER para continuar!')
''''''  

# Excluir
def divida_excluir():
  print('\n')
  divida_vizualizar()
  mes = input('Nome do mes a excluir:\n')
  
  try:
    achou = False
    if mes in dividas_dicionario:
      achou = True
    
      del dividas_dicionario[mes]
      print('Mês excluído com sucesso...')
      divida_salvar()
    else:
      achou = False
    if achou == False:
      print('Mês não encontrado!')
  except:
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
    else:
      system('clear')
      print('Digite uma operação válida!')
      