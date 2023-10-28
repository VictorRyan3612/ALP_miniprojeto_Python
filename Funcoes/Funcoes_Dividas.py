from Funcoes import Funcoes_Menus
from os import system
import pickle

meses = ('Janeiro','Fevereiro','Março', 'Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro',1,2,3,4,5,6,7,8,9,10,11,12)

############## Dividas
##### Funções

# Validação de numero ↓
def validacao_numero(num1):
  while num1.isdecimal() == False:
    num1 = input(f'Digite um numero válido!\n')
  num1 = int(num1)
  return num1
''''''

# Validação de Mes
def validacao_mes():
  global meses
  mes = input('As dividas são de qual mês?\n').capitalize()

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
def divida_salvar():
  with open('divida.dat', 'wb') as arq_divida:
    pickle.dump(dividas_dicionario, arq_divida)
''''''

# Carregar
def divida_carregar():
  with open('divida.dat', 'rb') as arq_divida:
    dividas_dicionario = pickle.load(arq_divida)
''''''

# Cadastrar
def divida_cadastrar():
  global dividas_dicionario
  mes = validacao_mes()
      
  Q_dividas = input(f'Quantas dividas você quer cadastrar?\n')
  Q_dividas = validacao_numero(Q_dividas)
    
  matriz = []


  
   # mes ainda não existe no dicionário ↓
  if mes not in dividas_dicionario:
    for i in range(1, Q_dividas + 1):
      divida = []
      print('\n')

      
      nomeDivida = input(f'Nome da dívida {i}:\n')

        
      # Validação de valor
      valor = input(f'Quanto é o valor de {nomeDivida}?\n')
      valor = validacao_numero(valor)

      
    
      divida += [nomeDivida,valor]
      matriz += [divida]

      
    # mes já existe no dicionário ↓
  else:
    print('\n')
    for i in range(1, Q_dividas + 1):
      divida = []
      nomeDivida = input(f'Nome da dívida {i}:\n')
      valor = input(f'Quanto é o valor de {nomeDivida}?\n')
      valor = validacao_numero(valor)
      
    divida_carregar()
  
    matriz += dividas_dicionario[mes]
    divida += [nomeDivida,valor]
    matriz.extend([divida])
    
  dividas_dicionario [mes] = matriz
  
  divida_salvar()
    
  input('Tecle ENTER para continuar!')
''''''

# Vizualizar
def divida_vizualizar():
  try:
    print('Todas as dívidas:\n')
    divida_carregar()
    for mes in dividas_dicionario.keys():
      print(f'{mes}:\t{dividas_dicionario[mes]}')
  except:
    print('Não há dívidas registradas')
		
  print('\n')
''''''

# Pesquisar
def divida_pesquisar():
  print('Pesquisa')
  print('\n')
  mes = validacao_mes()
  
  if mes in dividas_dicionario:
  
    print('\n')
    print('Mês:\t',mes)
    print('Conta:\t',dividas_dicionario[mes][0])
    print('Valor:\t', dividas_dicionario[mes][1])
    print('\n')
  
  else:
    print('Mês não encontrato!')
  
  input('Aperte ENTER para continuar\n')
''''''

# Editar
def divida_editar():
  print('\n')
  divida_vizualizar()
  mes = validacao_mes()

  divida_carregar()
  matriz = dividas_dicionario[mes]
  
  if mes in dividas_dicionario:
    #print(f'No mes {mes} tem essas dividas:\n{dividas_dicionario[mes]}')
    
    q_qual_divida = input('Quantas deseja alterar?\n')
    q_qual_divida = validacao_numero(q_qual_divida)
    
    for i in range (1,q_qual_divida+1):
      editar = []
      qual_divida = input('Qual deseja alterar?\n')
      qual_divida = validacao_numero(qual_divida)
      qual_divida -= 1
      matriz.pop(qual_divida)        
      
      nomeDivida = input('Novo nome da conta:\n')
      
      valor = input('Novo valor da conta:\n')
      valor = validacao_numero(valor)
      
      editar = [nomeDivida, valor]
      matriz.insert(qual_divida,editar)
      
    dividas_dicionario[mes] = matriz
    divida_salvar()

    print('Conta alterada com sucesso...')
    
  else:
    print('Mês não encontrato!')
  input('Tecle ENTER para continuar!')
''''''  

# Excluir
def divida_excluir():
  print('\n')
  divida_vizualizar()
  mes = validacao_mes()
  
  try:
    if mes in dividas_dicionario:
    
      del dividas_dicionario[mes]
      print('Mês excluído com sucesso...')
      divida_salvar()
      
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
      input('Aperte ENTER para continuar\n')
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
