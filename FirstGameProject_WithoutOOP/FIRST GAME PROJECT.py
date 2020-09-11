import pygame
pygame.init()

win = pygame.display.set_mode((430,336))

pygame.display.set_caption("FIRST GAME PROJECT")

walkRight = [pygame.image.load('rr0.png'), pygame.image.load('rr1.png'), pygame.image.load('rr2.png'), pygame.image.load('rr3.png') ,pygame.image.load('rr4.png') ,pygame.image.load('rr5.png')]
walkLeft = [pygame.image.load('rl0.png'), pygame.image.load('rl1.png'), pygame.image.load('rl2.png') ,pygame.image.load('rl3.png') ,pygame.image.load('rl4.png') ,pygame.image.load('rl5.png')]
bg = pygame.image.load('bg.png')
idle = [pygame.image.load('idle1.png'), pygame.image.load('idle2.png'), pygame.image.load('idle3.png')]
jump = [pygame.image.load('j0.png'), pygame.image.load('j1.png'), pygame.image.load('j2.png')]

clock = pygame.time.Clock()

x = 50
y = 280
width = 50
height = 37
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
jumpDrawCheck = False
walkCount = 0
idleCount = 0
jumpDrawCount = 0

def redrawGameWindow():
    global walkCount
    global idleCount
    global jumpDrawCount
    win.blit(bg, (0, 0))

    if walkCount +1 > 36:
        walkCount = 0
    if idleCount +1 > 36:
        idleCount = 0
    if jumpDrawCount +1 > 36:
        jumpDrawCount = 0
    if left:
        win.blit(walkLeft[walkCount//6], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//6], (x, y))
        walkCount += 1
    elif jumpDrawCheck:
        win.blit(jump[jumpDrawCount//12], (x, y))
        jumpDrawCount += 1
    else:
        win.blit(idle[idleCount//12], (x, y))
        idleCount += 1
        walkCount = 0

    pygame.display.update()

#mainloop
run = True
while run:
    clock.tick(36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
        jumpDrawCheck = False

    elif keys[pygame.K_RIGHT] and x < 300:
        x += vel
        left = False
        right = True
        jumpDrawCheck = False
    else:
        right = False
        left = False
        jumpDrawCheck = False
        walkCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    if isJump:
        jumpDrawCheck = True
        if jumpCount >= -10:
            neg = 1
            if jumpCount <= 0:
                neg = -1
            y -= (jumpCount ** 2) /3 * neg # /value this decrease the flight height
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()
