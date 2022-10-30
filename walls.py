import numpy as np
import matplotlib.pyplot as plt
import keyboard

walls = [[0,0,0,0,0],
         [0,1,0,1,0],
         [0,0,0,0,0],
         [0,1,0,1,0],
         [0,0,0,0,0]]

posx, posy = 0,0
rot = np.pi/4

for i in range(60):
    rot_i = rot + np.deg2rad(i-30)
    x,y = posx,posy
    sin, cos = (0.02*np.sin(rot_i)), (0.02*np.cos(rot_i))
    n = 0
    while True:
       x, y = x+cos, y+sin
       n +=1
       if walls[int(x)][int(y)] != 0:
         h = 1/(0.02 *n)
         break
    plt.vlines(i,-h,h,linewidth=8)
    plt.axis('off')
    plt.tight_layout()
    plt.axis([0,60,-1,2])
    plt.draw()
    plt.pause(0.0001)



plt.close()