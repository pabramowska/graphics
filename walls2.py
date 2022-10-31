import numpy as np
from matplotlib import pyplot as plt
import keyboard

mapa = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 2, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 2, 0, 2, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(len(mapa)):
    for j in range(len(mapa)):
        if mapa[i][j] == 1:
            mapa[i][j] = list(np.random.uniform(0, 1, 3))

posx, posy, rot = 1.5, 1.5, np.pi / 4


while 1:

    plt.hlines(-0.6, 0, 60, colors='gray', lw=180,alpha=0.8)
    plt.hlines(0.6, 0, 60, colors='lightblue', lw=180)
    for i in range(60):
        rot_i = rot + np.deg2rad(i - 30)
        x, y = posx, posy
        sin, cos = 0.02 * np.sin(rot_i), 0.02 * np.cos(rot_i)
        n = 0

        while 1:
            x, y, n = x + cos, y + sin, n + 1

            if mapa[int(x)][int(y)]:
                h = np.clip(1 / (0.02 * n), 0, 1)
                c = "gray"
                if mapa[int(x)][int(y)]==2:
                    c="black"
                break

        plt.vlines(i, -h, h, lw=8, colors=c)

    plt.axis('off');
    plt.tight_layout();
    plt.axis([0, 60, -1, 1])
    plt.draw();
    plt.pause(0.0001);
    plt.clf()

    key = keyboard.read_key()
    x, y = (posx, posy)

    if key == 'up':
        x, y = (x + 0.3 * np.cos(rot), y + 0.3 * np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3 * np.cos(rot), y - 0.3 * np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi / 8
    elif key == 'right':
        rot = rot + np.pi / 8
    elif key == 'esc':
        break
    elif key =='alt':
        x,y,h = x+0.3,y+0.3,h/2
    elif key == 'ctrl':
        x, y,h = (x - 0.3), (y - 0.3),h*2

    if mapa[int(x)][int(y)] == 0:
        posx, posy = (x, y)

plt.close()