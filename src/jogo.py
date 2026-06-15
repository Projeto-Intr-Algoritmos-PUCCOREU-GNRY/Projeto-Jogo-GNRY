import pygame

from src.config import *
from src.funcoes import *
from src.sprites import carregar_frames_bird


def desenhar_tela_inicial(tela, fonte, recorde, tela_inicial_img, contador):
    tela.blit(tela_inicial_img, (0, 0))

    texto_recorde = fonte.render(f"RECORDE: {recorde}", True, BRANCO)

    tela.blit(
        texto_recorde,
        (
            LARGURA // 2 - texto_recorde.get_width() // 2,
            345
        )
    )

    if (contador // 30) % 2 == 0:
        instrucao = fonte.render(
            "PRESSIONE ESPACO PARA COMECAR",
            True,
            BRANCO
        )

        tela.blit(
            instrucao,
            (
                LARGURA // 2 - instrucao.get_width() // 2,
                395
            )
        )

    pygame.display.update()


def desenhar_chao(tela, chao_img):
    y_chao = ALTURA - chao_img.get_height()

    for x in range(0, LARGURA, chao_img.get_width()):
        tela.blit(chao_img, (x, y_chao))


def executar_jogo():
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    clock = pygame.time.Clock()

    fonte = pygame.font.SysFont("arial", 32)
    fonte_grande = pygame.font.SysFont("arial", 56)

    frames = carregar_frames_bird(
        "assets/imagens/birds/BirdSprite.png"
    )

    background = pygame.image.load(
        "assets/imagens/fase1/background_fase1.png"
    ).convert()

    background = pygame.transform.scale(
        background,
        (LARGURA, ALTURA)
    )

    tela_inicial_img = pygame.image.load(
        "assets/imagens/tela_inicial.png"
    ).convert()

    tela_inicial_img = pygame.transform.scale(
        tela_inicial_img,
        (LARGURA, ALTURA)
    )

    chao_img = pygame.image.load(
        "assets/imagens/fase1/chao_fase1.png"
    ).convert_alpha()

    chao_img = pygame.transform.scale(
        chao_img,
        (200, 32)
    )

    cano_img = pygame.image.load(
        "assets/imagens/fase1/cano_fase1.png"
    ).convert_alpha()

    cano_img = pygame.transform.scale(
        cano_img,
        (80, 400)
    )

    cano_img_invertido = pygame.transform.flip(
        cano_img,
        False,
        True
    )

    while True:
        passaro = {
            "x": 120,
            "y": 200,
            "largura": 64,
            "altura": 64,
            "velocidade": 0
        }

        primeiro_cano = criar_cano()
        primeiro_cano["x"] = 500
        canos = [primeiro_cano]

        pontos = 0
        recorde = carregar_recorde()
        game_over = False
        tela_inicial = True
        contador_canos = 0
        contador_tela_inicial = 0

        frame_atual = 0
        contador_animacao = 0

        while True:
            clock.tick(FPS)

            reiniciar_partida = False

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        if tela_inicial:
                            tela_inicial = False
                            passaro["velocidade"] = FORCA_PULO

                        elif game_over:
                            reiniciar_partida = True

                        else:
                            passaro["velocidade"] = FORCA_PULO

            if reiniciar_partida:
                break

            if tela_inicial:
                contador_tela_inicial += 1

                desenhar_tela_inicial(
                    tela,
                    fonte,
                    recorde,
                    tela_inicial_img,
                    contador_tela_inicial
                )

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

                contador_animacao += 1

                if contador_animacao >= 8:
                    frame_atual += 1

                    if frame_atual >= len(frames):
                        frame_atual = 0

                    contador_animacao = 0

                if verificar_colisao(passaro, canos):
                    game_over = True

                    novo_recorde = atualizar_recorde(recorde, pontos)

                    if novo_recorde != recorde:
                        recorde = novo_recorde
                        salvar_recorde(recorde)

            tela.blit(background, (0, 0))

            for cano in canos:
                tela.blit(
                    cano_img_invertido,
                    (
                        cano["x"],
                        cano["altura_topo"] - cano_img.get_height()
                    )
                )

                tela.blit(
                    cano_img,
                    (
                        cano["x"],
                        cano["altura_topo"] + cano["abertura"]
                    )
                )

            tela.blit(
                frames[frame_atual],
                (passaro["x"], passaro["y"])
            )

            desenhar_chao(tela, chao_img)

            texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
            texto_recorde = fonte.render(f"Recorde: {recorde}", True, BRANCO)

            tela.blit(texto_pontos, (20, 20))
            tela.blit(texto_recorde, (20, 60))

            if game_over:
                texto_game_over = fonte_grande.render(
                    "GAME OVER",
                    True,
                    VERMELHO
                )

                texto_pontuacao = fonte.render(
                    f"Pontuação final: {pontos}",
                    True,
                    BRANCO
                )

                texto_reiniciar = fonte.render(
                    "Pressione ESPAÇO para jogar novamente",
                    True,
                    BRANCO
                )

                tela.blit(texto_game_over, (250, 160))
                tela.blit(texto_pontuacao, (285, 230))
                tela.blit(texto_reiniciar, (190, 285))

            pygame.display.update()