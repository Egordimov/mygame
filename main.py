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
wall_h =  pygame.transform.scale(pygame.image.load("images/wall_h.png"),(64, 32))
wall_v =  pygame.transform.scale(pygame.image.load("images/wall_v.png"),(32,64))

# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()

#создание объектов 
player = Object(player_img,start_x,start_y,3)
all_sprites.add(player)


# создание стен Object(картинка,x,y,скорость)
wall1 = Object(wall_v,0,64,0)
wall2 = Object(wall_v,0,64,0)
wall3 = Object(wall_v,0,128,0)
wall4 = Object(wall_v,0,192,0)
wall5 = Object(wall_v,0,256,0)
wall6 = Object(wall_v,0,320,0)
wall7 = Object(wall_v,0,384,0)
wall8 = Object(wall_v,0,448,0)
wall9 = Object(wall_v,0,512,0)
wall10 = Object(wall_v,0,576,0)
wall11 = Object(wall_v,32,567,0)
wall12 = Object(wall_v,64,567,0)
wall13 = Object(wall_v,96,567,0)
wall14 = Object(wall_v,96,503,0)
wall15 = Object(wall_v,96,439,0)
wall16 = Object(wall_v,96,377,0)
wall17 = Object(wall_v,96,350,0)
wall18 = Object(wall_h,95,350,0)
wall19 = Object(wall_v,0,0,0)
wall20 = Object(wall_v,0,0,0)
wall21 = Object(wall_v,0,0,0)
wall2 = Object(wall_v,0,0,0)
wall23 = Object(wall_v,0,0,0)
wall24 = Object(wall_v,0,0,0)
wall25 = Object(wall_v,0,0,0)
wall26 = Object(wall_v,0,0,0)
wall27 = Object(wall_v,0,0,0)
wall28= Object(wall_v,0,0,0)
wall29 = Object(wall_v,0,0,0)
wall30 = Object(wall_v,0,0,0)
wall31 = Object(wall_v,0,0,0)
wall32 = Object(wall_v,0,0,0)
wall33 = Object(wall_v,0,0,0)
wall34 = Object(wall_v,0,0,0)
wall35 = Object(wall_v,0,0,0)
wall36 = Object(wall_v,0,0,0)
wall37 = Object(wall_v,0,0,0)



walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18)
all_sprites.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18)


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