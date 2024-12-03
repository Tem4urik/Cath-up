from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')
#задай фон сцены
background = transform.scale(image.load('Yellow.png'),(700,500))
x1 = 100
y1 = 300
x2 = 300
y2 = 300
x3 = 200
y3 = 300
sprite1 = transform.scale(image.load('sprite1.png'),(100, 100))
sprite2 = transform.scale(image.load('sprite2.png'),(100, 100))
sprite3 = transform.scale(image.load('Undertale.png'),(100, 100))
speed = 10

game = True
clock = time.Clock()
FPS = 60

while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x2, y2))
    window.blit(sprite2,(x1, y1))
    window.blit(sprite3,(x3, y3))
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 >5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 >5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed

    if keys_pressed[K_h] and x3 >5:
        x3 -= speed
    if keys_pressed[K_k] and x3 < 595:
        x3 += speed
    if keys_pressed[K_u] and y3 > 5:
        y3 -= speed
    if keys_pressed[K_j] and y3 < 395:
        y3 += speed

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)