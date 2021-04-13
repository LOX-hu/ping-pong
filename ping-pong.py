from pygame import *
from random import randint, uniform
from time import time as timer
class GameSprite(sprite.Sprite):
    def _init_(self, player_image, player_x, player_y, w, h, player_speed):
        super()._init_()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.killed = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0: self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 630: self.rect.x += self.speed
        # if keys_pressed[K_SPACE]: player.fire()
    def fire(self):
         bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, uniform(10.0, 15.0))
        bullets.add(bullet)
killed = 0
lost = 0
lives = 3
class Emeny(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed 
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,650)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed 
        if self.rect.y < 0:
            self.kill()

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60

num_fire = 0
rel_time = False

window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player('rocket.png',320, 400, 75, 100, 15)

monsters = sprite.Group()
for _ in range(5):
    monster = Emeny('ufo.png', randint(0,650), 0, 65, 50, randint(1,2))
    monsters.add(monster)

asteroids = sprite.Group()
for _ in range(5):
    asteroid = Emeny('asteroid.png', randint(0,650), 0, 65, 50, randint(1,2))
    asteroids.add(asteroid)

bullets = sprite.Group()

font.init()
font1 = font.SysFont('Arial', 36)

game = True
finish = False           
while game:
    for e in event.get():
        if e.type == QUIT: game = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            if num_fire < 5 and rel_time == False:
                player.fire()
                num_fire = num_fire + 1
            if num_fire >= 5 and rel_time == False:
                rel_time = True
                last_time = timer()       

    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        clock.tick(FPS)
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        bullets.draw(window)
        bullets.update()
        
        lost_text = font1.render(f'Пропущено: {lost}', 1, (255,255,255))
        kill_text = font1.render(f'Убито: {killed}', 1, (255,255,255))
        reload_text = font1.render('ПЕРЕЗАРЯДКА', 1, (255,255,255))
        window.blit(lost_text,(0,0))
        window.blit(kill_text,(0,30))

        sprites_list = sprite.groupcollide(
            monsters, bullets, True, True
        )
        for i in sprites_list:
            killed = killed + 1
            monster = Emeny('ufo.png', randint(0,650), 0, 65, 50, uniform(2.5, 10.0))
            monsters.add(monster)

        sprites_list = sprite.groupcollide(
            asteroids, bullets, False, True
            )

        '''sprites_list = sprite.spritecollide(
            player, asteroids, False, True
            )'''
        
        if len(sprites_list) > 0:
            lives = lives - 1

        if lives == 0:
            finish = True

        if rel_time == True:
            window.blit(reload_text, (250,400))
            now = timer()
            if now - last_time >= 3:
                rel_time = False
                num_fire = 0

    display.update()