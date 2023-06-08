from pygame import *

black = (0, 0, 0)
white = (24, 217, 175)
clock = time.Clock()
FPS=60
font.init()
font1 = font.SysFont('Arial', 80)
win1 = font1.render('LEFT WIN!', True, black)
win2 = font1.render('RIGHT WIN!', True, black)

win_width = 1000
win_height = 700
screen = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")

#background = transform.scale(image.load(white), (win_width, win_height))

#Определение начальных координат мяча и ракеток
ball_x = win_width // 2
ball_y = win_height // 2
ball_speed_x = 10
ball_speed_y = 10

rocket1_x = 50
rocket1_y = win_height // 2 - 55
rocket2_x = win_width - 80
rocket2_y = win_height // 2 - 55
rocket_speed = 5

#Цикл игры
game = True
win = False
while game:
    screen.fill(white)
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not win:
            # screen.fill(white)

        # Обработка движения ракеток
        keys = key.get_pressed()
        if keys[K_w] and rocket1_y > 0:
            rocket1_y -= rocket_speed
        if keys[K_s] and rocket1_y < win_height - 100:
            rocket1_y += rocket_speed
        if keys[K_UP] and rocket2_y > 0:
            rocket2_y -= rocket_speed
        if keys[K_DOWN] and rocket2_y < win_height - 100:
            rocket2_y += rocket_speed

        # Обработка движения мяча
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        if ball_x < 0 or ball_x > win_width - 20:
            ball_speed_x = -ball_speed_x
        if ball_y < 0 or ball_y > win_height - 20:
            ball_speed_y = -ball_speed_y

        # Обработка столкновения мяча с ракетками
        if ball_x < rocket1_x + 20 and rocket1_y < ball_y < rocket1_y + 100:
            ball_speed_x = -ball_speed_x

        if ball_x > rocket2_x - 20 and rocket2_y < ball_y < rocket2_y + 100:
            ball_speed_x = -ball_speed_x

        if ball_x < 50:
            screen.blit(win1,(400, 200))
            win = True



        if ball_x > 950:
            screen.blit(win2,(400, 200))
            win = True

# Отрисовка объектов на экране
        draw.rect(screen, black, (rocket1_x, rocket1_y, 30, 120))
        draw.rect(screen, black, (rocket2_x, rocket2_y, 30, 120))
        draw.ellipse(screen, black, (ball_x, ball_y, 28, 28))
        display.update()
    clock.tick(FPS)
