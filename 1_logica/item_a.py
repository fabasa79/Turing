
def Le_linha():#Função que servirá para ler a linha de números passada pelo usuário.
    Linha = input("Digite os números da linha (separados por um espaço): ")
    L = Linha.split()
    Linha = []
    for elemento in L:
        Linha.append(int(elemento))
    return(Linha)

def Normaliza(L, soma): #Função para normalizar os valores da linha.
    media = soma/len(L)
    for i in range(len(L)):
        L[i] = L[i] - media

def Soma(L): #Função que soma todos os elementos de uma linha.
    soma = 0
    for elemento in L:
        soma += elemento
    return(soma)

def Procura_soma(L): #Função que procura a maior soma possível na linha.
    elementos = 1
    maiorsoma = L[0]
    valor = 0
    sequencia = 1
    while elementos < len(L):
        inicio = 0
        while inicio + elementos <= len(L):
            Lista = L[inicio:inicio+elementos]
            soma = Soma(Lista)
            if maiorsoma <= soma:
                maiorsoma = soma
                valor = inicio
                sequencia = elementos
            inicio += 1
        elementos +=1
    return(valor, sequencia)

def main():
    Linha = Le_linha()
    soma = Soma(Linha)
    Normaliza(Linha, soma)
    valor, sequencia = Procura_soma(Linha)
    print("{}, {}" .format(valor, sequencia))

main()
            
    
        

            
            
