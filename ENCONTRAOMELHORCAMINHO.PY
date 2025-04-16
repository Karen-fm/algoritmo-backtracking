def mostrar_tabuleiro(tabuleiro): # função mostrar o tabuleiro
    for linha in tabuleiro: # Para cada linha no tabuleiro:
        print("|" + "|".join(linha) + "|") # Imprimir a linha formatada com os Pipes -> | 
    print() # Pula uma linha para ficar mais organizado


def movimento_valido(tabuleiro, linha, coluna): # Essa função vê se podemos andar para uma nova posição
    n = len(tabuleiro) # Descobre o tamanho do tabuleiro 
    # Só podemos ir para essa nova posição se:
    # ela estiver dentro do tabuleiro e for um espaço vazio e não for um "X"

    return 0 <= linha < n and 0 <= coluna < n and tabuleiro[linha][coluna] == ' '


def chegou_destino(linha, coluna): # função diz se já chegamos no destino
    return linha == 0 and coluna == 3 # Objetivo é chegar na posição linha 0, coluna 3 na parte de cima do tabuleiro


def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade): # função tenta achar o melhor próximo passo
    if chegou_destino(linha_atual, coluna_atual): # Se já estamos no lugar certo, podemos parar
        return (linha_atual, coluna_atual, profundidade)

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # Lista dos 4 jeitos que podemos andar: pra cima, pra baixo, pra esquerda e pra direita
    # Começa com uma pontuação bem alta (o pior caso)
    melhor_profundidade = float('inf')
    melhor_linha, melhor_coluna = linha_atual, coluna_atual

    for dr, dc in direcoes: # Vamos testar cada direção
        nova_linha = linha_atual + dr # Nova posição na linha
        nova_coluna = coluna_atual + dc # Nova posição na coluna

        if movimento_valido(tabuleiro, nova_linha, nova_coluna): # Só continua se esse movimento for permitido
            tabuleiro[nova_linha][nova_coluna] = '*' # Marca esse lugar como visitado
            _, _, profundidade_rec = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1) # Chama a função de novo, indo mais fundo
            tabuleiro[nova_linha][nova_coluna] = ' ' # Desfaz o movimento, volta como era antes

            if profundidade_rec < melhor_profundidade: # Se esse caminho for melhor (menor profundidade) guarda ele
                melhor_profundidade = profundidade_rec
                melhor_linha = nova_linha
                melhor_coluna = nova_coluna

    return (melhor_linha, melhor_coluna, melhor_profundidade) # Retorna o melhor caminho encontrado (linha, coluna, e quantos passos deu)


def main(): # Função principal começa
    # ' ' caminho livre e 'X' parede
    tabuleiro = [
        [' ', ' ', ' ', ' ', 'X'],
        ['X', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['*', 'X', 'X', ' ', 'X'],
        [' ', ' ', ' ', ' ', ' ']
    ]

    linha_atual, coluna_atual = 3, 0 # Posição atual no começo
    mostrar_tabuleiro(tabuleiro) 

    while not chegou_destino(linha_atual, coluna_atual): # Enquanto não chega no destino
        nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0) # Tenta achar o melhor passo para ir
        # Se não conseguir achar mais caminhos, mostra mensagem e para
        if profundidade == float('inf'):
            print("Não foi possível encontrar um caminho até o destino.")
            break
        # Se achou um bom caminho, segue até lá
        linha_atual, coluna_atual = nova_linha, nova_coluna 
        tabuleiro[linha_atual][coluna_atual] = '*' # Marca esse lugar no caminho
        mostrar_tabuleiro(tabuleiro) # Mostra como o tabuleiro ficou agora


if __name__ == "__main__": # começa a funcionar 
    main() # Chama a função principal pra rodar tudo
