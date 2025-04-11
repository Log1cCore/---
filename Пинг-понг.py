from pygame import*
window = display.set_mode((900, 900))
display.set_caption('Ping-Pong')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 695:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 695:
            self.rect.y += self.speed        

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.direction = 'right'
        self.direction1 = 'up'
    def update(self):
        if sprite.collide_rect(ball, racket1):
            self.direction = 'right'
        if sprite.collide_rect(ball, racket2):
            self.direction = 'left'
        if self.rect.y >= 850:
            self.direction1 = 'up'
        if self.rect.y <= 0:
            self.direction1 = 'down'
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        if self.direction1 == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

racket1 = Player('racket.png', 50, 350, 4, 40, 200)
racket2 = Player('racket.png', 840, 350, 4, 40, 200)
ball = Enemy('ball.png', 450, 450, 3, 50, 50)

font.init()
win = font.Font(None, 70)

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((179, 166, 226))

    if ball.rect.x >= 850:
        win_text = win.render('Левый игрок выиграл!', True, (255, 41, 79))
        window.blit(win_text, (250, 400))
        finish = True
    if ball.rect.x <= 0:
        win_text = win.render('Правый игрок выиграл!', True, (255, 41, 79))
        window.blit(win_text, (250, 400))
        finish = True

    
    racket1.reset()
    racket2.reset()
    ball.reset()

    if not finish:
        racket1.update_l()
        racket2.update_r()
        ball.update()

    display.update()
    clock.tick(FPS)
