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
        
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0: self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400: self.rect.y += self.speed
           
 
killed = 0
lost = 0
lives = 3
 

clock = time.Clock()
FPS = 60
 
 

window = display.set_mode((700, 500))
display.set_caption("ping-pong")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player('racket.png',10, 100, 75, 100, 15)
player2 = Player('racket.png',620, 100, 75, 100, 15)
ball = GameSprite('tenis_ball.png', 350 , 250, 40, 40, 2)

speed_y = 3
speed_x = 3  
 

font.init()
font1 = font.SysFont('Arial', 36)
p1lose_text = font1.render('проиграл левый', 1, (255,255,255))
p2lose_text = font1.render('проиграл правый', 1, (255,255,255))
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
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x <= 0 or ball.rect.x >= 700:
            finish = True 
            window.blit(p1lose_text, (250,400))
        if ball.rect.y <= 0 :
            speed_y *= -1     
        if ball.rect.y > 460 :
            speed_y *= -1

        if sprite.collide_rect(ball, player2):
            speed_x *= -1
        if sprite.collide_rect(ball, player):
            speed_x *= -1
        clock.tick(FPS)
        
    display.update()