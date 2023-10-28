

#parte final do programa principal
alunos = {
1 : ["123456", "João", "BSI"],
2 : ["123123", "Maria", "História"],
3 : ["445566", "José", "Direito"]
}
arqAlunos = open("alunos.dat", "wb")
pickle.dump(alunos, arqAlunos)
arqAlunos.close()


## parte inical
alunos = {}
try:
 arqAlunos = open("alunos.dat", "rb")
 alunos = pickle.load(arqAlunos)
 arqAlunos.close()
except:
 arqAlunos = open("alunos.dat", "wb")
 arqAlunos.close()

print(alunos)