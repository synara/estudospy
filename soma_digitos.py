numero = input("Digite um número: ")

i = 0
resultado = 0

while i < len(numero):
    resultado += int(numero[i])
    i += 1

print(resultado)