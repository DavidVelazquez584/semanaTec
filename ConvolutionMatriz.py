import numpy as np

imagen = np.array([[1,2,3],[7,8,9],[0,0,1]])
kernell1 = np.array([[1,1,1],[0,0,0],[2,10,3]])

print(imagen.shape)
print(kernell1.shape)

def Convolution(image, kernel):
    i_fila,i_columna = image.shape
    conv = 0.0

    for i in range(i_fila):
        for j in range(i_columna):
            conv += image[i,j]*kernel[i,j]

    return conv


print(Convolution(imagen,kernell1))