import pygame

pygame.init()
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)

screen2 = pygame.Surface((40, 40))
pygame.draw.circle(screen2, pygame.Color("green"), (20, 20), 20, 0)
k = [0, 0]
running = True
coords = [[0, 0], [0, 0]]
sc2_pos = [0, 0]
clock = pygame.time.Clock()


def move_circle(k):
    tol = 0.3
    beta = 0.7
    sc2_pos[0] += k[0]
    sc2_pos[1] += k[1]
    # print(sc2_pos)
    if (sc2_pos[0] < 0 and k[0] < 0) or (sc2_pos[0] + 40 > width and k[0] > 0):
        k[0] *= -beta
    if (sc2_pos[1] < 0 and k[1] < 0) or (sc2_pos[1] + 40 > height and k[1] > 0):
        k[1] *= -beta
    k[0] = 0 if (abs(k[0]) < tol) else k[0]
    k[1] = 0 if (abs(k[1]) < tol and sc2_pos[1] + 41 > height) else k[1]
    screen.blit(screen2, (sc2_pos[0], sc2_pos[1]))
    # print(k)
    # print('--------------------------------------------')


while running:

    x_speed_tol = 1e-1

    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            k = [(coords[1][0] - coords[0][0]), (coords[1][1] - coords[0][1])]
    screen.fill((0, 0, 0))

    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    falling_acceleration = 0.15

    if sc2_pos[1] + 43 < height:
        k[1] += falling_acceleration
    if abs(k[0]) > x_speed_tol:
        k[0] -= 0.0025*k[0]/abs(k[0])

    if pressed[0]:
        screen.blit(screen2, (pos[0] - 20, pos[1] - 20))
        sc2_pos = [pos[0] - 20, pos[1] - 20]
    else:
        move_circle(k)

    

    coords[0], coords[1] = coords[1], pygame.mouse.get_pos()

    pygame.display.flip()
