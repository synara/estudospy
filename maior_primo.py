def maior_primo(numero):
    maiorPrimo = 0
    for i in range(2, numero):
        aux = éPrimo(i, maiorPrimo)
        if aux > maiorPrimo:
            maiorPrimo = aux
    return maiorPrimo

def éPrimo(numero, maiorPrimo):
    if (numero <= 1) : 
        return maiorPrimo
    if (numero <= 3) : 
        return numero
  
    if (numero % 2 == 0 or numero % 3 == 0) : 
        return maiorPrimo
  
    i = 5
    while(i * i <= numero) : 
        if (numero % i == 0 or numero % (i + 2) == 0) : 
            return maiorPrimo
        i = i + 6
  
    return numero
