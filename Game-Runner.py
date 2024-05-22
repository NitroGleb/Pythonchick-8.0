from pygame import *
from pygame.sprite import *



#events = event.get()
#event[0].type
win_width = 700
win_height = 500
font.init()
font1 = font.Font(None,80)
font2 = font.Font(None, 80)
win = font1.render('ПОБЕДА',1,(10,20,120))
lose = font2.render('ПОРАЖЕНИЕ',1,(10,20,120))
window = display.set_mode((win_width,win_height))
display.set_caption('ИГРА')
background = transform.scale(image.load('ШАХМАТЫ.jpg'),(win_width,win_height))
sprite1 = transform.scale(image.load('Mario.png'),(100,100))


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,window):
        super().__init__()
        self.window = window
        self.image = transform.scale(image.load(player_image),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reflect(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'down'
    up = True
    down = False
    def update(self):
        #while final != True:
            #self.up = True
            #self.down = False
            #self.direction = 'up'

            if self.rect.y > 430:
                self.rect.y = self.rect.y - 220
                self.up = False
                self.down = True
                self.direction = 'down'

            if self.rect.y > 210:
                self.direction = 'up'
                self.rect.y = self.rect.y + 3
                self.up = True
                self.down = False
            
            
                
            
            #if self.up:
                #self.rect.y -= self.speed
            #elif self.down:
                #self.rect.y += self.speed
            #return self.rect.y
#self.rect.y == 'top'

            
    


        
class Wall(sprite.Sprite):
    def __init__(self,color,width,height,player_x2,player_y2,window):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = player_x2
        self.rect.y = player_y2
        self.window = window
    def draw_wall(self):
        self.window.blit(self.image,(self.rect.x,self.rect.y))

game = True
final = False
FPS = 60
clock = time.Clock()

mixer.init()
mixer.music.load('star-wars-imperial-march.mp3')
mixer.music.play()
YELLOW = (255,255,0)
player = Player('Mario.png',5,400,5,window)
monster = Enemy('Enemy.jpeg',550,350,1,window)
finish = GameSprite('Mario.png',620,350,0,window)
waller = Wall(YELLOW,50,400,80,100,window)
waller_2 = Wall(YELLOW,200,50,80,100,window)
waller_3 = Wall(YELLOW,350,50,350,150,window)
waller_4 = Wall(YELLOW,50,270,350,150,window)
waller_5 = Wall(YELLOW,200,50,200,250,window)
waller_6 = Wall(YELLOW,170,50,100,380,window)
waller_7 = Wall(YELLOW,50,400,480,300,window)

wallers = sprite.Group(waller,waller_2,waller_3,waller_4,waller_5,waller_6,waller_7)
monsters = sprite.Group(monster)
finisher = sprite.Group(finish)
# wall_8 = Wall()
# wall_9 = Wall()
# wall_10 = Wall()


while game:
    window.blit(background,(0,0))
    for a in event.get():
        if a.type == QUIT:
            game = False

    if sprite.spritecollide(player,wallers,False):
        window.blit(lose, (0,0))
        final = True

    if sprite.spritecollide(player,monsters,False):
        window.blit(lose, (0,0))
        final = True

    if sprite.spritecollide(player,finisher,False):
        window.blit(win, (0,0))
        final = True
    


    if final != True:
        window.blit(background,(0,0))
        player.update()
        monster.update()
        #monster.update2()

        player.reflect()
        monster.reflect()
        waller.draw_wall()
        waller_2.draw_wall()
        waller_3.draw_wall()
        waller_4.draw_wall()
        waller_5.draw_wall()
        waller_6.draw_wall()
        waller_7.draw_wall()
        finish.reflect()

    clock.tick(FPS)
    display.update()
