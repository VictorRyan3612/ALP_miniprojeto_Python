from Funcoes import Funcoes_Menus
from os import system
import pickle



############## orcamentos
## Funções

#Cadastrar
def orcamento_cadastrar():
  global orcamentos_dicionario
  
  mes = input('Os orçamentos são de qual mês?\n')
  
  Q_orcamentos = int(input(f'Quantas orçamentos você quer cadastrar?\n'))
  
  
  matriz = []
  if mes not in orcamentos_dicionario:
    for i in range(1, Q_orcamentos + 1):
      orcamento = []
      print('\n')
      nomeOrcamento = input(f'Nome da orçamento {i}:\n')
      valor = int(input(f'Quanto é o valor de {nomeOrcamento}?\n'))
  
    
      orcamento += [nomeOrcamento,valor]
      matriz += [orcamento]
  else:
    print('\n')
    for i in range(1, Q_orcamentos + 1):
      orcamento = []
      nomeOrcamento = input(f'Nome da orçamento {i}:\n')
      valor = int(input(f'Quanto é o valor de {nomeOrcamento}?\n'))
      
    with open('orcamento.dat', 'rb') as arq_orcamento:
      orcamentos_dicionario = pickle.load(arq_orcamento)
    
  
    matriz += orcamentos_dicionario[mes]
    orcamento += [nomeOrcamento,valor]
    matriz.extend([orcamento])
    
  
    
  orcamentos_dicionario [mes] = matriz
  
  with open('orcamento.dat', 'wb') as arq_orcamento:
    pickle.dump(orcamentos_dicionario, arq_orcamento)
    
  input('Tecle ENTER para continuar!')
''''''

# Salvar
def orcamento_salvar():
  with open('orcamento.dat', 'wb') as arq_orcamento:
    pickle.dump(orcamentos_dicionario, arq_orcamento)
''''''
    
# Vizualizar
def orcamento_vizualizar():
  print('Todas as orçamentos:\n')
  try:
    with open('orcamento.dat', 'rb') as arq_orcamento:
      orcamentos_dicionario = pickle.load(arq_orcamento) 
      
      for mes in orcamentos_dicionario:
        print(f'{mes}: = {orcamentos_dicionario[mes]}')
  except:
    print('Não há orçamentos registrados')
		
  print('\n')
  input('Aperte ENTER para continuar\n')
''''''

# Pesquisar
def orcamento_pesquisar():
  print('Pesquisa')
  print('\n')
  mes = input('Digite o mês a buscar:\n')

  try:
    achou = False
    if mes in orcamentos_dicionario:
      achou = True
      
      print('\n')
      print('Mês:\t',mes)
      print('Conta:\t',orcamentos_dicionario[mes][0][0])
      print('Valor:\t', orcamentos_dicionario[mes][0][1])
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
def orcamento_editar():
  print('\n')
  orcamento_vizualizar()
  mes = input('Mês da conta que deseja alterar:\n')
  print('\n')

  with open('orcamento.dat', 'rb') as arq_orcamento:
    orcamentos_dicionario = pickle.load(arq_orcamento)
    
  try:
    achou = False
    if mes in orcamentos_dicionario:
      achou = True
     
      
        
      matriz = []
      for i in orcamentos_dicionario[mes]:
        orcamento = []
        nomeOrcamento = input('Novo nome do orçamento:\n')
        valor = input('Novo valor da orçamento:\n')

  
        orcamento += [nomeOrcamento,valor]
        matriz += [orcamento]
      orcamentos_dicionario [mes] = matriz

      with open('orcamento.dat', 'wb') as arq_orcamento:
        pickle.dump(orcamentos_dicionario, arq_orcamento)
      print('Orçamento alterado com sucesso...')
      orcamento_salvar()
    
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
def orcamento_excluir():
  print('\n')
  orcamento_vizualizar()
  mes = input('Mês do orçamento a excluir:\n')
  
  try:
    achou = False
    if mes in orcamentos_dicionario:
      achou = True
    
      del orcamentos_dicionario[mes]
      print('Mês excluído com sucesso...')
      orcamento_salvar()
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
    Funcoes_Menus.menu_Orcamento()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      orcamento_cadastrar()
      system('clear')

    elif operacao == '2':
      orcamento_vizualizar()
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