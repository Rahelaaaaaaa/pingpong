from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(width, height))
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys [K_DOWN] and self.rect.y < window_height - 80:
            self.rect.x += self.player_speed
    def update_l(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.player_speed
        if keys [K_s] and self.rect.y < window_height - 80:
            self.rect.x += self.player_speed
        
    

back = (200, 255, 255)

window_width = 700
window_height = 600


mw = display.set_mode((window_width, window_height))
mw.fill(back)

platform1 = Player("racket.png", 30, 200, 4, 50, 150)
platformr = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)


clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        mw.fill(back)
        platform1.reset()
        platformr.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)


