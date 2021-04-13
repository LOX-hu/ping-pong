from pygame import *
from random import randint, uniform
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.killed = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0: self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400: self.rect.y += self.speed
        # if keys_pressed[K_SPACE]: player.fire()
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0: self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400: self.rect.y += self.speed
        # if keys_pressed[K_SPACE]: player.fire()    
 
killed = 0
lost = 0
lives = 3
# class Emeny(GameSprite):
#     def update(self):
#         global lost
#         self.rect.y += self.speed 
#         if self.rect.y > 500:
#             self.rect.y = 0
#             self.rect.x = randint(0,650)
#             lost += 1

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed 
#         if self.rect.y < 0:
#             self.kill()

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()

clock = time.Clock()
FPS = 60

 

window = display.set_mode((700, 500))
display.set_caption("ping-pong")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player('racket.png',10, 100, 75, 100, 15)
player2 = Player('racket.png',620, 100, 75, 100, 15)

  
 

font.init()
font1 = font.SysFont('Arial', 36)

game = True
finish = False           
while game:
    for e in event.get():
        if e.type == QUIT: game = False
         
                   

    if finish != True:
        window.fill((0,255,0))
        player.reset()
        player.update_right()
        player2.reset()
        player2.update_left()
        clock.tick(FPS)
        
        # lost_text = font1.render(f'Пропущено: {lost}', 1, (255,255,255))
        # kill_text = font1.render(f'Убито: {killed}', 1, (255,255,255))
        # reload_text = font1.render('ПЕРЕЗАРЯДКА', 1, (255,255,255))
        # window.blit(lost_text,(0,0))
        # window.blit(kill_text,(0,30))

    

    display.update()