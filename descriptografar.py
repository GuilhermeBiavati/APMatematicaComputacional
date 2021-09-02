from utils import ascListToString, asctListToBinaryList, binaryListTosctList, encrypt, textListToAscList

print('Informe a mensagem criptografada: ')
mensagemcriptografada = str(input())
print('Informe a chave: ')
chave = str(input())

mensagemcriptografadalista = list(mensagemcriptografada)
chavelista = list(chave)

# polula lista com os caracteres asc2 em binario vindos da mensagem
mensagemcriptografadalistasc = textListToAscList(mensagemcriptografadalista)

mensagemcriptografadalistbinary = asctListToBinaryList(
    mensagemcriptografadalistasc)

# popular lista  com caracteres da chave para asc2
chavelistaasc = textListToAscList(chavelista)

# popular lista da chave com caracteres asc2 para binario
chavelistbinary = asctListToBinaryList(chavelistaasc)

mensagemdescriptografadalistbinary = encrypt(
    mensagemcriptografadalistbinary, chavelistbinary)

# polula lista com os caracteres binario para asc2 vindos da mensagem descriptografada
listchavedescriptografadaasc = binaryListTosctList(
    mensagemdescriptografadalistbinary)

# contatena na variavel a converção dos caracateres em asc2 para texto assim resultando na mensagem original
mensagemdescriptografada = ascListToString(listchavedescriptografadaasc)
# printa a mensagem
print("Mensagem descriptografada")
print(mensagemdescriptografada)
