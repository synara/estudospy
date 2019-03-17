largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

auxl = largura
auxa = altura

while altura > 0:
    while largura > 0:
        if altura == auxa or altura == 1:
            print('#', end = "")
        else:
            if largura == auxl or largura == 1:
                print('#', end = "")
            else:
                print(' ', end = "")
        largura = largura - 1
    largura = auxl
    altura = altura - 1
    print()
            
