##coisas para adicionar no programa


##########################
### Programa Principal ###
##########################


### Recuperando os dados do arquivo
## Repetir pela quantidade de arquivos
try:
  arqAlunos = open("alunos.dat", "rb")
  alunos = pickle.load(arqAlunos)
  arqAlunos.close()
except:
  arqAlunos = open("alunos.dat", "wb")
  arqAlunos.close()
  alunos = {}







### Gravando os dados no arquivo
# Repetir pela quantidade de arquivos

arqAlunos = open("alunos.dat", "wb")
pickle.dump(alunos, arqAlunos)
arqAlunos.close()