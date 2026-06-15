import pygame


def carregar_frames_bird(local_arquivo):

    sheet = pygame.image.load(local_arquivo).convert_alpha()

    largura_sheet = sheet.get_width()
    altura_sheet = sheet.get_height()

    quantidade_frames = 8
    largura_frame = largura_sheet // quantidade_frames

    frames = []

    for i in range(quantidade_frames):

        frame = sheet.subsurface(
            (
                i * largura_frame,
                0,
                largura_frame,
                altura_sheet
            )
        ).copy()

        frame = pygame.transform.scale(
            frame,
            (64, 64)
        )

        frames.append(frame)

    return frames