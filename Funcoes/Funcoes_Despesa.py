from Funcoes import Funcoes_Menus
from os import system
import pickle

meses = ('Janeiro','Fevereiro','Março', 'Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro',1,2,3,4,5,6,7,8,9,10,11,12)

############## Despesas
##### Funções

# Validação de numero ↓
def validacao_numero(num1):
  while num1.isdecimal() == False:
    num1 = input('Digite um número válido!\n')
  num1 = int(num1)
  return num1
''''''

# Validação de Mes
def validacao_mes():
  global meses
  mes = input('As despesas são de qual mês?\n').capitalize()

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
        mes = input('Digite um mês válido!\n').capitalize()
  return mes
''''''

# Salvar
def despesa_salvar():
  with open('despesa.dat', 'wb') as arq_despesa:
    pickle.dump(despesas_dicionario, arq_despesa)
''''''

# Cadastrar
def despesa_cadastrar():
  global despesas_dicionario
  mes = validacao_mes()
      
  Q_despesas = input(f'Quantas despesas você quer cadastrar?\n')
  Q_despesas = validacao_numero(Q_despesas)
    
  matriz = []


  
   # mes ainda não existe no dicionário ↓
  if mes not in despesas_dicionario:
    for i in range(1, Q_despesas + 1):
      despesa = []
      print('\n')

      
      nome_Despesa = input(f'Nome da despesa {i}:\n')

        
      # Validação de valor
      valor = input(f'Quanto é o valor de {nome_Despesa}?\n')
      valor = validacao_numero(valor)

      
    
      despesa += [nome_Despesa,valor]
      matriz += [despesa]

      
    # mes já existe no dicionário ↓
  else:
    print('\n')
    for i in range(1, Q_despesas + 1):
      despesa = []
      nome_Despesa = input(f'Nome da despesa {i}:\n')
      valor = input(f'Quanto é o valor de {nome_Despesa}?\n')
      valor = validacao_numero(valor)
      
  
    matriz += despesas_dicionario[mes]
    despesa += [nome_Despesa,valor]
    matriz.extend([despesa])
    
  despesas_dicionario [mes] = matriz
  
  despesa_salvar()
    
  input('Tecle ENTER para continuar!')
''''''

# Vizualizar
def despesa_vizualizar():
  global despesas_dicionario
  try:
    print('Todas as despesas:\n')

    for mes in despesas_dicionario.keys():
      print(f'{mes}:\t{despesas_dicionario[mes]}')
  except:
    print('Não há despesas registradas')
		
  print('\n')
''''''

# Pesquisar
def despesa_pesquisar():
  global despesas_dicionario
  print('Pesquisa')
  print('\n')
  mes = validacao_mes()
  
  if mes in despesas_dicionario:
  
    print('\n')
    print('Mês:\t',mes)
    print('Conta:\t',despesas_dicionario[mes][0])
    print('Valor:\t', despesas_dicionario[mes][1])
    print('\n')
  
  else:
    print('Mês não encontrato!')
  
  input('Aperte ENTER para continuar\n')
''''''

# Editar
def despesa_editar():
  global despesas_dicionario
  print('\n')
  despesa_vizualizar()
  mes = validacao_mes()


  
  
  if mes in despesas_dicionario:
    matriz = despesas_dicionario[mes]
    print(f'No mes {mes} tem essas despesas:\n{despesas_dicionario[mes]}')
    print('\n')
    
    q_qual_despesa = input('Quantas deseja alterar?\n')
    q_qual_despesa = validacao_numero(q_qual_despesa)
    
    for i in range (1,q_qual_despesa+1):
      editar = []
      
      qual_despesa = input('Qual deseja alterar?\n')
      qual_despesa = validacao_numero(qual_despesa)
      qual_despesa -= 1
      matriz.pop(qual_despesa)        
      
      nome_Despesa = input('Novo nome da despesa:\n')
      
      valor = input('Novo valor da despesa:\n')
      valor = validacao_numero(valor)
      
      editar = [nome_Despesa, valor]
      matriz.insert(qual_despesa,editar)
      
    despesas_dicionario[mes] = matriz
    despesa_salvar()

    print('Conta alterada com sucesso...')
    
  else:
    print('Mês não encontrato!')
  input('Tecle ENTER para continuar!')
''''''  

# Excluir
def despesa_excluir():
  global despesas_dicionario
  print('\n')
  despesa_vizualizar()
  mes = validacao_mes()
  
  try:
    if mes in despesas_dicionario:
    
      del despesas_dicionario[mes]
      print('Mês excluído com sucesso...')
      despesa_salvar()
      
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
      input('Aperte ENTER para continuar\n')
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
