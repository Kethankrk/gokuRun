import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("First Python Game")

goku_image = pygame.image.load("goku.png")
playerX = 300
playerY = 300

changeX = 0
changeY = 0


def player(x, y):
    screen.blit(goku_image, (x, y))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = - 0.4
            if event.key == pygame.K_RIGHT:
                changeX = 0.4

            if event.key == pygame.K_UP:
                changeY = - 0.4
            if event.key == pygame.K_DOWN:
                changeY =  0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeY = 0

    playerY += changeY
    playerX += changeX
    if playerY > 600 or playerY < 0:
        continue
    if playerX > 720 or playerX < 0:
        continue
    player(playerX, playerY)

    pygame.display.update()
