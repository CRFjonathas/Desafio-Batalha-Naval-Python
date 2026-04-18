# Cria uma lista com 10 zeros, e repete esse processo 10 vezes (OU SEJA, CRIA UMA MATRIZ...)
tabuleiro = [[0] * 10 for _ in range(10)]

# MOLDE DAS HABILIDADES ESPECIAIS
cruz = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0]
]

cone = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
]

octaedro = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

# NAVIO HORIZONTAL
for col in range(3):
    linha_atual = 1
    coluna_atual = col + 3
    tabuleiro[linha_atual][coluna_atual] = 3

# NAVIO VERTICAL
for lin in range(3):
    linha_atual = lin + 3
    coluna_atual = 8
    tabuleiro[linha_atual][coluna_atual] = 3

# NAVIO DIAGONAL (ESQUERDA -> DIREITA)
for d in range(3):
    linha_atual = d + 7
    coluna_atual = d + 7
    tabuleiro[linha_atual][coluna_atual] = 3

# NAVIO DIAGONAL (DIREITA -> ESQUERDA)
for d in range(3):    
    linha_atual = 4 + d
    coluna_atual = 3 - d
    tabuleiro[linha_atual][coluna_atual] = 3


# HABILIDADE CRUZ
linha_cruz = 3
coluna_cruz = 4
for l in range(3):
    for c in range(5):
        if cruz[l][c] == 1:
            tabuleiro[linha_cruz + l][coluna_cruz + c] = 1

# HABILIDADE CONE
linha_cone = 6
coluna_cone = 2
for l in range(3):
    for c in range(5):
        if cone[l][c] == 1:
            tabuleiro[linha_cone + l][coluna_cone + c] = 1

# HABILIDADE OCTEADRO
linha_octeadro = 0
coluna_octeadro = 3
for l in range(3):
    for c in range(5):
        if octaedro[l][c] == 1:
            tabuleiro[linha_octeadro + l][coluna_octeadro + c] = 1

# IMPRESSÃO DO TABULEIRO
print("\n--- MAPA DO TABULEIRO ---\n")
for linha in tabuleiro:
    print(*linha)
