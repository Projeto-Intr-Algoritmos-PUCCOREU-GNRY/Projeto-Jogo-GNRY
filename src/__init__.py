import pygame
import random

pygame.init()

LARGURA = 500
ALTURA = 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird Simples")

clock = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 36)

# Pássaro
passaro_x = 100
passaro_y = 300
passaro_tamanho = 35
velocidade = 0
gravidade = 0.5
pulo = -9

# Canos
cano_largura = 80
espaco = 180
cano_x = LARGURA
cano_altura = random.randint(100, 400)
velocidade_cano = 4

pontos = 0
passou_cano = False
jogando = True
game_over = False

while jogando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if not game_over:
                    velocidade = pulo
                else:
                    # Reiniciar jogo
                    passaro_y = 300
                    velocidade = 0
                    cano_x = LARGURA
                    cano_altura = random.randint(100, 400)
                    pontos = 0
                    passou_cano = False
                    game_over = False

    if not game_over:
        # Movimento do pássaro
        velocidade += gravidade
        passaro_y += velocidade

        # Movimento do cano
        cano_x -= velocidade_cano

        if cano_x < -cano_largura:
            cano_x = LARGURA
            cano_altura = random.randint(100, 400)
            passou_cano = False

        # Pontuação
        if cano_x + cano_largura < passaro_x and not passou_cano:
            pontos += 1
            passou_cano = True

        # Retângulos de colisão
        passaro = pygame.Rect(passaro_x, passaro_y, passaro_tamanho, passaro_tamanho)

        cano_cima = pygame.Rect(cano_x, 0, cano_largura, cano_altura)
        cano_baixo = pygame.Rect(
            cano_x,
            cano_altura + espaco,
            cano_largura,
            ALTURA - (cano_altura + espaco)
        )

        # Colisão
        if passaro.colliderect(cano_cima) or passaro.colliderect(cano_baixo):
            game_over = True

        # Bater no chão ou no teto
        if passaro_y < 0 or passaro_y + passaro_tamanho > ALTURA:
            game_over = True

    # Desenhar fundo
    tela.fill((135, 206, 235))

    # Desenhar chão
    pygame.draw.rect(tela, (222, 184, 135), (0, ALTURA - 80, LARGURA, 80))

    # Desenhar canos
    pygame.draw.rect(tela, (0, 180, 0), (cano_x, 0, cano_largura, cano_altura))
    pygame.draw.rect(
        tela,
        (0, 180, 0),
        (cano_x, cano_altura + espaco, cano_largura, ALTURA - (cano_altura + espaco))
    )

    # Desenhar pássaro
    pygame.draw.circle(
        tela,
        (255, 255, 0),
        (passaro_x + passaro_tamanho // 2, int(passaro_y) + passaro_tamanho // 2),
        passaro_tamanho // 2
    )

    # Texto da pontuação
    texto_pontos = fonte.render(str(pontos), True, (255, 255, 255))
    tela.blit(texto_pontos, (LARGURA // 2, 40))

    if game_over:
        texto_game_over = fonte.render("GAME OVER", True, (255, 0, 0))
        texto_reiniciar = fonte.render("Espaco para reiniciar", True, (255, 255, 255))

        tela.blit(texto_game_over, (150, 280))
        tela.blit(texto_reiniciar, (90, 330))

    pygame.display.flip()

pygame.quit()