import numpy as np
import pygame

pygame.init()
surface_size = (1200,800)
surface = pygame.display.set_mode(surface_size)

white = (255,255,255)
black=(0,0,0)
blue = (65,105,225)
pink = (255,20,147)

#współrzędne obiektów
location_first = np.array([[550, 400, 100], [620, 400,100], [550, 500,100], [620, 500,100],[550, 400, 100], [620, 400,100], [550, 500,100], [620, 500,100]])
location_second = np.array([[250, 400, 100], [320, 400, 100], [250, 500, 100], [320, 500, 100], [250, 400, 0], [320, 400, 0], [250, 500, 0], [320, 500, 0]])

#macierz rzutowania
near = 0.1
far = 1000
field_of_view = 90
aspect_ratio = surface_size[1]/surface_size[0]
field_of_view_rad = 1/np.tan(np.deg2rad(field_of_view/2))
projection_matrix = np.array([[0.0,0.0,0.0,0.0] for _ in range(4)])
projection_matrix[0][0] = aspect_ratio * field_of_view_rad
projection_matrix[1][1] = field_of_view_rad
projection_matrix[2][2] = far/(far-near)
projection_matrix[2][3] = 1
projection_matrix[3][2] = (-far*near)/(far-near)

def multiplyVector(vector, matrix):

    result_vecor = np.array([0,0,0])
    result_vecor[0] = vector[0]*matrix[0][0] + vector[1]*matrix[1][0] + vector[2]*matrix[2][0]+ matrix[3][0]
    result_vecor[1] = vector[0] * matrix[0][1] + vector[1] * matrix[1][1] + vector[2] * matrix[2][1] + matrix[3][1]
    result_vecor[2] = vector[0] * matrix[0][2] + vector[1] * matrix[1][2] + vector[2] * matrix[2][2] + matrix[3][2]
    n = vector[0] * matrix[0][3] + vector[1] * matrix[1][3] + vector[2] * matrix[2][3] + matrix[3][3]

    if(n!=0):
        result_vecor[0] /= n
        result_vecor[1] /= n
        result_vecor[2] /= n

    return result_vecor


def drawObject(coordinates,color):

    #pierwszy prostokąt
    pygame.draw.line(surface, color, (coordinates[0][0], coordinates[0][1]),(coordinates[1][0], coordinates[1][1]))
    pygame.draw.line(surface, color, (coordinates[1][0], coordinates[1][1]), (coordinates[3][0], coordinates[3][1]))
    pygame.draw.line(surface, color, (coordinates[2][0], coordinates[2][1]), (coordinates[3][0], coordinates[3][1]))
    pygame.draw.line(surface, color, (coordinates[0][0], coordinates[0][1]), (coordinates[2][0], coordinates[2][1]))

    #drugi prostokąt
    pygame.draw.line(surface, color, (coordinates[4][0], coordinates[4][1]),(coordinates[5][0], coordinates[5][1]))
    pygame.draw.line(surface, color, (coordinates[6][0], coordinates[6][1]), (coordinates[7][0], coordinates[7][1]))
    pygame.draw.line(surface, color, (coordinates[5][0], coordinates[5][1]), (coordinates[7][0], coordinates[7][1]))
    pygame.draw.line(surface, color, (coordinates[4][0], coordinates[4][1]), (coordinates[6][0], coordinates[6][1]))

    #boki
    pygame.draw.line(surface, color, (coordinates[0][0], coordinates[0][1]),(coordinates[4][0], coordinates[4][1]))
    pygame.draw.line(surface, color, (coordinates[1][0], coordinates[1][1]), (coordinates[5][0], coordinates[5][1]))
    pygame.draw.line(surface, color, (coordinates[2][0], coordinates[2][1]), (coordinates[6][0], coordinates[6][1]))
    pygame.draw.line(surface, color, (coordinates[3][0], coordinates[3][1]), (coordinates[7][0], coordinates[7][1]))

game_on=True
while game_on:
    # obsługa klawiatury
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
    surface.fill(black)
    drawObject(location_first,pink)
    drawObject(location_second, blue)
    pygame.display.update()