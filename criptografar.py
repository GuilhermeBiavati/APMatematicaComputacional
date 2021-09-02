# Receber as informações necesarias
from utils import ascListToString, asctListToBinaryList, binaryListTosctList, encrypt, textListToAscList


print('Informe a mensagem: ')
mensagem = str(input())
print('Informe a chave: ')
chave = str(input())

# iniciando as variaveis

mensagemlista = list(mensagem)
chavelista = list(chave)

# popular lista com caracteres em asc2
mensagemlistaasc = textListToAscList(mensagemlista)


# popular lista com caracteres asc2 para binario
mensagemlistbinary = asctListToBinaryList(mensagemlistaasc)

# popular lista  com caracteres da chave para asc2
chavelistaasc = textListToAscList(chavelista)

# popular lista da chave com caracteres asc2 para binario
chavelistbinary = asctListToBinaryList(chavelistaasc)

mensagemcriptografadalistbinary = encrypt(mensagemlistbinary, chavelistbinary)

mensagemcriptografadalistasc = binaryListTosctList(
    mensagemcriptografadalistbinary)

mensagemcriptografada = ascListToString(mensagemcriptografadalistasc)

print("Mensagem criptografada: ")
print(mensagemcriptografada)
