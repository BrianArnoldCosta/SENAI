# print("Senai na veia")
# print()
# print("Brian Arnold Costa")


# #Projeto01 cronômetro - explodir bomba
# from time import sleep as s
# for i in range(10,-1,-1):
#     print("Irá explodir em:",i,"segundos!!!", sep="")
#     s(1)

# print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOM !!!!!!!!!!")

import pygame # type: ignore
import random

# Inicializar pygame
pygame.init()

# Tamanho da grade
largura_bloco = 30
colunas = 10
linhas = 20
largura_janela = colunas * largura_bloco
altura_janela = linhas * largura_bloco

# Cores
cores = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 165, 0),
    (255, 0, 255)
]

# Formatos das peças (padrão Tetris)
formas = [
    [[1, 1, 1, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[0, 0, 1],
     [1, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[0, 1, 0],
     [1, 1, 1]]
]

# Função para criar uma nova peça
def nova_peca():
    forma = random.choice(formas)
    cor = cores[formas.index(forma)+1]
    return {'forma': forma, 'x': colunas // 2 - len(forma[0]) // 2, 'y': 0, 'cor': cor}

# Desenha a grade e peças
def desenhar(tela, grade, peca_atual):
    tela.fill((0, 0, 0))

    # Desenhar a grade atual
    for y in range(linhas):
        for x in range(colunas):
            pygame.draw.rect(tela, grade[y][x], (x * largura_bloco, y * largura_bloco, largura_bloco, largura_bloco), 0)

    # Desenhar peça atual
    forma = peca_atual['forma']
    for y, linha in enumerate(forma):
        for x, bloco in enumerate(linha):
            if bloco:
                pygame.draw.rect(tela, peca_atual['cor'],
                                 ((peca_atual['x'] + x) * largura_bloco, (peca_atual['y'] + y) * largura_bloco,
                                  largura_bloco, largura_bloco), 0)

    pygame.display.update()

# Verificar colisão
def colisao(grade, peca, dx, dy):
    for y, linha in enumerate(peca['forma']):
        for x, bloco in enumerate(linha):
            if bloco:
                novo_x = peca['x'] + x + dx
                novo_y = peca['y'] + y + dy
                if novo_x < 0 or novo_x >= colunas or novo_y >= linhas:
                    return True
                if novo_y >= 0 and grade[novo_y][novo_x] != (0, 0, 0):
                    return True
    return False

# Travar peça no tabuleiro
def travar(grade, peca):
    for y, linha in enumerate(peca['forma']):
        for x, bloco in enumerate(linha):
            if bloco:
                grade[peca['y'] + y][peca['x'] + x] = peca['cor']

# Remover linhas completas
def limpar_linhas(grade):
    nova_grade = [linha for linha in grade if (0, 0, 0) in linha]
    while len(nova_grade) < linhas:
        nova_grade.insert(0, [(0, 0, 0)] * colunas)
    return nova_grade

# Rotacionar peça
def rotacionar(peca):
    peca['forma'] = [list(row) for row in zip(*peca['forma'][::-1])]

# Loop principal
def main():
    tela = pygame.display.set_mode((largura_janela, altura_janela))
    pygame.display.set_caption("Tetris em Python 🧱")
    relogio = pygame.time.Clock()
    grade = [[(0, 0, 0)] * colunas for _ in range(linhas)]

    peca_atual = nova_peca()
    queda_tempo = 0
    velocidade_queda = 500  # ms

    rodando = True
    while rodando:
        queda_tempo += relogio.get_rawtime()
        relogio.tick()

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not colisao(grade, peca_atual, -1, 0):
                    peca_atual['x'] -= 1
                elif evento.key == pygame.K_RIGHT and not colisao(grade, peca_atual, 1, 0):
                    peca_atual['x'] += 1
                elif evento.key == pygame.K_DOWN and not colisao(grade, peca_atual, 0, 1):
                    peca_atual['y'] += 1
                elif evento.key == pygame.K_UP:
                    antiga = peca_atual['forma']
                    rotacionar(peca_atual)
                    if colisao(grade, peca_atual, 0, 0):
                        peca_atual['forma'] = antiga

        # Queda automática
        if queda_tempo > velocidade_queda:
            if not colisao(grade, peca_atual, 0, 1):
                peca_atual['y'] += 1
            else:
                travar(grade, peca_atual)
                grade = limpar_linhas(grade)
                peca_atual = nova_peca()
                if colisao(grade, peca_atual, 0, 0):
                    print("GAME OVER")
                    rodando = False
            queda_tempo = 0

        desenhar(tela, grade, peca_atual)

    pygame.quit()

if __name__ == "__main__":
    main()
