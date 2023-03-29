import pygame

pygame.init()

height = 608
width = 1200
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("First Python Game")

goku_image = pygame.image.load("goku.png")



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.changeX = 0
        self.changeY = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.speed = 2

    def Start(self):
        screen.blit(goku_image, (self.x, self.y))

    def Render(self):
        if self.left and self.x >= 0:
            self.x += -self.speed
        if self.right and self.x <= width - 110:
            self.x += self.speed
        if self.up and self.y >= 0:
            self.y += -self.speed
        if self.down and self.y <= height - 130:
            self.y += self.speed
        
        self.Start()


running = True
new = Player(300, 200)
while running:

    screen.fill((0,0,0))
    # new.Start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                new.left = True
            if event.key == pygame.K_d:
                new.right = True
            if event.key == pygame.K_w:
                new.up = True
            if event.key == pygame.K_s:
                new.down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                new.left = False
            if event.key == pygame.K_d:
                new.right = False
            if event.key == pygame.K_w:
                new.up = False
            if event.key == pygame.K_s:
                new.down = False
    # new.Start()
    new.Render()

    pygame.display.update()
