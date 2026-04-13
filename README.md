# 🚢 Simulador de Batalha Naval (Python Edition)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

## 💻 Sobre o Projeto

Este projeto é uma refatoração completa em **Python** de um sistema de simulação de tabuleiro de Batalha Naval, originalmente desenvolvido em C. O objetivo desta transição é aplicar boas práticas de engenharia de software, substituindo a manipulação crua de memória do C pelas estruturas de dados dinâmicas e de alto nível do Python.

O sistema simula o posicionamento estratégico de frotas e a aplicação de ataques em área (AoE - Area of Effect) utilizando lógica matricial e algoritmos espaciais.

## ⚙️ Níveis de Complexidade e Implementação

O projeto foi arquitetado em três fases evolutivas de complexidade:

### 🏅 Nível Novato (Vetores e Matrizes Básicas)
- Criação de um tabuleiro bidimensional.
- Lógica de posicionamento linear de dois navios (Eixos Vertical e Horizontal).
- Mapeamento e exibição de coordenadas no terminal.

### 🏅 Nível Aventureiro (Expansão e Diagonais)
- Expansão dinâmica do tabuleiro para uma matriz `10x10`.
- Inclusão de posicionamentos oblíquos (Navios nas Diagonais principal e secundária).
- Renderização visual do tabuleiro completo (ex: `0` para água, `3` para navio).

### 🏅 Nível Mestre (Padrões Espaciais e Habilidades)
- Implementação de matrizes de Habilidades Especiais.
- Algoritmos para sobrepor padrões de ataque (Cone, Cruz e Octaedro) sobre o tabuleiro principal.
- Utilização de laços de repetição aninhados otimizados para definir as Zonas de Impacto.

---

## 🎯 Exemplos de Saída (Habilidades Especiais)

Para a renderização das matrizes de habilidades no Nível Mestre, o sistema utiliza a seguinte lógica de impressão em Python:
```python
print(f"{matriz[i][j]} ", end="")
```

Exemplo de saída de habilidade em Cone:
```python
0 0 1 0 0
0 1 1 1 0
1 1 1 1 1
```
Exemplo de saída de habilidade em Octaedro:
```python
0 0 1 0 0
0 1 1 1 0
0 0 1 0 0
```
Exemplo de saída de habilidade em Cruz:
```python
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
```

## 🛠️ Tecnologias e Conceitos Aplicados
- Linguagem: Python 3.10+

- Conceitos Chave:

    - Matrizes e Listas Bidimensionais (Arrays 2D).

    - Manipulação de Índices e Fatiamento (Slicing).

    - Separação de Responsabilidades (Funções modulares em vez de loops massivos).

    - Lógica de Sobreposição de Dados (Data Overlay).