import numpy as np
import pygame

pygame.init()
surface_size = (1200,800)
surface = pygame.display.set_mode(surface_size)

white = (255,255,255)
black = (0,0,0)
blue = (65,105,225)
pink = (255,20,147)

#współrzędne obiektów
location_first = np.array([[550, 400, 0], [620, 400,0], [550, 500,0], [620, 500,0],[550, 400, 1.1], [620, 400,1.1], [550, 500,1.1], [620, 500,1.1]])
location_second = np.array([[250, 400, 0], [320, 400, 0], [250, 500, 0], [320, 500, 0], [250, 400, 1.1], [320, 400, 1.1], [250, 500, 1.1], [320, 500, 1.1]])

#macierz rzutowania
z_min = 0.1
z_max = 1000
field_of_view = 90
aspect_ratio = surface_size[1]/surface_size[0]
field_of_view_rad = 1/np.tan(np.deg2rad(field_of_view/2))
projection_matrix = np.array([[0.0,0.0,0.0,0.0] for _ in range(4)])
projection_matrix[0][0] = aspect_ratio * field_of_view_rad
projection_matrix[1][1] = field_of_view_rad
projection_matrix[2][2] = z_max/(z_max-z_min)
projection_matrix[2][3] = 1
projection_matrix[3][2] = (-z_max*z_min)/(z_max-z_min)

def multiply_vector(vector, matrix):
    result_vecor = np.array([0.0,0.0,0.0])
    result_vecor[0] = (vector[0]*matrix[0][0]) + (vector[1]*matrix[1][0]) + (vector[2]*matrix[2][0])+ (matrix[3][0])
    result_vecor[1] = vector[0] * matrix[0][1] + vector[1] * matrix[1][1] + vector[2] * matrix[2][1] + matrix[3][1]
    result_vecor[2] = vector[0] * matrix[0][2] + vector[1] * matrix[1][2] + vector[2] * matrix[2][2] + matrix[3][2]
    n = vector[0] * matrix[0][3] + vector[1] * matrix[1][3] + vector[2] * matrix[2][3] + matrix[3][3]

    if(n!=0):
        result_vecor /= n
    return result_vecor


def project(coordinates):
    vector_list = []
    for vector in coordinates:
        vector_list.append(multiply_vector(vector,projection_matrix))
    return np.array(vector_list)


def move(coordinates, x_move, y_move):
    for vector in coordinates:
        vector[0]+=x_move
        vector[1]+=y_move
    return coordinates

def draw(coordinates,color):

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

location_first_projected = project(location_first)
location_second_projected = project(location_second)
x_move, y_move, z_move = 0,0,0
game_on=True

while game_on:

    # obsługa klawiatury
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_RIGHT:
                x_move = -1
            elif event.key == pygame.K_LEFT:
                x_move = 1
            elif event.key == pygame.K_UP:
                y_move = 1
            elif event.key == pygame.K_DOWN:
                y_move = -1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_move = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_move = 0

    moved_first = move(location_first_projected, x_move, y_move)
    moved_second = move(location_second_projected, x_move, y_move)

    surface.fill(black)
    draw(moved_first,pink)
    draw(moved_second, blue)
    pygame.display.update()