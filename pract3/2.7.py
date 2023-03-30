import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open(
    r'C:\Users\alexs\OneDrive\Рабочий стол\PractPython\pract3\p.jpg'))
print(repr(img))

plt.imshow(img)
plt.show()
