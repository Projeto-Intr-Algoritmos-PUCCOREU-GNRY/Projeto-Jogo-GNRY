import pygame
import random

from src.config import *
from src.funcoes import *
from src.sprites import carregar_frames_bird

fases = {
    1: {
        "background": "assets/imagens/fase1/background_fase1.png",
        "cano": "assets/imagens/fase1/cano_fase1.png"
    },
    2: {
        "background": "assets/imagens/fase2/background_fase2.png",
        "cano": "assets/imagens/fase2/cano_fase2.png"
    },
    3: {
        "background": "assets/imagens/fase3/background_fase3.png",
        "cano": "assets/imagens/fase3/cano_fase3.png"
    },
    4: {
        "background": "assets/imagens/fase4/background_fase4.png",
        "cano": "assets/imagens/fase4/cano_fase4.png"
    },
    5: {
        "background": "assets/imagens/fase5/background_fase5.png",
        "cano": "assets/imagens/fase5/cano_fase5.png"
    }
}

nomes_fases = {
    1: "CAMPO",
    2: "CIDADE DOURADA",
    3: "HORIZONTE NOTURNO",
    4: "DISTRITO INDUSTRIAL",
    5: "NEO SUNSET"
}

def carregar_fase(numero):
    background = pygame.image.load(
        fases[numero]["background"]
    ).convert()

    background = pygame.transform.scale(
        background,
        (LARGURA, ALTURA)
    )

    cano = pygame.image.load(
        fases[numero]["cano"]
    ).convert_alpha()

    cano = pygame.transform.scale(
        cano,
        (100, 400)
    )

    cano_invertido = pygame.transform.flip(
        cano,
        False,
        True
    )

    return background, cano, cano_invertido

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


#def desenhar_chao(tela, chao_img):
#    y_chao = ALTURA - chao_img.get_height()
#
#    for x in range(0, LARGURA, chao_img.get_width()):
#        tela.blit(chao_img, (x, y_chao))


def executar_jogo():
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    clock = pygame.time.Clock()

    som_pulo = pygame.mixer.Sound(
    "assets/sons/jump_song.wav"
    )
    som_pulo.set_volume(0.7)

    som_gameover = pygame.mixer.Sound(
    "assets/sons/gameover.wav"
    )
    som_gameover.set_volume(0.7)

    musicas_jogo = [
        "assets/sons/jogo1.mp3",
        "assets/sons/jogo2.mp3",
        "assets/sons/jogo3.mp3"
    ]

    fonte = pygame.font.Font(
        "assets/fontes/fs-pixel-sans-unicode-regular.ttf",
        36
    )

    fonte_grande = pygame.font.Font(
        "assets/fontes/fs-pixel-sans-unicode-regular.ttf",
         72
    )

    frames = carregar_frames_bird(
    "assets/imagens/birds/BirdSprite.png"
    )

    tela_inicial_img = pygame.image.load(
        "assets/imagens/tela_inicial.png"
    ).convert()

    tela_inicial_img = pygame.transform.scale(
        tela_inicial_img,
        (LARGURA, ALTURA)
    )

    #chao_img = pygame.image.load(
    #    "assets/imagens/fase1/chao_fase1.png"
    #).convert_alpha()

    #chao_img = pygame.transform.scale(
    #    chao_img,
    #    (200, 32)
    #)

    while True:

        fase_atual = 1
        background, cano_img, cano_img_invertido = carregar_fase(
            fase_atual
        )
    
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
        vitoria = False
        contador_canos = 0
        contador_tela_inicial = 0

        tempo_mensagem_fase = 0

        frame_atual = 0
        contador_animacao = 0

        pygame.mixer.music.load(
            "assets/sons/menu.mp3"
        )
        pygame.mixer.music.set_volume(0.20)

        pygame.mixer.music.play(-1)

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

                            pygame.mixer.music.stop()

                            pygame.mixer.music.load(
                                random.choice(musicas_jogo)
                            )

                            pygame.mixer.music.play(-1)

                            som_pulo.play()

                            passaro["velocidade"] = FORCA_PULO

                        elif game_over or vitoria:
                            reiniciar_partida = True

                        else:
                            passaro["velocidade"] = FORCA_PULO
                            som_pulo.play()

            if reiniciar_partida:

                pygame.mixer.music.stop()

                pygame.mixer.music.load(
                    "assets/sons/menu.mp3"
                )

                pygame.mixer.music.play(-1)

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

            if not game_over and not vitoria:
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

                        if pontos >= 50:
                            vitoria = True


                        if pontos < 10:
                            nova_fase = 1
                        elif pontos < 20:
                            nova_fase = 2
                        elif pontos < 30:
                            nova_fase = 3
                        elif pontos < 40:
                            nova_fase = 4
                        else:
                            nova_fase = 5

                        if nova_fase != fase_atual:
                            fase_atual = nova_fase

                            background, cano_img, cano_img_invertido = carregar_fase(
                                fase_atual
                            )

                            tempo_mensagem_fase = 120

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
                    pygame.mixer.music.stop()
                    som_gameover.play()

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

            #desenhar_chao(tela, chao_img)

            sombra = fonte.render(
                f"Pontos: {pontos}",
                True,
                PRETO
            )

            texto_pontos = fonte.render(
                f"Pontos: {pontos}",
                True,
                BRANCO
            )

            tela.blit(sombra, (22, 22))
            tela.blit(texto_pontos, (20, 20))

            sombra_recorde = fonte.render(
                f"Recorde: {recorde}",
                True,
                PRETO
            )

            texto_recorde = fonte.render(
                f"Recorde: {recorde}",
                True,
                BRANCO
            )

            tela.blit(sombra_recorde, (22, 62))
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
            
            if vitoria:

                texto_vitoria = fonte_grande.render(
                    "PARABENS!",
                    True,
                    BRANCO
                )

                texto_final = fonte.render(
                    "VOCE COMPLETOU O FLAPPY PYTHON",
                    True,
                    BRANCO
                )

                texto_reiniciar = fonte.render(
                    "PRESSIONE ESPACO PARA JOGAR NOVAMENTE",
                    True,
                    BRANCO
                )

                tela.blit(
                    texto_vitoria,
                    (
                        LARGURA // 2 - texto_vitoria.get_width() // 2,
                        150
                    )
                )

                tela.blit(
                    texto_final,
                    (
                        LARGURA // 2 - texto_final.get_width() // 2,
                        230
                    )
                )

                tela.blit(
                    texto_reiniciar,
                    (
                        LARGURA // 2 - texto_reiniciar.get_width() // 2,
                        300
                    )
                )

            if tempo_mensagem_fase > 0:

                texto_nome = fonte_grande.render(
                    nomes_fases[fase_atual],
                    True,
                    BRANCO
                )

                tela.blit(
                    texto_nome,
                    (
                        LARGURA // 2 - texto_nome.get_width() // 2,
                        ALTURA // 2 - 30
                    )
                )

                tempo_mensagem_fase -= 1
            pygame.display.update()