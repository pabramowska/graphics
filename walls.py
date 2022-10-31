import numpy as np
import matplotlib.pyplot as plt
import keyboard

# walls = [[0,0,0,0,0],
#          [0,1,0,1,0],
#          [0,0,0,0,0],
#          [0,1,0,1,0],
#          [0,0,0,0,0]]
walls = [[1,1,1,1,1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,0,0,0,1],
         [1,1,1,1,1]]

for i in range(len(walls[0])):
    for j in range(len(walls[1])):
        if walls[i][j] == 1:
            walls[i][j] = list(np.random.uniform(0,1,3))
posx, posy = 1,1
exitx, exity = 3,3
rot = np.pi/4

while True:
    for i in range(60):
        rot_i = rot + np.deg2rad(i-30)
        x,y = (posx),posy
        while True:
           x, y = (x+0.02*np.cos(rot_i)), (y+0.02*np.sin(rot_i))

           if walls[int(x)][int(y)] != 0:
             dist = np.sqrt((x-posx)**2 + (y-posy)**2)
             h=1/(dist+0.0001)
             #h = np.clip(1/(0.02*n),0,1)
             c = np.asanyarray(walls[int(x)][int(y)])*(0.3*0.7*h**2)
             break
        plt.vlines(i,-h,h,linewidth=8,colors=c)
        plt.axis('off')
        plt.tight_layout()
        plt.axis([0,60,-1.2,1.2])
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

        key = keyboard.read_key()
        x,y = posx, posy

        if key=='up':
            x,y=(x+0.3*np.cos(rot), y+0.3*np.sin(rot))
        elif key=='down':
            x, y = (x - 0.3 * np.cos(rot), y - 0.3 * np.sin(rot))
        elif key=='left':
            rot = rot - np.pi/8
        elif key == "right":
            rot = rot + np.pi/8
        elif key=='esc':
            break



