def pesquisarAluno():
  print()
  matr = input("Favor informar a matrícula: ")
  if matr in alunos:
    print("Nome: ", alunos[matr][0])
    print("Matrícula: ", matr)
    print("Data de nascimento: ", alunos[matr][1])
  else:
    print("Matrícula não encontrada!")
  input("Tecle ENTER para continuar!")


def editarAluno():
  print()
  matr = input("Matrícula do aluno a alterar: ")
  if matr in alunos:
    nome = input("Novo nome: ")
    nasc = input("Nova data de nascimento (dd/mm/aaaa): ")
    alunos[matr] = [nome, nasc]
    print("Aluno alterado com sucesso...")
  else:
    print("Matrícula não encontrada!")
  input("Tecle ENTER para continuar!")


def excluirAluno():
  print()
  matr = input("Matrícula do aluno a excluir: ")
  if matr in alunos:
    del alunos[matr]
    print("Aluno excluído com sucesso...")
  else:
    print("Matrícula não encontrada!")
  input("Tecle ENTER para continuar!")