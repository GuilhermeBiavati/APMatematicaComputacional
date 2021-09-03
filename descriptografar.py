from utils import ascListToString, asctListToBinaryList, binaryListTosctList, encrypt, textListToAscList

print('Informe a mensagem criptografada: ')
mensagemcriptografada = str(input())
print('Informe a chave: ')
chave = str(input())
# Transforma tanto a chave quanto a mensagem em listas
mensagemcriptografadalista = list(mensagemcriptografada)
chavelista = list(chave)

# transforma a lista anterior em asc2
mensagemcriptografadalistasc = textListToAscList(mensagemcriptografadalista)

# transforma a lista em asc2 para binario
mensagemcriptografadalistbinary = asctListToBinaryList(
    mensagemcriptografadalistasc)

# transforma a lista anterior em asc2
chavelistaasc = textListToAscList(chavelista)

# transforma a lista em asc2 para binario
chavelistbinary = asctListToBinaryList(chavelistaasc)

# passa cada caracter das listas comparando usando o xor e retornando uma lista de binarios já criptografados
mensagemdescriptografadalistbinary = encrypt(
    mensagemcriptografadalistbinary, chavelistbinary)

# converte a mensagem criptografada para asc2
listchavedescriptografadaasc = binaryListTosctList(
    mensagemdescriptografadalistbinary)

# transforma para texto e concatena a mensagem
mensagemdescriptografada = ascListToString(listchavedescriptografadaasc)
# printa a mensagem
print("Mensagem descriptografada")
print(mensagemdescriptografada)
