# Manipulação de dicionários/objetos

dadosLivro = {"título": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899}
print("Dados do livro: ", dadosLivro)

# Solicitando nova ano de publicação
novoAno = input("Digite novo ano de publicação aqui: ")

dadosLivro["ano"] = novoAno
print("Dados livro atualizado", dadosLivro)