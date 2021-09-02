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


def textListToAscList(textList):
    ascList = []

    for i in range(len(textList)):
        ascList.append(ord(textList[i]))

    return ascList


def asctListToBinaryList(ascList):
    binaryList = []

    for i in range(len(ascList)):
        binaryList.append(decToBin(int(ascList[i])))

    return binaryList


def binaryListTosctList(binarycList):
    ascList = []

    for i in range(len(binarycList)):
        ascList.append(binaryToDecimal(int(binarycList[i])))

    return ascList


def ascListToString(ascList):
    string = ""
    for i in range(len(ascList)):
        string += chr(int(ascList[i]))
    return string


def encrypt(mesageBinaryList, keyBinaryList):

    decryptBinaryList = []
    index = 0
    for i in range(len(mesageBinaryList)):
        # separa binario em uma nova lista tanto da mensagem quanto da chave
        listItem = list(mesageBinaryList[i])
        listItemChave = list(keyBinaryList[index])
        decryptBinaryItem = ""
        # quando a mensagem é maior que a chave é necessario preencher-la repetindo chave
        if i >= (len(keyBinaryList) - 1):
            index = 0
        else:
            index += 1
        # Loop passa em cada caracter da mensagem e da cheve fazendo a operação ou exclusiva
        # e concatenando os resultados em uma variavel
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
                decryptBinaryItem += "1"
            else:
                decryptBinaryItem += "0"

        decryptBinaryList.append(decryptBinaryItem)

    return decryptBinaryList
