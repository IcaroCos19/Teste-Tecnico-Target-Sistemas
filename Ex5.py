def invertePalavra(palavra):
    invert = ""
    for i in range(len(palavra) -1, -1, -1):
        invert += palavra[i]
    return invert


texto = input("digite uma palavra: ")
print("ela invertida: ", invertePalavra(texto))