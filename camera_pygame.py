import pygame

pygame.init()
surface = pygame.display.set_mode((800,600))
white = (255,255,255)


def cube(start, size_base, size_height):

    #pierwszy prostokąt
    point_1 = [start[0], start[1]]
    point_2 = [start[0]+ size_base, start[1]]
    point_3 = [start[0], start[1]+size_height]
    point_4 = [start[0]+ size_base, start[1]+size_height]

    # linie łączące pierwszy prostokąt
    pygame.draw.line(surface, white, (point_1),(point_2))
    pygame.draw.line(surface, white, (point_3),(point_4))
    pygame.draw.line(surface, white, (point_2),(point_4))
    pygame.draw.line(surface, white, (point_1),(point_3))

    #drugi prostokąt
    shift_base = size_base//2
    shift_height = size_height//2
    point_5 = [point_1[0] + shift_base, point_1[1] - shift_height]
    point_6 = [point_2[0] + shift_base, point_2[1] - shift_height]
    point_7 = [point_3[0] + shift_base, point_3[1] - shift_height]
    point_8 = [point_4[0] + shift_base, point_4[1] - shift_height]

    #linie łączące pierwszy prostokąt
    pygame.draw.line(surface, white, (point_5),(point_6))
    pygame.draw.line(surface, white, (point_7),(point_8))
    pygame.draw.line(surface, white, (point_6),(point_8))
    pygame.draw.line(surface, white, (point_5),(point_7))

    #łączenie prostokątów
    pygame.draw.line(surface, white, (point_1),(point_5))
    pygame.draw.line(surface, white, (point_2),(point_6))
    pygame.draw.line(surface, white, (point_3),(point_7))
    pygame.draw.line(surface, white, (point_4),(point_8))

cube([250,225],70,100)
cube([50,200],70,100)

game_on=True
while game_on:
    for event in pygame.event.get():
        #sychodzenie z programu
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False

    pygame.display.update()