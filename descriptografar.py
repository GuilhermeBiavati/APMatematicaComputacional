
def decToBin(num):
    return bin(num).replace("0b", '').zfill(8)


def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


print('Informe a mensagem: ')
mensagem = str(raw_input())
print('Informe a chave: ')
chave = str(input())


mensagemlistbinary = list(map(''.join, zip(*[iter(mensagem)]*8)))


chavelista = list(chave)

chavelistaasc = []
chavelistbinary = []

for i in range(len(chavelista)):
    chavelistaasc.append(ord(chavelista[i]))


for i in range(len(chavelistaasc)):
    chavelistbinary.append(decToBin(chavelistaasc[i]))


chavedescriptografada = ""

for i in range(len(mensagemlistbinary)):
    listItem = list(mensagemlistbinary[i])

    if i > len(chavelistbinary)-1:
        listItemChave = list(chavelistbinary[0])
    else:
        listItemChave = list(chavelistbinary[i])

    for i in range(len(listItem)):

        if(listItem[i] == "1"):
            carac1 = True
        else:
            carac1 = False

        if(listItemChave[i] == "1"):
            carac2 = True
        else:
            carac2 = False

        if(carac1 ^ carac2):
            chavedescriptografada += "1"
        else:
            chavedescriptografada += "0"

listchavedescriptografadaasc = []

chavedescriptografada = list(
    map(''.join, zip(*[iter(chavedescriptografada)]*8)))


for i in range(len(chavedescriptografada)):
    listchavedescriptografadaasc.append(
        binaryToDecimal(int(chavedescriptografada[i])))

mensagemdescriptografada = ""

for i in range(len(listchavedescriptografadaasc)):
    mensagemdescriptografada += chr(int(listchavedescriptografadaasc[i]))

print(mensagemdescriptografada)
