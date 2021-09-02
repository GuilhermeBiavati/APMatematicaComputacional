print('Informe a mensagem: ')
mensagem = str(input())

mensagemlista = list(mensagem)
mensagemlistaasc = []
mensagemlistbinary = []


def decToBin(num):
    return bin(num).replace("0b", '').zfill(8)


for i in range(len(mensagemlista)):
    # print(mensagemlista[i])
    mensagemlistaasc.append(ord(mensagemlista[i]))


for i in range(len(mensagemlistaasc)):
    mensagemlistbinary.append(decToBin(mensagemlistaasc[i]))

print('Informe a chave: ')
chave = str(input())

chavelista = list(chave)

chavelistaasc = []
chavelistbinary = []

for i in range(len(chavelista)):

    chavelistaasc.append(ord(chavelista[i]))


for i in range(len(chavelistaasc)):
    chavelistbinary.append(decToBin(chavelistaasc[i]))


chavecriptografada = ""

index = 0

for i in range(len(mensagemlistbinary)):

    listbinary = list(mensagemlistbinary[i])
    listbinary2 = list(chavelistbinary[index])

    if i >= (len(chavelistbinary) - 1):
        index = 0
    else:
        index += 1

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


print(chavecriptografada)
