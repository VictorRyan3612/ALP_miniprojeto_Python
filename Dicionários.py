# Criação de dicionário
computador = {'CPU': [['Intel', 'grafics'], ['AMD', 'ryzen']], 'RAM': '8gb', 'SSD': '250bg'}

# aparecer na tela
for chave in computador.keys():
  print(f'Chave = {chave} e Valor = {computador[chave]}')



print('\n\n')


# copia o dicionário para backup
computador_backup1 = computador.copy() 

### Apagar
apagar = input('O que deseja apagar?\n')
print('\n\n')
del computador[apagar]



# copia o dicionário para backup
computador_backup2 = computador_backup1.copy()

## Editar
editar_chave = input('Qual quer editar?\n')
editar_valor = input('O que deseja editar?\n')
computador[editar_chave] = editar_valor


#versão original
print ('versão original')
for chave in computador.keys():
  print(f'Chave = {chave} e Valor = {computador[chave]}')
print('\n\n\n')

# Versão com arquivo deletado
print('Versão com arquivo deletado')
for chave in computador.keys():
  print(f'Chave = {chave} e Valor = {computador_backup1[chave]}')
print('\n\n\n')


# Versão com arquivo deletado e
for chave in computador.keys():
  print(f'Chave = {chave} e Valor = {computador_backup2[chave]}')