import matplotlib.pyplot as plt
import PIL as pl
import numpy as np

aks = pl.Image.open('/home/mohsencactus/python 2/Begin/pink.png')
image = np.array(aks)


plt.ylabel('mehvare Y')
plt.xlabel('mehvare X')
plt.title("HELLO")
plt.grid(True)
plt.plot([0,150],[0,150])
plt.plot([0,150],[0,150],'ro')
plt.imshow(image)
plt.show()
