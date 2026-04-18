# Cria uma lista com 10 zeros, e repete esse processo 10 vezes (OU SEJA, CRIA UMA MATRIZ...)
tabuleiro = [[0] * 10 for _ in range(10)]

print("--- COORDENADAS DOS NAVIOS ---\n")

# NAVIO HORIZONTAL
for col in range(0,3):
    linha_atual = 2
    coluna_atual = col + 3
    tabuleiro[linha_atual][coluna_atual] = 3
    print(f"Navio Horizontal - Linha {linha_atual}, Coluna {coluna_atual}")     # Imprime posição de cada elemnto do navio posicionado na horizontal

print()

# NAVIO VERTICAL
for lin in range(0,3):
    linha_atual = lin + 4
    coluna_atual = 8
    tabuleiro[linha_atual][coluna_atual] = 3
    print(f"Navio Vertical - Linha {linha_atual}, Coluna {coluna_atual}")       # Imprime posição de cada elemnto do navio posicionado na vertical

# IMPRESSÃO DO TABULEIRO
print("\n--- MAPA DO TABULEIRO ---\n")
for linha in tabuleiro:
    print(*linha)
