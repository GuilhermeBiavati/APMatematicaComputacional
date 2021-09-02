
# função para converter de decimal para binario

def decToBin(num):
    return bin(num).replace("0b", '').zfill(8)

# função para converter de binario para decimal


def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

# Receber as informações necesarias


print('Informe a mensagem criptografada: ')
mensagem = str(input())
print('Informe a chave: ')
chave = str(input())

# iniciando as variaveis

# polula lista com os caracteres asc2 em binario vindos da mensagem
mensagemlistbinary = list(map(''.join, zip(*[iter(mensagem)]*8)))
chavelista = list(chave)
chavelistaasc = []
chavelistbinary = []
chavedescriptografada = ""
listchavedescriptografadaasc = []
mensagemdescriptografada = ""

# popular lista  com caracteres da chave para asc2


for i in range(len(chavelista)):
    chavelistaasc.append(ord(chavelista[i]))

# popular lista da chave com caracteres asc2 para binario

for i in range(len(chavelistaasc)):
    chavelistbinary.append(decToBin(chavelistaasc[i]))

# Loop passa em cada item da lista binaria na mensagem

index = 0
for i in range(len(mensagemlistbinary)):

    # separa binario em uma nova lista tanto da mensagem quanto da chave
    listItem = list(mensagemlistbinary[i])
    listItemChave = list(chavelistbinary[index])

    # quando a mensagem é maior que a chave é necessario preencher-la repetindo chave
    if i >= (len(chavelistbinary) - 1):
        index = 0
    else:
        index += 1

    # Loop passa em cada caracter da mensagem e da cheve fazendo a operação ou exclusiva e concatenando os resultados em uma variavel

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

# polula lista com os caracteres asc2 em binario vindos da mensagem descriptografada
chavedescriptografada = list(
    map(''.join, zip(*[iter(chavedescriptografada)]*8)))

# polula lista com os caracteres binario para asc2 vindos da mensagem descriptografada

for i in range(len(chavedescriptografada)):
    listchavedescriptografadaasc.append(
        binaryToDecimal(int(chavedescriptografada[i])))

# contatena na variavel a converção dos caracateres em asc2 para texto assim resultando na mensagem original

for i in range(len(listchavedescriptografadaasc)):
    mensagemdescriptografada += chr(int(listchavedescriptografadaasc[i]))

# printa a mensagem
print(mensagemdescriptografada)
