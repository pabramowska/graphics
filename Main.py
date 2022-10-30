import numpy as np
import pygame

width, height = 800, 600
pygame.display.set_caption("Zadanie 1 - wirtualna kamera")
screen = pygame.display.set_mode((width, height))

points = np.matrix('-1,-1,1;1,-1,1;1,1,1;-1,1,1;-1,-1,-1;1,-1,-1;1,1,-1;-1,1,-1')
projection_matrix = np.matrix('1,0,0;0,1,0;0,0,0')
projected_points = [[0,0] for _ in points]
angle = 0


def connect_points(coordinate1,  coordinate2, points):
    pygame.draw.line(screen, (0,0,0),(points[coordinate1][0],points[coordinate1][1]),(points[coordinate2][0],points[coordinate2][1]))

clock = pygame.time.Clock()
while True:
     clock.tick(120)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()

     screen.fill((255,255,255))

    #to jest ze wzorów na obrót wokół osi współrzędnych

     rotation_x = np.matrix([
         [1,0,0],
         [0, np.cos(angle), -np.sin(angle)],
         [0, np.sin(angle), np.cos(angle)]
     ])

     rotation_y = np.matrix([
         [np.cos(angle), 0, np.sin(angle)],
         [0,1,0],
         [-np.sin(angle), 0, np.cos(angle)],
     ])

     rotation_z = np.matrix([
         [np.cos(angle), -np.sin(angle), 0],
         [np.sin(angle), np.cos(angle), 0],
         [0, 0, 1]
     ])

     angle+=0.01

     row = 0
     for point in points:
        #zwykła macierz
        # projection = np.dot(projection_matrix,point.transpose())
        # projection = np.dot(rotation_z,projection)
        # #przekształcenia -> macierz rotacji razy współrzędne
        rotated_z = np.dot(rotation_z, point.transpose())
        rotated_x = np.dot(rotation_x, rotated_z)
        rotated_y = np.dot(rotation_y, rotated_x)
        projection = np.dot(projection_matrix, rotated_y)


        # if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
        #     angle = 50
        #     pygame.event.pump()
                # #przekształcenia -> macierz rotacji razy współrzędne
                # rotated_z = np.dot(rotation_z, point.transpose())
                # rotated_x = np.dot(rotation_x, rotated_z)
                # rotated_y = np.dot(rotation_y, rotated_x)
                # projection = np.dot(projection_matrix, rotated_y)

        #tu się drukują punkty
        x = int(projection[0][0]*100) +width/2
        y = int(projection[1][0]*100) +height/2


        projected_points[row] = [x,y]
        row += 1

#łączenie pierwszego prostokąta
        connect_points(0,1,projected_points)
        connect_points(1, 2, projected_points)
        connect_points(2, 3, projected_points)
        connect_points(3, 0, projected_points)


#rysowanie drugiego prostokąta
        connect_points(4,5,projected_points)
        connect_points(5, 6, projected_points)
        connect_points(6, 7, projected_points)
        connect_points(7, 4, projected_points)
#łączenie podstaw
        connect_points(1,5,projected_points)
        connect_points(3,7,projected_points)
        connect_points(2, 6, projected_points)
        connect_points(0, 4, projected_points)




     pygame.display.update()
