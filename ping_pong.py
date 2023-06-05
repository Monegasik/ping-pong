import pygame
import time
from random import randint
 
pygame.init()
 

back = (200, 255, 255) #цвет фона (background)
mw = pygame.display.set_mode((700, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()



#окончание игры
game_over = False
moving_up = False
moving_down = False

ball_x = 3
ball_y = 3

#координаты старта платформы
platform_x1 = 350
platform_y1 = 200

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, width, height) #прямоугольник
        self.fill_color = back
        if color:
            self.fill.color = color

    def color(self, new_color):
        self.fill_color = new_color
 
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
 
    # def collidepoint(self, x, y):
    #     return self.rect.collidepoint(x, y)      

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    def __init__(self, filename, x = 0, y = 0, width = 10, height = 10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    


platform_left = Picture('platform3.png', 100, 100, 50, 50)
platform_right = Picture('platform3.png', 400, 400, 50, 50)

ball = Picture('ball.png', 250, 190, 50, 50)



while not game_over:
    ball.fill()
    platform_left.fill()
    platform_right.fill()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False


#движение платформы
    if moving_down:
        platform.rect.y -= 3

    if moving_up:
        platform.rect.y += 3


# permanent ball moving
    ball.rect.x += ball_x
    ball.rect.y += ball_y

# check borders, change direction if needs
    if ball.rect.y < 0:
        ball_y *= - 1

    if ball.rect.x > 450 or ball.rect.x < 0:
        ball_x *= - 1

# check if ball touch the platform and change direction:
    if (ball.rect.colliderect(platform_left.rect) or 
    ball.rect.colliderect(platform_right.rect)):
        ball_y *= - 1


# draw platform and ball
    platform_left.draw()
    platform_right.draw()
    ball.draw()

    # renew scene
    pygame.display.update()
    clock.tick(40)
