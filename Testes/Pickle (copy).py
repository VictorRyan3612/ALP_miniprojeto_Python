##coisas para adicionar no programa


##########################
### Programa Principal ###
##########################


### Recuperando os dados do arquivo
## Repetir pela quantidade de arquivos
try:
  with open('divida.txt', 'r') as dividatxt:
    divida_dicionario = pickle.load(dividatxt)

except:
  dividatxt = open("alunos.dat", "wb")
  arqAlunos.close()
  alunos = {}







### Gravando os dados no arquivo
# Repetir pela quantidade de arquivos

arqAlunos = open("alunos.dat", "wb")
pickle.dump(alunos, arqAlunos)
arqAlunos.close()