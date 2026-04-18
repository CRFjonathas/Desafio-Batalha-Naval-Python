# Cria uma lista com 10 zeros, e repete esse processo 10 vezes (OU SEJA, CRIA UMA MATRIZ...)
tabuleiro = [[0] * 10 for _ in range(10)]

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

# IMPRESSÃO DO TABULEIRO
print("\n--- MAPA DO TABULEIRO ---\n")
for linha in tabuleiro:
    print(*linha)
