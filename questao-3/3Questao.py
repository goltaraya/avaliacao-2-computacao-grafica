import cv2
import numpy as np

# Carrega a imagem
# Substitua pelo caminho que está sua imagem
image = cv2.imread('questao-3/cat.jpg')

# Definindo a escala
scale_percent = 50  # Mudança de escala em porcentagem
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# Realiza a mudança de escala
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# Definindo a matriz de translação
tx = 50  # Valor de translação no eixo X
ty = 100  # Valor de translação no eixo Y
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Realiza a translação
translated = cv2.warpAffine(resized, M, (resized.shape[1], resized.shape[0]))

# Definindo o ângulo de rotação
angle = 45  # Ângulo de rotação em graus

# Realiza a rotação
(h, w) = translated.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(translated, M, (w, h))

# Mostra a imagem original e a imagem manipulada
cv2.imshow("Imagem Original", image)
cv2.imshow("Imagem Manipulada", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
