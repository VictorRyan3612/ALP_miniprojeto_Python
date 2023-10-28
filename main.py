### Alunos 
# Artur Morais Candeia
# Victor Ryan Galvão Silva


#importações
from Funcoes import Funcoes_Menus
from Funcoes import Funcoes_Orcamento
from Funcoes import Funcoes_Despesa
from Funcoes import Funcoes_Dividas
from os import system
import pickle

######################################
########## Programa principal ##########
######################################


Funcoes_Menus.informacoes()
input('Aperte ENTER\n')


## Carregando no arquivo
# try:
#   arq_divida = open("divida.dat", "rb")
#   dividas_dicionario = pickle.load(arq_divida)
#   arq_divida.close()
# except:
#   arq_divida = open("divida.dat", "wb")
#   arq_divida.close()
#   dividas_dicionario = {}


menu = ''
while menu != '0':
  system('clear')
  
  Funcoes_Menus.menu_Principal()
  menu = input("Escolha sua opção:\n")

  
# Menu orçamento
  if menu == '1':
    Funcoes_Orcamento.modulo_orcamento()

# Menu despesa
  elif menu == '2':
    Funcoes_Despesa.modulo_despesa()

# Menu dívida
  elif menu == '3':
    Funcoes_Dividas.modulo_divida()

## Salvando no arquivo


print('Fim do programa')