import pygame

from src.config import *
from src.funcoes import *


def desenhar_tela_inicial(tela, fonte, fonte_grande, recorde):
    tela.fill(AZUL)

    titulo = fonte_grande.render("FLAPPY BIRD", True, VERDE)
    instrucao = fonte.render("Pressione ESPAÇO para começar", True, PRETO)
    controles = fonte.render("Controle: ESPAÇO para pular", True, PRETO)
    texto_recorde = fonte.render(f"Recorde: {recorde}", True, PRETO)

    tela.blit(titulo, (250, 130))
    tela.blit(instrucao, (220, 220))
    tela.blit(controles, (240, 260))
    tela.blit(texto_recorde, (330, 310))

    pygame.display.update()


def executar_jogo():

    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    clock = pygame.time.Clock()

    fonte = pygame.font.SysFont("arial", 28)
    fonte_grande = pygame.font.SysFont("arial", 48)

    while True:

        passaro = {
            "x": 120,
            "y": 250,
            "largura": 40,
            "altura": 30,
            "velocidade": 0
        }

        canos = []
        pontos = 0
        recorde = carregar_recorde()
        game_over = False
        tela_inicial = True
        contador_canos = 0

        while True:

            clock.tick(FPS)

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return

                if evento.type == pygame.KEYDOWN:

                    if evento.key == pygame.K_SPACE:

                        if tela_inicial:
                            tela_inicial = False

                        elif game_over:
                            return executar_jogo()

                        else:
                            passaro["velocidade"] = FORCA_PULO

            if tela_inicial:
                desenhar_tela_inicial(tela, fonte, fonte_grande, recorde)
                continue

            if not game_over:

                passaro["velocidade"] += GRAVIDADE
                passaro["y"] += passaro["velocidade"]

                contador_canos += 1

                if contador_canos >= 90:
                    canos.append(criar_cano())
                    contador_canos = 0

                for cano in canos:

                    cano["x"] -= VELOCIDADE_CANO

                    if (
                        not cano["passou"]
                        and cano["x"] + cano["largura"] < passaro["x"]
                    ):
                        pontos += 1
                        cano["passou"] = True

                canos = [
                    cano
                    for cano in canos
                    if cano["x"] + cano["largura"] > 0
                ]

                if verificar_colisao(passaro, canos):

                    game_over = True

                    novo_recorde = atualizar_recorde(recorde, pontos)

                    if novo_recorde != recorde:
                        recorde = novo_recorde
                        salvar_recorde(recorde)

            tela.fill(AZUL)

            pygame.draw.rect(
                tela,
                AMARELO,
                (
                    passaro["x"],
                    passaro["y"],
                    passaro["largura"],
                    passaro["altura"]
                )
            )

            for cano in canos:

                pygame.draw.rect(
                    tela,
                    VERDE,
                    (
                        cano["x"],
                        0,
                        cano["largura"],
                        cano["altura_topo"]
                    )
                )

                pygame.draw.rect(
                    tela,
                    VERDE,
                    (
                        cano["x"],
                        cano["altura_topo"] + cano["abertura"],
                        cano["largura"],
                        ALTURA
                    )
                )

            texto_pontos = fonte.render(f"Pontos: {pontos}", True, PRETO)
            texto_recorde = fonte.render(f"Recorde: {recorde}", True, PRETO)

            tela.blit(texto_pontos, (20, 20))
            tela.blit(texto_recorde, (20, 55))

            if game_over:

                texto_game_over = fonte_grande.render(
                    "GAME OVER",
                    True,
                    VERMELHO
                )

                texto_pontuacao = fonte.render(
                    f"Pontuação final: {pontos}",
                    True,
                    PRETO
                )

                texto_reiniciar = fonte.render(
                    "Pressione ESPAÇO para jogar novamente",
                    True,
                    PRETO
                )

                tela.blit(texto_game_over, (250, 160))
                tela.blit(texto_pontuacao, (285, 225))
                tela.blit(texto_reiniciar, (170, 280))

            pygame.display.update()