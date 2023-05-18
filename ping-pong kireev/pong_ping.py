#Создай собственный Шутер!
from random import randint 
from pygame import *
#парпметры окно 
display.set_caption("SpaceWar")
img_back = "nebo.png" 
img_hero = "floppa_one.png"
img_enemy = "pelmen.png" 
img_hero2 = "floppa_two.png"
window = display.set_mode((700, 500))
background = transform.scale(image.load(img_back), (700, 500))

#класс GameSprite
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
          sprite.Sprite.__init__(self)
          self.image = transform.scale(image.load(player_image), (size_x, size_y))
          self.speed = player_speed
          self.rect = self.image.get_rect()
          self.rect.x = player_x
          self.rect.y = player_y
     def reset(self):
          window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
     def update(self):
          keys = key.get_pressed()
          if keys[K_UP] and self.rect.y > 5:
               self.rect.y -= self.speed
          if keys[K_DOWN] and self.rect.y < 700 - 80:
               self.rect.y += self.speed
class Player_2(GameSprite):
     def update(self):
          keys = key.get_pressed()
          if keys[K_w] and self.rect.y > 5:
               self.rect.y -= self.speed
          if keys[K_s] and self.rect.y < 700 - 80:
               self.rect.y += self.speed


               
packman = Player(img_hero, 5, 500 - 300, 80 ,100, 10)
packman2 = Player_2(img_hero, 600, 500 - 300, 80 ,100, 10)
monster = Player(img_enemy, 200, 250, 80, 80, 2 )

clock = time.Clock()
FPS=60

finish=False
game=True

speed_x = 3
speed_y = 3

while game:
     for e in event.get():
          if e.type == QUIT:
               game = False 


                    
     if finish != True:
          window.blit(background,(0,0))

          packman.reset()
          packman.update()

          packman2.reset()
          packman2.update()

          monster.reset()
          monster.rect.x += speed_x
          monster.rect.y += speed_y

     if monster.rect.y > 500-50 or monster.rect.y < 0 :
          speed_y *= -1 

     elif monster.rect.x > 700-50 or monster.rect.x < 0 :
          speed_x *= -1 

     if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman2, monster):
          speed_x *= -1


     clock.tick(FPS)
     display.update()