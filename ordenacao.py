numeros = input("Digite três numeros: ")

sequencia = numeros.split(',')
verificar = True

for i in range(1, len(sequencia)):
    if(sequencia[i-1] > sequencia[i]):
        verificar = False
        break

if (verificar):
    print("crescente")
else:
    print("não está em ordem crescente")
