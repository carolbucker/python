# Solicitando entrada da variável idade
idade =  int(input("Qual a sua idade?"))

# Definindo a categoria atraves da idade

## categoria = "Indefinida"
if idade < 13:
    categoria = "Criança"
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"
elif idade >= 18 and idade < 60:
    categoria = "Adulto"
else :
    categoria = "Idoso"

print(f"A pessoa é classificada como: {categoria}")