#Alunos 
# Artur Morais Candeia
# Victor Ryan Galvão Silva


#importações
from os import system
import pickle




############################# Funções

''''''
################### Menus #####################

def menu_Principal():
    print('''
      ==============================
      Programa Controle de Financias
      ==============================
      1 - Módulo Orçamento
      2 - Módulo Despesas
      3 - Módulo Dívidas 
      0 - Encerrar
  ''')

def menu_Orcamento():
    print('''
    ==============================
          Módulo Orçamento
    ==============================
    1 - Cadastrar Orçamento
    2 - Exibir Lista de Orçamentos
    3 - Procurar Orçamento
    0 - Sair
  ''')


def menu_Despesas():
    print('''
    ==============================
          Módulo Despesas
    ==============================
    1 - Cadastrar Despesa
    2 - Exibir Lista de Despesas
    3 - Procurar Despesas
    0 - Sair
  ''')



def menu_Dividas():
    print('''
    ==============================
          Módulo Dívidas
    ==============================
    1 - Cadastrar Dívida
    2 - Exibir Lista de Dívidas
    3 - Procurar Dívida
    0 - Sair
  ''')
''''''

################ Funções dos módulos #############

############# Orcamento
def orcamento_cadastrar():
  print()

def orcamento_vizualizar():
  print()

def orcamento_pesquisar():
  print()

def modulo_orcamento():
  system('clear')
  operacao = ''
  while operacao != '0':
    menu_Orcamento()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')
## Cadastrar orcamento
    if operacao == '1':
      orcamento_cadastrar()
        
  # Vizualizar as orcamento
    elif operacao == '2':
      orcamento_vizualizar()

# Pesquisar orcamento
    elif operacao == '3':
      orcamento_pesquisar()
      
    elif operacao == '0':
      system('clear')
      print()

  
''''''
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
    menu_Despesas()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')
## Cadastrar despesa
    if operacao == '1':
      despesa_cadastrar()
        
  # Vizualizar as dividas
    elif operacao == '2':
      despesa_vizualizar()

# Pesquisar despesa
    elif operacao == '3':
      despesa_pesquisar()
      
    elif operacao == '0':
      system('clear')
      print()

''''''
############## Dividas
def divida_cadastrar():
  dividas_dicionario = {}
  dividas_principal = []
  divida = []
  Q_dividas = int(input(f'Quantas dividas você quer cadastrar?\n'))
  mes = input('As dividas são de qual mês?\n')
  for i in range(1, Q_dividas + 1):
    divida = []
    print('\n')
    nomeDivida = input(f'Nome da dívida {i}:\n')
    valor = int(input(f'Quanto é o valor de {nomeDivida}?\n'))
    divida.append(nomeDivida)
    divida.append(valor)
    dividas_principal.append(divida)
    dividas_dicionario [mes] = dividas_principal

  with open('divida.txt', 'a') as dividatxt:
    arquivo = mes + ': ' + str(dividas_principal) + '\n'
    dividatxt.write(arquivo)


### Vizualizar
def divida_vizualizar():
  print('Módulo de relatório\n')
  try:
    with open('divida.txt', 'r') as dividatxt:
      # print(dividatxt.read())
      for i in [dividatxt]:
        for j in i:
          print(j)
  except:
    system('clear')
    print('Arquivo ainda não existe')
### Pesquisar
def divida_pesquisar():
  print('Pesquisa')
  divida_busca = input('Digite o nome buscar:\n')
  achou = False
  for x in x:
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

## Divida principal
def modulo_divida():
  system('clear')
  operacao = ''
  while operacao != '0':
    menu_Dividas()
    operacao = input('Selecione o que quer fazer:\n')
    print('\n')

    if operacao == '1':
      divida_cadastrar()
        

    elif operacao == '2':
      divida_vizualizar()


    elif operacao == '3':
      divida_pesquisar()
      
    elif operacao == '0':
      system('clear')
      print()

''''''

####################################
############# Programa principal
#####################################


menu = ''
while menu != '0':
  menu_Principal()
  menu = input("Escolha sua opção:\n")

  
# Menu orçamento
  if menu == '1':
    modulo_orcamento()

# Menu despesa
  elif menu == '2':
    modulo_despesa()

# Menu dívida
  elif menu == '3':
    
    modulo_divida()
  
    

#   elif menu =='0':
#     print('Fim do programa\n')
#   menu = input('escolha outra opção\n')
# print('Fim do programa')

# debito = int(input('Quanto dinheiro você tem?\n'))
# qcontas = int(input('Quantas despesas você tem mensalmmente?\n'))

# contas = []

# for i in range(1,qcontas+1):
#   nomeconta = input(f'Nome despesa {i}\n')
#   contas = int(input(f'Quanto é o valor de {nomeconta}?\n'))