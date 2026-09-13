# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exactamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

import random
from collections import deque


def generate_maze(m, n, room=0, wall=1, cheese="."):
    """Gera um labirinto perfeito de m X n células usando DFS itarativo.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Pilha explícita para substituir a dinamica do python de guardar as chamadas recursivas da função
    pilha = [(0, 0)]
    maze[1][1] = room  # Marca a primeira sala como visitada
    while pilha:
        x, y = pilha[-1]
        random.shuffle(directions)
        found = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Derruba a parede entre as duas salas
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                # Marca a nova sala como visitada
                maze[2 * nx + 1][2 * ny + 1] = room
                # Empilha a nova sala
                pilha.append((nx, ny))
                found = True
                break

        # backtracking quando nao há mais vizinhos desconhecidos
        if not found:
            pilha.pop()

    # Posiciona o queijo em uma sala
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * n))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))


def find_path(maze, wall=1, cheese="."):
    """Encontra um caminho de (1,1) até o queijo usando busca em largura."""

    start = (1, 1)
    queijo = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == cheese:
                queijo = (i, j)
                break
        if queijo is not None:
            break
    if queijo is None:
        return None
    # Fila da busca em largura
    fila = deque([start])
    # Guarda de onde viemos para conseguir reconstruir o caminho
    anterior = {start: None}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        x, y = fila.popleft()
        if (x, y) == queijo:
            break
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # Verifica se posciao é valida
            if not (0 <= nx < len(maze) and 0 <= ny < len(maze[0])):
                continue
            if maze[nx][ny] == wall or (nx, ny) in anterior:
                continue

            # Guarda o ponto anterior que chegou nesse e adiciona esse novo na fila
            anterior[(nx, ny)] = (x, y)
            fila.append((nx, ny))

    if queijo not in anterior:
        return None

    # Reconstrói o caminho, começando pelo queijo
    caminho = []
    atual = queijo

    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]

    # Como construímos de trás para frente, precisamos inverter
    caminho.reverse()

    return caminho


def print_maze_path(maze, path, start=(1, 1), cheese="."):
    """Exibe o labirinto destacando o caminho encontrado."""

    resultado = [row[:] for row in maze]

    for x, y in path:
        if (x, y) != start and resultado[x][y] != cheese:
            resultado[x][y] = "."

    x, y = start
    resultado[x][y] = "S"

    for row in resultado:
        print(" ".join(map(str, row)))


# Example usage:
if __name__ == "__main__":
    m, n = 10, 14
    random.seed(10110)
    maze = generate_maze(m, n, " ", "W", "X")
    path = find_path(maze, "W", "X")

    print("Maze")
    print_maze_path(maze, path, (1,1), "X")
