### Alunos 
# Artur Morais Candeia
# Victor Ryan Galvão Silva


#importações
from Funcoes import Funcoes_Menus
from Funcoes import Funcoes_Orcamento
from Funcoes import Funcoes_Despesa
from Funcoes import Funcoes_Dividas
from os import system



# meses = ('Janeiro','Fevereiro','Março', 'Abril','Maio','Junho','Julho','Agosto','Setembro','outubro','novembro','dezembro',1,2,3,4,5,6,7,8,9,10,11,12)

######################################
########## Programa principal ########
######################################


Funcoes_Menus.informacoes()
input('Aperte ENTER\n')



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

print('\nFim do programa')