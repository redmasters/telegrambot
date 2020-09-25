print("Ola, quem tai?")
nome = input(">: ")

if "O meu nome eh" in nome:
    nome = nome[14:]

conhecidos = ['Raimundo', 'Will', 'Joao' ]
frase = 'Muito prazer '
if nome in conhecidos:
    frase = 'Eaew'
else:
    frase = 'Muito prazer '

print(frase + nome)

while True:
    resposta = input(">: ")
    if resposta == "tchau":
        break
    else:
        print("Digite outra coisa")

print("Tchau, bye!")
