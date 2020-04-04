import pygame

try:
    pygame.init()
except:
    print("PYGAME COM DEFEITO")

# janela -----------------------
largura = 640
comprimento = 480
sair = True

# CORES ---------------------------
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# PERSONAGEM ------------------------------------
pos_x = largura / 2
pos_y = comprimento / 2
tamanho = 100
velo_x = 0
velo_y = 0
relogio = pygame.time.Clock()

fundo = pygame.display.set_mode((largura, comprimento))  # cria janela
pygame.display.set_caption("Jogo do bruno")  # titulo da janela

rot = 0
rot_speed = 2

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velo_x = -5
                velo_y = 0

            if event.key == pygame.K_RIGHT:
                velo_x = 5
                velo_y = 0

            if event.key == pygame.K_UP:
                velo_x = 0
                velo_y = -5
            if event.key == pygame.K_DOWN:
                velo_x = 0
                velo_y = 5
            if event.key == pygame.K_0:
               tamanho-=10
            if event.key == pygame.K_9:
                tamanho+=10

    quadrado = pygame.Surface((tamanho, tamanho))  # define a surface (RECTANGLE)

    quadrado.set_colorkey(verde)  

    quadrado.fill(preto)  # fill the rectangle / surface with green color

    copiado = quadrado.copy()  # creating a copy of orignal image for smooth rotation
    copiado.set_colorkey(verde)

    rect = copiado.get_rect()  # define rect for placing the rectangle at the desired positionrect.center = (largura // 2, comprimento // 2)

    fundo.fill(azul)  # cor de fundo

    pos_x += velo_x
    pos_y += velo_y
    rect.center = (pos_x // 2, pos_y // 2)


    fundo.blit(quadrado, rect)  # drawing the rotated rectangle to the screen

    pygame.display.update()  # atualiza o jogo
    relogio.tick(60)  # velocidade que muda as imagens
    if (pos_x > largura):
        pos_x = 0
    if (pos_x < 0):
        pos_x = largura
    if pos_y > comprimento:
        pos_y = 0;
    if pos_y < 0:
        pos_y = comprimento

pygame.quit()  # saida a janela

