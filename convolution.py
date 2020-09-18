# Codigo propiamente obtenido de: CODEBIND (CODEBIND.COM)
# Liga de la página donde se obtuvo el codigo: http://www.codebind.com/python/opencv-python-tutorial-beginners-smoothing-images-blurring-images-opencv/

# Sección de importaciones de las librerias cv2, numpy y matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Se lee la imagen y se mantiene a color
img = cv2.imread('eljajas.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Se agregan los debidos filtros de la libreria cv2 con numpy
kernel=np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)

# Se agregan los arreglos para la interfaz a imprimir
titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

# Se agrega un for en donde se imprimen los 6 tipos de imagen obtenidas de imagen, 
# convolution, blur, gaussianBlur, media, bilateralFilter
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# Muestra el resultado
plt.show()
