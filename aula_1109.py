# Método de busca leitura
with open("text/exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Método de busca escrever
with open("text/exemplo2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá mundo!")

# Método de busca acrescentar
with open("text/exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nTexto adicional")
