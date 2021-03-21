import pygame

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("NIggERS")

class Object(pygame.sprite.Sprite):
    def __init__(self, img,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

# точка спавна игрока
start_x = 100
start_y = 440
# импорт изображений
bg = pygame.transform.scale(pygame.image.load("images/bg.png"),(800,600))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"),(35,35))
# создание групп объектов
all_sprites = pygame.sprite.Group()

#создание объектов 
player = Object(player_img,start_x,start_y,3)
all_sprites.add(player)

run = True

while run:
    window.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_UP]:
            player.rect.y -= player.speed
        if keys[pygame.K_DOWN]:
            player.rect.y += player.speed
        if keys[pygame.K_RIGHT]:
            player.image = pygame.transform.flip(player_img , False , False )
            player.rect.x += player.speed
        if keys[pygame.K_LEFT]:
            player.image = pygame.transform.flip(player_img , True , False)
            player.rect.x -= player.speed






















































    all_sprites.draw(window)
    all_sprites.update()
    pygame.display.update()