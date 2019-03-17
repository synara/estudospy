numero = int(input("Digite um número: "))
while numero >= 0:

    fatorial = 1
    while numero > 1:
        fatorial *= numero
        numero -= 1
    print(fatorial)
    numero = int(input("Digite um número: "))
