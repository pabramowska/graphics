import numpy as np

surface_size = (1200,800)
pygame.init()
surface = pygame.display.set_mode(surface_size)
white = (255,255,255)
black=(0,0,0)
blue = (65,105,225)
pink = (255,20,147)
locations = [[250,400],[550,400]]
#projection matrix
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
projection_matrix[3][2] =  (-far*near)/(far-near)
print(projection_matrix)