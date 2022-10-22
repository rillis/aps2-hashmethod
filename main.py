import itertools

def criptografar(frase, chave):
    criptografado=""
    for x, y in zip(frase, itertools.cycle(chave)):
        criptografado+=chr(ord(x)+ord(y))
    return criptografado

def descriptografar(frase, chave):
    descriptografado=""
    for x, y in zip(frase, itertools.cycle(chave)):
        descriptografado+=chr(ord(x)-ord(y))
    return descriptografado

while(True):
    opcao = int(input("Você deseja: \n1) Criptografar\n2) Descriptografar\nSua escolha: "))
    if opcao == 1:
        frase = input("Digite a frase a ser criptografada: ")
        chave = input("Digite a chave: ")
        print("Frase criptografada:", criptografar(frase, chave))
    else:
        frase = input("Digite a frase criptografada: ")
        chave = input("Digite a chave: ")
        print("Frase descriptografada:", descriptografar(frase, chave))