
# Receber as informações necesarias
print('Informe a mensagem: ')
mensagem = str(input())

print('Informe a chave: ')
chave = str(input())

# iniciando as variaveis

mensagemlista = list(mensagem)
mensagemlistaasc = []
mensagemlistbinary = []

chavelista = list(chave)
chavelistaasc = []
chavelistbinary = []

chavecriptografada = ""

index = 0

# função para converter de decimal para binario


def decToBin(num):
    return bin(num).replace("0b", '').zfill(8)

# popular lista com caracteres em asc2


for i in range(len(mensagemlista)):
    mensagemlistaasc.append(ord(mensagemlista[i]))

# popular lista com caracteres asc2 para binario

for i in range(len(mensagemlistaasc)):
    mensagemlistbinary.append(decToBin(mensagemlistaasc[i]))

# popular lista  com caracteres da chave para asc2

for i in range(len(chavelista)):
    chavelistaasc.append(ord(chavelista[i]))

# popular lista da chave com caracteres asc2 para binario

for i in range(len(chavelistaasc)):
    chavelistbinary.append(decToBin(chavelistaasc[i]))

# Loop passa em cada item da lista binaria na mensagem
for i in range(len(mensagemlistbinary)):

    # separa binario em uma nova lista tanto da mensagem quanto da chave
    listbinary = list(mensagemlistbinary[i])
    listbinary2 = list(chavelistbinary[index])

    # quando a mensagem é maior que a chave é necessario preencher-la repetindo chave
    if i >= (len(chavelistbinary) - 1):
        index = 0
    else:
        index += 1

    # Loop passa em cada caracter da mensagem e da cheve fazendo a operação ou exclusiva e concatenando os resultados em uma variavel
    for i in range(len(listbinary)):

        if(listbinary[i] == "1"):
            carac1 = True
        else:
            carac1 = False

        if(listbinary2[i] == "1"):
            carac2 = True
        else:
            carac2 = False

        if(carac1 ^ carac2):
            chavecriptografada += "1"
        else:
            chavecriptografada += "0"

# printa a mensagem criptografada
print(chavecriptografada)
