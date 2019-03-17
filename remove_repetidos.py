def remove_repetidos(lista):
    lista_resultado = []

    for i in range(len(lista)):
        if lista[i] not in lista_resultado:
            lista_resultado.append(lista[i])
            lista_resultado.sort()

    return lista_resultado

numeros = input("Informe uma lista de números: ")
numeros = numeros[1:len(numeros)-1].split(',')
numeros_inteiros = []

for n in numeros:
    numeros_inteiros.append(int(n))

print(remove_repetidos(numeros_inteiros))