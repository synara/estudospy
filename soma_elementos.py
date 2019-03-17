def soma_elementos(lista):
    resultado = 0
    for i in range(len(lista)):
        resultado += lista[i]
    return resultado


numeros = "[1, 2, 3]"
numeros = numeros[1:len(numeros)-1].split(',')
numeros_inteiros = []

for n in numeros:
    numeros_inteiros.append(int(n))

print(soma_elementos(numeros_inteiros))