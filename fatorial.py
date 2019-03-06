numero = int(input("Digite o valor de n: "))

i = 0
fatorial = 1

if numero == 0:
    print(1)
else:
    while numero > 0:
        fatorial *= numero
        numero -= 1
    
    print(fatorial)
