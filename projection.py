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
camera_location = np.array([0,0,0])
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

def normalize(vector):
    return vector/len(vector)

def matrix_point_at(pos, target, up):
    #kierunek do przodu
    new_froward = target-pos
    new_froward = normalize(new_froward)

    #kierunek do góry
    a = new_froward * sum(up*new_froward)
    new_up = up - a
    new_up = normalize(new_up)

    #kierunek w prawo
    new_right = np.cross(new_up, new_froward)

    #macierz kierunkowa
    dimension_matrix = np.array([0.0,0.0,0.0] for _ in range(4))
    dimension_matrix[0][0] = new_right[0]
    dimension_matrix[0][1] = new_right[1]
    dimension_matrix[0][2] = new_right[2]
    dimension_matrix[0][3] = 0.0
    dimension_matrix[1][0] = new_up[0]
    dimension_matrix[1][1] = new_up[1]
    dimension_matrix[1][2] = new_up[2]
    dimension_matrix[1][3] = 0.0
    dimension_matrix[2][0] = new_froward[0]
    dimension_matrix[2][1] = new_froward[1]
    dimension_matrix[2][2] = new_froward[2]
    dimension_matrix[2][3] = 0.0
    dimension_matrix[3][0] = pos[0]
    dimension_matrix[3][1] = pos[1]
    dimension_matrix[3][2] = pos[2]
    dimension_matrix[3][3] = 0.0

    return dimension_matrix

def inverse(matrix):
    new_matrix = np.array([0.0,0.0,0.0] for _ in range(4))
    new_matrix[0][0] = matrix[0][0]
    new_matrix[0][1] = matrix[1][0]
    new_matrix[0][2] = matrix[2][0]
    new_matrix[0][3] = 0.0
    
    new_matrix[1][0] = matrix[0][1]
    new_matrix[1][1] = matrix[1][1]
    new_matrix[1][2] = matrix[2][1]
    new_matrix[1][3] = 0.0
    
    new_matrix[2][0] = matrix[0][2]
    new_matrix[2][1] = matrix[1][2]
    new_matrix[2][2] = matrix[2][2]
    new_matrix[2][3] = 0.0
    
    new_matrix[3][0] = -(matrix[3][0] * new_matrix[0][0] + matrix[3][1] * new_matrix[1][0] + matrix[3][2] * new_matrix[2][0])
    new_matrix[3][1] = -(matrix[3][0] * new_matrix[0][1] + matrix[3][1] * new_matrix[1][1] + matrix[3][2] * new_matrix[2][1])
    new_matrix[3][2] = -(matrix[3][0] * new_matrix[0][2] + matrix[3][1] * new_matrix[1][2] + matrix[3][2] * new_matrix[2][2])
    new_matrix[3][3] = 1.0

    return new_matrix


def multiply_vector_normalized(vector, matrix):
    result_vecor = np.array([0.0,0.0,0.0])
    result_vecor[0] = (vector[0]*matrix[0][0]) + (vector[1]*matrix[1][0]) + (vector[2]*matrix[2][0])+ (matrix[3][0])
    result_vecor[1] = vector[0] * matrix[0][1] + vector[1] * matrix[1][1] + vector[2] * matrix[2][1] + matrix[3][1]
    result_vecor[2] = vector[0] * matrix[0][2] + vector[1] * matrix[1][2] + vector[2] * matrix[2][2] + matrix[3][2]
    n = vector[0] * matrix[0][3] + vector[1] * matrix[1][3] + vector[2] * matrix[2][3] + matrix[3][3]
    if(n!=0):
        result_vecor/=n
    return result_vecor


def vector_matrix_multiply(vector, matrix):
    result_vecor = np.array([0.0,0.0,0.0])
    result_vecor[0] = (vector[0]*matrix[0][0]) + (vector[1]*matrix[1][0]) + (vector[2]*matrix[2][0])+ (matrix[3][0])
    result_vecor[1] = vector[0] * matrix[0][1] + vector[1] * matrix[1][1] + vector[2] * matrix[2][1] + matrix[3][1]
    result_vecor[2] = vector[0] * matrix[0][2] + vector[1] * matrix[1][2] + vector[2] * matrix[2][2] + matrix[3][2]
    n = vector[0] * matrix[0][3] + vector[1] * matrix[1][3] + vector[2] * matrix[2][3] + matrix[3][3]
    return result_vecor


def project(coordinates):
    vector_list = []
    for vector in coordinates:
        vector_list.append(multiply_vector_normalized(vector,projection_matrix))
    return np.array(vector_list)


def move(coordinates, x_move, y_move):
    for vector in coordinates:
        vector[0]+=x_move
        vector[1]+=y_move
    return coordinates


def rotate_ox_matrix(theta):
    matrix = np.array([[0.0,0.0,0.0,0.0] for _ in range(4)])
    matrix[0][0] = 1.0
    matrix[1][1] = np.cos(theta)
    matrix[1][2] = np.sin(theta)
    matrix[2][1] = -np.sin(theta)
    matrix[2][2] = np.cos(theta)
    matrix[3][3] = 1.0

    return matrix

def rotate_oy_matrix(theta):
    matrix = np.array([[0.0, 0.0, 0.0, 0.0] for _ in range(4)])
    matrix[0][0] = 1.0
    matrix[1][1] = np.cos(theta)
    matrix[1][2] = np.sin(theta)
    matrix[2][1] = -np.sin(theta)
    matrix[2][2] = np.cos(theta)
    matrix[3][3] = 1.0

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


x_move, y_move, z_move = 0,0,0
rot_x=0
game_on=True


look_direction = np.array([0,0,1])
up = np.array([0,1,0])
target = camera_location+look_direction
camera_matrix = matrix_point_at(camera_location, target, up)
camera_view = inverse(camera_matrix)
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
            elif event.key == pygame.K_LESS:
                rot_x += 100
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_move = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_move = 0

    moved_first = move(location_first, x_move, y_move)
    moved_second = move(location_second, x_move, y_move)
    location_first_projected = project(moved_first)
    location_second_projected = project(moved_second)
    surface.fill(black)
    draw(location_first_projected,pink)
    draw(location_second_projected, blue)
    pygame.display.update()