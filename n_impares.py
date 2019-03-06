numero = int(input("Digite o valor de n: "))

contador = 0
impares = 0
i = 1

while impares < numero:
    if i % 2 != 0:
       print(i)
       impares += 1    
    i += 1