import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da janela e do jogo
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')
clock = pygame.time.Clock()

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Variáveis do jogo
tamanho_cobra = 20
velocidade = 10
cobra = [(largura // 2, altura // 2)]
dx, dy = 0, 0
comida = (random.randint(0, largura - tamanho_cobra) // tamanho_cobra * tamanho_cobra,
          random.randint(0, altura - tamanho_cobra) // tamanho_cobra * tamanho_cobra)

# Função para desenhar a cobra e a comida
def desenhar_cobra():
    for parte in cobra:
        pygame.draw.rect(tela, verde, (parte[0], parte[1], tamanho_cobra, tamanho_cobra))
    pygame.draw.rect(tela, vermelho, (comida[0], comida[1], tamanho_cobra, tamanho_cobra))

# Loop principal
jogo_ativo = True
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -tamanho_cobra
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = tamanho_cobra
                dy = 0
            elif event.key == pygame.K_UP:
                dy = -tamanho_cobra
                dx = 0
            elif event.key == pygame.K_DOWN:
                dy = tamanho_cobra
                dx = 0

    # Atualiza a posição da cobra
    cabeça = (cobra[0][0] + dx, cobra[0][1] + dy)
    cobra.insert(0, cabeça)
    if cabeça == comida:
        comida = (random.randint(0, largura - tamanho_cobra) // tamanho_cobra * tamanho_cobra,
                  random.randint(0, altura - tamanho_cobra) // tamanho_cobra * tamanho_cobra)
    else:
        cobra.pop()

    # Verifica colisões
    if (cobra[0][0] < 0 or cobra[0][0] >= largura or
        cobra[0][1] < 0 or cobra[0][1] >= altura or
        cabeça in cobra[1:]):
        jogo_ativo = False

    # Preenche a tela e desenha a cobra e a comida
    tela.fill(branco)
    desenhar_cobra()
    pygame.display.update()
    clock.tick(velocidade)

# Finaliza o pygame
pygame.quit()
