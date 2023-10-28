agenda = [
  ['Thallys', 'tatalys@ufrn', '999998888'],
  ['Charles', 'xaxarles@ufrn', '999997777'],
  ['Lucas', 'lulucas@ufrn', '999994444'],
  ['Charles Brown', 'brown@ufrn', '999990000'],
  ['Charles Chaplin', 'chaplin@ufrn', '000000000']
]
opcao = ""
while opcao != '0':
  print("====================")
  print("Programa Mini Agenda")
  print("====================")
  print("   1 - Cadastrar Contato")
  print("   2 - Exibir Lista de Contatos")
  print("   3 - Procurar Contato")
  print("   0 - Encerrar")
  opcao = input("Escolha sua opção: ")
  
  if opcao == '1':
    print()
    print("Módulo de cadastro")
    contato = []
    nome = input("Digite um nome: ")
    contato.append(nome)
    email = input("Digite um email: ")
    contato.append(email)
    fone = input("Digite um número de celular: ")
    contato.append(fone)
    agenda.append(contato)
    print()
  elif opcao == '2':
    print()
    print("Módulo de relatório")
    for i in agenda:
      print("Nome:\t", i[0])
      print("E-mail:\t", i[1])
      print("Fone:\t", i[2])
      print()
    print()
  elif opcao == '3':
    print()
    print("Módulo de consulta")
    nome_busca = input("Nome a procurar: ") 
    achou = False
    for pessoa in agenda:
      if nome_busca.upper() in pessoa[0].upper():
        achou = True
        print()
        print("Nome:\t", pessoa[0])
        print("E-mail:\t", pessoa[1])
        print("Fone:\t", pessoa[2])
        print()
    if not achou:
      print("Nome não encontrado!")
    print()
  elif opcao == '0':
    print()
    print("Módulo de encerramento")
    print()
  else:
    print("Opção inválida!")

print("Até logo!")