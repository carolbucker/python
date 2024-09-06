frutas = ["maça", "banana", "laranja"]
print("Lista de frutas:", frutas)

frutas.append("uva")
print("Lista de frutas atualizada:", frutas)

print("Primeira fruta:", frutas[0])

print("Terceira fruta:", frutas[3])

frutas.remove(frutas[2])
print(frutas)


# Exemplo com dicionários/objeto
pessoa = {"Nome": "Ana", "idade": 30}
print("Pessoa:", pessoa)

# Acessando valores
print("Nome:", pessoa["Nome"])

# Adicionando um novo par de chave valor
pessoa["cidade"] = "São Paulo"
print("Pessoa atualizada:", pessoa)

listaPessoas = []

pessoa = {"nome": "Ana", "idade": 32}
listaPessoas.append(pessoa)
print(listaPessoas)

pessoa = {"nome": "Brenda", "idade": 26}
listaPessoas.append(pessoa)
print(listaPessoas)

pessoa ={"nome": "Fernanda", "idade": 48}
listaPessoas.append(pessoa)
print(listaPessoas)

brenda = listaPessoas[1]
print(brenda)

conjunto = { 1, 2, 3, 4, 5}
print(3 in conjunto)
print(6 in conjunto)

