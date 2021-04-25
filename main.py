import pygame
pygame.init()
import pygame.mixer
from tkinter import*
from tkinter import messagebox as mb


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

#creat hide Tk window
Tk().wm_withdraw()

# точка спавна игрока
start_x = 80
start_y =10
# импорт изображений
bg = pygame.transform.scale(pygame.image.load("images/bg.png"),(800,600))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"),(35,35))
wall_h =  pygame.transform.scale(pygame.image.load("images/wall_h.png"),(64, 32))
wall_v =  pygame.transform.scale(pygame.image.load("images/wall_v.png"),(32,64))
enemy_img = pygame.transform.scale(pygame.image.load("images/enemy.png"),(36,50))
coin_img = pygame.transform.scale(pygame.image.load("images/coin.png"),(36,36))
# создание групп объектов
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
items = pygame.sprite.Group()
enimies = pygame.sprite.Group()
#создание объектов 
player = Object(player_img,start_x,start_y,1)
all_sprites.add(player)


# создание стен Object(картинка,x,y,скорость)
wall1 = Object(wall_v,0,0,0)
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
wall19 = Object(wall_h,131,350,0)
wall20 = Object(wall_h,195,350,0)
wall21 = Object(wall_h,259,350,0)
wall22 = Object(wall_h,323,350,0)
wall23 = Object(wall_h,387,350,0)
wall24 = Object(wall_v,451,350,0)
wall25 = Object(wall_v,451,414,0)
wall26 = Object(wall_h,451,450,0)
wall27 = Object(wall_h,500,450,0)
wall28= Object(wall_v,564,418,0)
wall29 = Object(wall_v,564,355,0)
wall30 = Object(wall_h,564,350,0)
wall31 = Object(wall_h,628,350,0)
wall32 = Object(wall_v,661,530,0)
wall33 = Object(wall_v,661,470,0)
wall34 = Object(wall_h,200,570,0)
wall35 = Object(wall_h,0,570,0)
wall36 = Object(wall_h,0,570,0)
wall37 = Object(wall_h,0,0,0)





walls.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37)
all_sprites.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37)

# создание противников

enemy1_x = 390
enemy1_y = 500
enemy1 = Object(enemy_img, enemy1_x,enemy1_y,1)
enimies.add(enemy1)
all_sprites.add(enemy1)

coin1_x = 130
coin1_y = 240
coin1 = Object(coin_img,coin1_x,coin1_y,0)
items.add(coin1)
all_sprites.add(coin1)


coin2_x = 135
coin2_y = 240
coin2= Object(coin_img,coin2_x,coin2_y,0)
items.add(coin2)
all_sprites.add(coin2)

coin4_x = 120
coin4_y = 240
coin4 = Object(coin_img,coin4_x,coin4_y,0)
items.add(coin4)
all_sprites.add(coin4)

coin3_x = 230
coin3_y = 240
coin3 = Object(coin_img,coin3_x,coin3_y,0)
items.add(coin3)
all_sprites.add(coin3)

#text
coins_font = pygame.font.Font(None,35)
coins_text = coins_font.render("Монеты: 0", True , pygame.Color("red"))

#music
pygame.mixer.music.load('sound/bg.mp3 ')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)

run = True
points = 0

while run:

    if points == 3:
        mb.showinfo("Информация","Вы выиграли!")
        run = False


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

    if len(pygame.sprite.spritecollide(player,walls,False)) > 0:
        player.rect.x = start_x
        player.rect.y = start_y

    # enemy direction 
    enemy1.rect.x += enemy1.speed
    if len(pygame.sprite.spritecollide(enemy1,walls,False)) > 0:
        enemy1.speed *= -1

    # get points
    if len(pygame.sprite.spritecollide(player,items,True)) > 0:
        points += 1
        coins_text = coins_font.render((("Монеты: " + str(points))), True, pygame.Color("red"))
        
    all_sprites.draw(window)
    all_sprites.update()
    window.blit(coins_text,(370,480))

    pygame.display.update()