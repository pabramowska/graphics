import py2exe
import numpy as np
import pygame
import pygame.gfxdraw

pygame.init()
surface_size = (1200,1000)
surface = pygame.display.set_mode(surface_size)



white = (255,255,255)
black = (0,0,0)
blue = (65,105,225)
pink = (255,20,147)
yellow = (255,255,153)
green = (0,255,0)

#współrzędne obiektów
location_first_front = np.array([[519, 600, 1.2], [589, 600,1.2], [519, 700,1.2], [589, 700,1.2],[519, 600, 1.3], [589, 600,1.3], [519, 700,1.3], [589, 700,1.3]])
location_first_back = np.array([[520, 600,1.31], [650, 600,1.31], [520, 650,1.31], [650, 650,1.31], [520, 600,1.5], [650, 600,1.5], [520, 650,1.5], [650, 650,1.5]])
location_second_front = np.array([[709, 600,1.2], [779, 600, 1.2], [709, 700, 1.2], [779, 700, 1.2], [709, 600, 1.3], [779, 600, 1.3], [709, 700, 1.3], [779, 700, 1.3]])
location_second_back = np.array([[710, 600, 1.5], [780, 600, 1.5], [710, 700, 1.5], [780, 700, 1.5], [710, 600, 1.6], [780, 600, 1.6], [710, 700, 1.6], [780, 700, 1.6]])


def multiply_vector_normalized(vector, matrix):
    result_vector = np.matmul(vector,matrix)
    n = result_vector[2]
    if(n!=0):
        result_vector/= n
    return result_vector


def project(coordinates):

        # macierz rzutowania
    z_min = 0.1
    z_max = 1000
    field_of_view =  95
    aspect_ratio = surface_size[1] / surface_size[0]
    field_of_view_rad = 1 / np.tan(np.deg2rad(field_of_view / 2))
    projection_matrix = np.array([[0.0, 0.0, 0.0, 0.0] for _ in range(4)])
    projection_matrix[0][0] = aspect_ratio * field_of_view_rad
    projection_matrix[1][1] = field_of_view_rad
    projection_matrix[2][2] = z_max / (z_max - z_min)
    projection_matrix[2][3] = 1
    projection_matrix[3][2] = (-z_max * z_min) / (z_max - z_min)
    vector_list = []

    for vector in coordinates:
        vector_list.append(multiply_vector_normalized(vector,projection_matrix))
    return np.array(vector_list)


def move(coordinates, x_move, y_move, z_move):
    coordinates[:,0]+=x_move
    coordinates[:,1]+=y_move
    coordinates[:,2]+=z_move
    return coordinates


def scale(coordinates, scalex, scaley):
    coordinates[:,0]*=scalex
    coordinates[:,1]*=scaley
    return coordinates

def rotate(coordinates, theta):
    moy = np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]])
    rotated = []
    for vector in coordinates:
        rotated.append(np.matmul(np.append(vector,1),moy))
    rotated = np.array(rotated)
    return rotated

def draw(coordinates,color):

        #pierwszy prostokąt
    pygame.gfxdraw.filled_polygon(surface,
                                [(coordinates[0][0], coordinates[0][1]), (coordinates[1][0], coordinates[1][1]),
                                (coordinates[3][0], coordinates[3][1]), (coordinates[2][0], coordinates[2][1])],
                                color)
        #drugi prostokąt
    pygame.gfxdraw.filled_polygon(surface,
                                    [(coordinates[4][0], coordinates[4][1]), (coordinates[5][0], coordinates[5][1]),
                                    (coordinates[7][0], coordinates[7][1]), (coordinates[6][0], coordinates[6][1])],
                                    color)

        #boki
    pygame.draw.line(surface, color, (coordinates[0][0], coordinates[0][1]),(coordinates[4][0], coordinates[4][1]))
    pygame.draw.line(surface, color, (coordinates[1][0], coordinates[1][1]), (coordinates[5][0], coordinates[5][1]))
    pygame.draw.line(surface, color, (coordinates[2][0], coordinates[2][1]), (coordinates[6][0], coordinates[6][1]))
    pygame.draw.line(surface, color, (coordinates[3][0], coordinates[3][1]), (coordinates[7][0], coordinates[7][1]))

def draw_transformed(location, x_move, y_move, z_move, x_scale, y_scale,color,theta):
    moved = move(location, x_move, y_move, z_move)
    rotated = rotate(moved, theta)
    projected = project(rotated)
    scaled = scale(projected,x_scale,y_scale)
    draw(scaled, color)

x_move, y_move, z_move = 0,0,0
game_on=True
x_scale,y_scale=1,1
deg = 0


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
            elif event.key == pygame.K_z:
                x_scale += 0.1
                y_scale += 0.1
            elif event.key == pygame.K_x:
                x_scale -= 0.1
                y_scale -= 0.1
            elif event.key == pygame.K_w:
                z_move = -0.0003
            elif event.key == pygame.K_s:
                z_move = 0.0003
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_move = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_move = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                z_move = 0
            if event.key == pygame.K_z or event.key == pygame.K_x:
                pass

    surface.fill(black)
    draw_transformed(location_first_front, x_move, y_move, z_move, x_scale, y_scale, pink,deg)
    draw_transformed(location_first_back, x_move, y_move, z_move, x_scale, y_scale, blue,deg)
    draw_transformed(location_second_front, x_move, y_move, z_move, x_scale, y_scale, yellow,deg)
    draw_transformed(location_second_back, x_move, y_move, z_move, x_scale, y_scale, green,deg)
    pygame.display.update()

