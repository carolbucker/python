# Pesquisar no dicionário
listaAluno = {"Miguel": 8, "Carol": 7}
print("Lista de Alunos e suas notas: ", listaAluno)

# Solicitando o nome do aluno
nomeAluno = input("Digite aqui o nome do aluno: ")

if nomeAluno in listaAluno:
    print(f"A nota do aluno é: {listaAluno[nomeAluno]}")
else:
    print("Aluno não está na lista")


