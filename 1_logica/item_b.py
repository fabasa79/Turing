def Le_matriz(): #Função que servirá para ler a matriz de números passada pelo usuário.
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    M = []
    for i in range (lin):
        Linha = input("Digite os valores da linha {}: " .format(i+1))
        L = Linha.split()
        Linha = []
        for elemento in L:
            Linha.append(int(elemento)) 
        M.append(Linha)
    return(M)

def Soma(M): #Função que soma todos os elementos da matriz.
    soma = 0
    for Linha in M:
        for elemento in Linha:
            soma += elemento
    return(soma)

def Normaliza(M, soma): #Função para normalizar os valores da matriz.
    media = soma/(len(M[0])*len(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = M[i][j] - media

def parte_matriz(M, inicio, fim): #Função que divide a matriz em partes menores. Usada para testar possíveis somas.
    Matriz = []
    for i in range(inicio[0], fim[0]):
        Linha = []
        for j in range(inicio[1], fim[1]):
            Linha.append(M[i][j])
        Matriz.append(Linha)
    return(Matriz)
    
def Procura_soma(M): #Função que procura a maior soma possível na matriz.
    maiorsoma = M[0][0]
    i = 0
    j = 0
    elemento = [0, 0]
    final = [0, 0]
    sequencia_I = 1
    sequencia_J = 1
    I = 0
    while I < len(M):
        J = 0
        while J < len(M[0]):
            sequencia_I = 0
            while I + sequencia_I <= len(M):
                sequencia_J = 0
                while J + sequencia_J <= len(M[0]):
                    Matriz = parte_matriz(M, [I, J], [I + sequencia_I,J + sequencia_J])
                    soma = Soma(Matriz)
                    if maiorsoma <= soma:
                        maiorsoma = soma
                        elemento = [I, J]
                        final = [sequencia_I, sequencia_J]
                    sequencia_J += 1
                sequencia_I +=1
            J += 1
        I += 1
    return(elemento, final)

def main():
    Matriz = Le_matriz()
    soma = Soma(Matriz)
    Normaliza(Matriz, soma)
    valor, sequencia = Procura_soma(Matriz)
    print("({}, {}), i = {}, j = {}" .format(valor[0], valor[1], sequencia[0], sequencia[1]))

main()

            
    
