import pygame

pygame.init()

height = 608
width = 1200
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("First Python Game")



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
        self.speed = .6

        self.sprites = []
        self.sprites.append(pygame.image.load("./Idle/Idle01.png"))
        self.sprites.append(pygame.image.load("./Idle/Idle02.png"))
        self.current_sprite = 0

        self.run_sprites = []
        self.run_sprites.append(pygame.image.load("./Walk/walk01.png"))
        self.run_sprites.append(pygame.image.load("./Walk/walk02.png"))
        self.run_sprites.append(pygame.image.load("./Walk/walk03.png"))
        self.run_sprites.append(pygame.image.load("./Walk/walk04.png"))
        self.run_current_sprite = 0

    def Idle(self):
        image = self.sprites[int(self.current_sprite)]
        self.current_sprite += 0.02
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        image = pygame.transform.scale(image, (100, 100))
        screen.blit(image, (self.x, self.y))

    def Run(self):
        run_image = self.run_sprites[int(self.run_current_sprite)]
        self.run_current_sprite += 0.02
        if self.run_current_sprite >= len(self.run_sprites):
            self.run_current_sprite = 0
        run_image = pygame.transform.scale(run_image, (100, 100))
        screen.blit(run_image, (self.x, self.y))
    
    def Reverse(self):
        run_image = self.run_sprites[int(self.run_current_sprite)]
        self.run_current_sprite += 0.02
        if self.run_current_sprite >= len(self.run_sprites):
            self.run_current_sprite = 0
        run_image = pygame.transform.flip(run_image, True, False)
        run_image = pygame.transform.scale(run_image, (100, 100))
        screen.blit(run_image, (self.x, self.y))

    def Render(self):
        if self.left and self.x >= 0:
            self.x += -self.speed
            self.Reverse()
        elif self.right and self.x <= width - 110:
            self.x += self.speed
            self.Run()

        elif self.up and self.y >= 0:
            self.y += -self.speed
            self.Idle()
        elif self.down and self.y <= height - 130:
            self.y += self.speed
            self.Idle()
        else:
            self.Idle()

running = True
new = Player(300, 200)
while running:

    screen.fill((0,0,0))
    # new.Idle()

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
    
    new.Render()

    pygame.display.update()
