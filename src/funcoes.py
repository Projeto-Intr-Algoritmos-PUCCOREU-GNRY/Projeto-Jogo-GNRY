import random
import os
import pygame

from src.config import *


def criar_cano():
    altura_topo = random.randint(60, 280)

    return {
        "x": LARGURA,
        "largura": LARGURA_CANO,
        "altura_topo": altura_topo,
        "abertura": DISTANCIA_ENTRE_CANOS,
        "passou": False
    }


def carregar_recorde():

    if not os.path.exists(ARQUIVO_RECORDE):
        return 0

    with open(ARQUIVO_RECORDE, "r") as arquivo:

        conteudo = arquivo.read().strip()

        if conteudo == "":
            return 0

        return int(conteudo)


def salvar_recorde(recorde):

    with open(ARQUIVO_RECORDE, "w") as arquivo:
        arquivo.write(str(recorde))


def atualizar_recorde(recorde, pontos):

    if pontos > recorde:
        return pontos

    return recorde


def verificar_colisao(passaro, canos):

    # teto
    if passaro["y"] <= 0:
        return True

    # chão
    if passaro["y"] + passaro["altura"] >= ALTURA:
        return True

    rect_passaro = pygame.Rect(
        passaro["x"],
        passaro["y"],
        passaro["largura"],
        passaro["altura"]
    )

    for cano in canos:

        rect_topo = pygame.Rect(
            cano["x"],
            0,
            cano["largura"],
            cano["altura_topo"]
        )

        rect_baixo = pygame.Rect(
            cano["x"],
            cano["altura_topo"] + cano["abertura"],
            cano["largura"],
            ALTURA
        )

        if rect_passaro.colliderect(rect_topo):
            return True

        if rect_passaro.colliderect(rect_baixo):
            return True

    return False