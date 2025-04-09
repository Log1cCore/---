from pygame import*
window = display.set_mode((900, 900))
display.set_caption('Ping-Pong')

game = True
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((179, 166, 226))
    display.update()
    clock.tick(FPS)