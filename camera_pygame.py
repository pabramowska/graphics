import pygame

pygame.init()
surface = pygame.display.set_mode((1200,800))
white = (255,255,255)
black=(0,0,0)
#lokalizacja prostopadłościanów w układzie współrzędnych
locations = [[250,425],[50,400]]


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



game_on=True
current_status=0

while game_on:
    # obsługa klawiatury
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_RIGHT:
                current_status = -1
            elif event.key == pygame.K_LEFT:
                current_status = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                current_status = 0

    for location in locations:
        location[0] += current_status

    #rysowanie prostopadłościanów
    surface.fill(black)
    cube(locations[0], 70, 100)
    cube(locations[1], 70, 100)
    pygame.display.update()
