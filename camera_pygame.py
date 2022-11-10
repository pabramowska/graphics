import pygame

# pygame.init()
#
surface = pygame.display.set_mode((800,600))
white = (255,255,255)
#
# color = (255,0,0)
# pygame.draw.rect(surface, color, pygame.Rect(20,30,60,90))

def cube(start, size):
    #pierwszy prostokąt
    point_1 = [start[0], start[1]]
    point_2 = [start[0]+ size, start[1]]
    point_3 = [start[0], start[1]+size]
    point_4 = [start[0]+ size, start[1]+size]

    # linie łączące pierwszy prostokąt
    pygame.draw.line(surface, white, (point_1),(point_2))
    pygame.draw.line(surface, white, (point_3),(point_4))
    pygame.draw.line(surface, white, (point_2),(point_4))
    pygame.draw.line(surface, white, (point_1),(point_3))

    #drugi prostokąt
    shift = size//2
    point_5 = [point_1[0] + shift, point_1[1] - shift]
    point_6 = [point_2[0] + shift, point_2[1] - shift]
    point_7 = [point_3[0] + shift, point_3[1] - shift]
    point_8 = [point_4[0] + shift, point_4[1] - shift]

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

cube([250,225],100)
cube([50,200],100)

while True:
    pygame.display.flip()