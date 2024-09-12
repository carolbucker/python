# Digitando lista de compras
frutas = ["maça", "banana", "laranja"]
print("Lista de frutas:" ,frutas)

#Solicitando ao usuário uma nova fruta
novaFruta = input("Digite uma nova fruta: ")

#Adicionando uma nova fruta
frutas.append(novaFruta)
print("Lista de frutas atualizada: ", frutas)

# Removendo uma nova fruta
frutaRemover = input("Digite a fruta que quer remover: ")

if frutaRemover in frutas:
    frutas.remove(frutaRemover)
    print("Lista de frutas atualizada final", frutas)
else:
    print("Fruta não está na lista para ser removida")

