#Variáveis
diaInscricao = 29
dataMaximaInscrição = 28
indicação = True
listaDeEspera = False
idadeMinima = 14
idadeMaxima = 17
idadeMarcelo = 15

if diaInscricao > dataMaximaInscrição :
    print("Marcelo tem indicação especial")
else :
    print("Marcelo não tem indicação especial")

if idadeMinima < idadeMarcelo and idadeMarcelo < idadeMaxima :
    print("Marcelo pode se inscrever")
else:
    print("Marcelo não tem idade permitida")

if listaDeEspera == False:
    print("Marcelo não está na lista de espera")



