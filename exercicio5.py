def inverte_palavra(entrada):
    n = len(entrada)
    palavra_invertida = ''
    for i in range(n - 1, -1, -1):
        palavra_invertida += entrada[i]

    return f'você digitou {entrada}, o seu inverso é {palavra_invertida}'


palavra = input("Entre com uma palavra: ")
print(inverte_palavra(palavra))
