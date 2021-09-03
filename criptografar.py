from utils import ascListToString, asctListToBinaryList, binaryListTosctList, encrypt, textListToAscList

print('Informe a mensagem: ')
mensagem = str(input())
print('Informe a chave: ')
chave = str(input())

# Transforma tanto a chave quanto a mensagem em listas ex: ['3', '6', '2'...]
mensagemlista = list(mensagem)
chavelista = list(chave)

# transforma a lista anterior em asc2
# ex: [97, 112, 114, 111, 118, 97, 100, 111]
mensagemlistaasc = textListToAscList(mensagemlista)

# transforma a lista em asc2 para binario
# ex: ['01100001', '01110000', '01110010', '01101111', '01110110', '01100001', '01100100', '01101111']
mensagemlistbinary = asctListToBinaryList(mensagemlistaasc)

# transforma a lista anterior em asc2
# ex: [97, 112, 114, 111, 118, 97, 100, 111]
chavelistaasc = textListToAscList(chavelista)

# transforma a lista em asc2 para binario
# ex: ['01100001', '01110000', '01110010', '01101111', '01110110', '01100001', '01100100', '01101111']
chavelistbinary = asctListToBinaryList(chavelistaasc)

# passa cada caracter das listas comparando usando o xor e retornando uma lista de binarios já criptografados
# ex: ['01010000', '01000010', '01000001', '01011110', '01000111', '01010000', '01010101', '01011110']
mensagemcriptografadalistbinary = encrypt(mensagemlistbinary, chavelistbinary)

# converte a mensagem criptografada para asc2
# ex: [80, 66, 65, 94, 71, 80, 85, 94]
mensagemcriptografadalistasc = binaryListTosctList(
    mensagemcriptografadalistbinary)

# transforma para texto e concatena a mensagem
# ex:
mensagemcriptografada = ascListToString(mensagemcriptografadalistasc)

print("Mensagem criptografada: ")
print(mensagemcriptografada)
