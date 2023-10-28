from Funcoes import Funcoes_Menus
from os import system
import pickle



############## despesas
## Funções

# Cadastrar
def despesa_cadastrar():
  global despesas_dicionario
  
  mes = input('As despesas são de qual mês?\n')
  Q_despesas = int(input(f'Quantas despesas você quer cadastrar?\n'))
  
  matriz = []
  if mes not in despesas_dicionario:
    for i in range(1, Q_despesas + 1):
      despesa = []
      print('\n')
      nomeDespesa = input(f'Nome da despesa {i}:\n')
      valor = int(input(f'Quanto é o valor de {nomedespesa}?\n'))
  
    
      despesa += [nomeDespesa,valor]
      matriz += [despesa]
  else:
    print('\n')
    for i in range(1, Q_despesas + 1):
      despesa = []
      nomedespesa = input(f'Nome da despesa {i}:\n')
      valor = int(input(f'Quanto é o valor de {nomedespesa}?\n'))
      
    with open('despesa.dat', 'rb') as arq_despesa:
      despesas_dicionario = pickle.load(arq_despesa)
    
  
    matriz += despesas_dicionario[mes]
    despesa += [nomedespesa,valor]
    matriz.extend([despesa])
    
  
    
  despesas_dicionario [mes] = matriz
  
  with open('despesa.dat', 'wb') as arq_despesa:
    pickle.dump(despesas_dicionario, arq_despesa)
    
  input('Tecle ENTER para continuar!')
''''''

# Salvar
def despesa_salvar():
  with open('despesa.dat', 'wb') as arq_despesa:
    pickle.dump(despesas_dicionario, arq_despesa)
''''''

# Vizualizar
def despesa_vizualizar():
  print('Todas as despesas:\n')
  try:
    with open('despesa.dat', 'rb') as arq_despesa:
      despesas_dicionario = pickle.load(arq_despesa) 
      
      for mes in despesas_dicionario:
        print(f'{mes}: = {despesas_dicionario[mes]}')
  except:
    print('Não há despesas registradas')
		
  print('\n')
  input('Aperte ENTER para continuar\n')
''''''

### Pesquisar
def despesa_pesquisar():
  print('Pesquisa')
  print('\n')
  mes = input('Digite o mês buscar:\n')

  try:
    achou = False
    if mes in despesas_dicionario:
      achou = True
      
      print('\n')
      print('Mês:\t',mes)
      print('Conta:\t',despesas_dicionario[mes][0][0])
      print('Valor:\t', despesas_dicionario[mes][0][1])
      print('\n')
      
    else:
      achou = False
    if achou == False:
      print('Mês não encontrado')
  except:
    print('Mês não encontrado')
  input('Aperte ENTER para continuar\n')
''''''

# Editar
def despesa_editar():
  print('\n')
  despesa_vizualizar()
  mes = input('Mês da conta que deseja alterar:\n')
  print('\n')

  try:
    achou = False
    if mes in despesas_dicionario:
      achou = True
      
      nomedespesa = input('Novo nome da conta:\n')
      valor = input('Novo valor da conta:\n')
      despesas_dicionario[mes] = [nomedespesa, valor]
      print('Conta alterado com sucesso...')
      despesa_salvar()
    
    else:
      achou = False
    print()
    if achou == False:
      print('Mês não encontrado')
  except:
    print('Mês não encontrado')
  input('Aperte ENTER para continuar\n')
''''''

# Excluir
def despesa_excluir():
  print('\n')
  despesa_vizualizar()
  mes = input('Nome da conta a excluir:\n')
  
  try:
    achou = False
    if mes in despesas_dicionario:
      achou = True
    
      del despesas_dicionario[mes]
      print('Mês excluído com sucesso...')
      despesa_salvar()
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
  arq_despesa = open('despesa.dat', 'rb')
  despesas_dicionario = pickle.load(arq_despesa)
  arq_despesa.close()
except:
  arq_despesa = open('despesa.dat', 'wb')
  arq_despesa.close()
  despesas_dicionario = {}




def modulo_despesa():
  system('clear')
  operacao = ''
  while operacao != '0':
    Funcoes_Menus.menu_Despesas()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      despesa_cadastrar()
      system('clear')

    elif operacao == '2':
      despesa_vizualizar()
      system('clear')

    elif operacao == '3':
      despesa_pesquisar()
      system('clear')

    elif operacao == '4':
      despesa_editar()
      system('clear')
      
    elif operacao == '5':
      despesa_excluir()
      system('clear')
    elif operacao == '0':
      system('clear')
    else:
      system('clear')
      print('Digite uma operação válida!')