from Funcoes import Funcoes_Menus
from os import system
import pickle

meses = ('Janeiro','Fevereiro','Março', 'Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro',1,2,3,4,5,6,7,8,9,10,11,12)

############## Orcamentos
##### Funções

# Validação de numero ↓
def validacao_numero(num1):
  while num1.isdecimal() == False:
    num1 = input(f'Digite um número válido!\n')
  num1 = int(num1)
  return num1
''''''

# Validação de Mes
def validacao_mes():
  global meses
  mes = input('Os orçamentos são de qual mês?\n').capitalize()

  if mes.isdecimal() == True:
    mes = int(mes)
    if (mes >= 1) and (mes <= 12):
      mes = meses[mes-1]
      
  while mes not in meses:
    mes = input('Digite um mês válido!\n')
    if mes.isdecimal() == True:
      mes = int(mes)
      if (mes >= 1) and (mes <= 12):
        mes = meses[mes-1]
      else:
        mes = input(f'Digite um mês válido!\n').capitalize()
  return mes
''''''

# Salvar
def orcamento_salvar():
  with open('orcamento.dat', 'wb') as arq_orcamento:
    pickle.dump(orcamentos_dicionario, arq_orcamento)
''''''

# Cadastrar
def orcamento_cadastrar():
  global orcamentos_dicionario
  mes = validacao_mes()
      
  Q_orcamentos = input(f'Quantos orçamentos você quer cadastrar?\n')
  Q_orcamentos = validacao_numero(Q_orcamentos)
    
  matriz = []


  
   # mes ainda não existe no dicionário ↓
  if mes not in orcamentos_dicionario:
    for i in range(1, Q_orcamentos + 1):
      orcamento = []
      print('\n')

      
      nome_Orcamento = input(f'Nome do orçamento {i}:\n')

        
      # Validação de valor
      valor = input(f'Quanto é o valor de {nome_Orcamento}?\n')
      valor = validacao_numero(valor)

      
    
      orcamento += [nome_Orcamento,valor]
      matriz += [orcamento]

      
    # mes já existe no dicionário ↓
  else:
    print('\n')
    for i in range(1, Q_orcamentos + 1):
      orcamento = []
      nome_Orcamento = input(f'Nome do orçamento {i}:\n')
      valor = input(f'Quanto é o valor de {nome_Orcamento}?\n')
      valor = validacao_numero(valor)
      
  
    matriz += orcamentos_dicionario[mes]
    orcamento += [nome_Orcamento,valor]
    matriz.extend([orcamento])
    
  orcamentos_dicionario [mes] = matriz
  
  orcamento_salvar()
    
  input('Tecle ENTER para continuar!')
''''''

# Vizualizar
def orcamento_vizualizar():
  global orcamentos_dicionario
  try:
    print('Todas os orçamentos:\n')

    for mes in orcamentos_dicionario.keys():
      print(f'{mes}:\t{orcamentos_dicionario[mes]}')
  except:
    print('Não há orçamentos registrados')
		
  print('\n')
''''''

# Pesquisar
def orcamento_pesquisar():
  global orcamentos_dicionario
  print('Pesquisa')
  print('\n')
  mes = validacao_mes()
  
  if mes in orcamentos_dicionario:
  
    print('\n')
    print('Mês:\t',mes)
    print('Orçamento:\t',orcamentos_dicionario[mes][0])
    print('Valor:\t', orcamentos_dicionario[mes][1])
    print('\n')
  
  else:
    print('Mês não encontrato!')
  
  input('Aperte ENTER para continuar\n')
''''''

# Editar
def orcamento_editar():
  global orcamentos_dicionario
  print('\n')
  orcamento_vizualizar()
  mes = validacao_mes()

  
  if mes in orcamentos_dicionario:
    matriz = orcamentos_dicionario[mes]
    print(f'No mes {mes} tem essas orcamentos:\n{orcamentos_dicionario[mes]}')
    print('\n')
    
    q_qual_orcamento = input('Quantas deseja alterar?\n')
    q_qual_orcamento = validacao_numero(q_qual_orcamento)
    
    for i in range (1,q_qual_orcamento+1):
      editar = []
      qual_orcamento = input('Qual deseja alterar?\n')
      qual_orcamento = validacao_numero(qual_orcamento)
      qual_orcamento -= 1
      matriz.pop(qual_orcamento)        
      
      nome_Orcamento = input('Novo nome do orçamento:\n')
      
      valor = input('Novo valor do orçamento:\n')
      valor = validacao_numero(valor)
      
      editar = [nome_Orcamento, valor]
      matriz.insert(qual_orcamento,editar)
      
    orcamentos_dicionario[mes] = matriz
    orcamento_salvar()

    print('Conta alterada com sucesso...')
    
  else:
    print('Mês não encontrato!')
  input('Tecle ENTER para continuar!')
''''''  

# Excluir
def orcamento_excluir():
  global orcamentos_dicionario
  print('\n')
  orcamento_vizualizar()
  mes = validacao_mes()
  
  try:
    if mes in orcamentos_dicionario:
    
      del orcamentos_dicionario[mes]
      print('Mês excluído com sucesso...')
      orcamento_salvar()
      
    else:
      print('Mês não encontrado!')
  except:
    print('Ocorreu algum problema')
    
  input('Tecle ENTER para continuar!')

''''''

##############################
##### Programa Principal #####
##############################


try:
  arq_orcamento = open('orcamento.dat', 'rb')
  orcamentos_dicionario = pickle.load(arq_orcamento)
  arq_orcamento.close()
except:
  arq_orcamento = open('orcamento.dat', 'wb')
  arq_orcamento.close()
  orcamentos_dicionario = {}




def modulo_orcamento():
  system('clear')
  operacao = ''
  while operacao != '0':
    Funcoes_Menus.menu_Orcamentos()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      orcamento_cadastrar()
      system('clear')

    elif operacao == '2':
      orcamento_vizualizar()
      input('Aperte ENTER para continuar\n')
      system('clear')

    elif operacao == '3':
      orcamento_pesquisar()
      system('clear')

    elif operacao == '4':
      orcamento_editar()
      system('clear')
      
    elif operacao == '5':
      orcamento_excluir()
      system('clear')
    elif operacao == '0':
      system('clear')
    else:
      system('clear')
      print('Digite uma operação válida!')
