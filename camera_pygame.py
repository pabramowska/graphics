"""
to do:
-naprawić skalę (zoom)
-dodać obrót wokół osi
-dodać róch do przodu
-róch góra-dół """

import pygame

pygame.init()
surface = pygame.display.set_mode((1200,800))
white = (255,255,255)
black=(0,0,0)
#lokalizacja prostopadłościanów w układzie współrzędnych

locations = [[250,400],[550,400]]
size = [70, 100]
scale = 1

#          !!!!WAŻNE!!!!
#zastanów się nad użyciem skali tu i jak to rozwiązać!

def cube(location, size, scale):

    size_base = size[0]*scale
    size_height = size[1]*scale
    #pierwszy prostokąt
    point_1 = [location[0]*scale, location[1]*scale]
    point_2 = [(location[0]+ size_base), location[1]*scale]
    point_3 = [(location[0])*scale, (location[1]+size_height)*scale]
    point_4 = [(location[0]+ size_base)*scale, (location[1]+size_height)*scale]


    # linie łączące pierwszy prostokąt
    pygame.draw.line(surface, white, (point_1),(point_2))
    pygame.draw.line(surface, white, (point_3),(point_4))
    pygame.draw.line(surface, white, (point_2),(point_4))
    pygame.draw.line(surface, white, (point_1),(point_3))

    #drugi prostokąt
    shift_base = size_base//2
    shift_height = size_height//2

    point_5 = [(point_1[0] + shift_base)*scale, (point_1[1] - shift_height)*scale]
    point_6 = [(point_2[0] + shift_base)*scale, (point_2[1] - shift_height)*scale]
    point_7 = [(point_3[0] + shift_base)*scale, (point_3[1] - shift_height)*scale]
    point_8 = [(point_4[0] + shift_base)*scale, (point_4[1] - shift_height)*scale]


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

y_move = 0
scale_change = 0
current_size = size
z_status = 0
z_location = 1
print(current_size)


while game_on:
    # obsługa klawiatury
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_RIGHT:

                current_status = -0.3
            elif event.key == pygame.K_LEFT:
                current_status = 0.3
            elif event.key == pygame.K_UP:
                y_move = 0.3
            elif event.key == pygame.K_DOWN:
                y_move =-0.3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                current_status= 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_move= 0

    for location in locations:
        location[0] += current_status
        location[1] += y_move
    # scale+=scale_change

    #rysowanie prostopadłościanów
    surface.fill(black)
    cube(locations[0],current_size,scale)
    cube(locations[1], current_size,scale)

    pygame.display.update()
