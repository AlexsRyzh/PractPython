import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



img = np.array(Image.open(r'C:\Users\alexs\OneDrive\Рабочий стол\PractPython\pract3\p.jpg'))
WIDTH = img.shape[1]
HEIGHT = img.shape[0]


points = np.random.randint(0, [WIDTH, HEIGHT], size=(200, 2))

print(WIDTH,HEIGHT)

def dist(x,y,x1,y1):
    return ((x-x1)**2+(y-y1)**2)**0.5

for i in range(HEIGHT):
    for j in range(WIDTH):
        min_dist = (WIDTH+HEIGHT)
        color = np.array([0,0,0])
        for point in points:
            new_dist = dist(j, i,point[0],point[1])
            if new_dist<min_dist:
                min_dist = new_dist
                color = img[point[1]][point[0]]
        img[i][j]=color
    print(i)


plt.imshow(img)
plt.show()