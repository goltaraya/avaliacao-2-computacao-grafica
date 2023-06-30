import cv2
import numpy as np
from matplotlib import pyplot as plt

# Função para exibir histograma
def exibir_histograma(imagem, titulo):
    hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])
    plt.figure()
    plt.title(titulo)
    plt.xlabel('Intensidade de pixel')
    plt.ylabel('Frequência')
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

# Carregar a imagem
imagem = cv2.imread('imgexemplo.jpg')

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Verificar se a imagem possui dimensões válidas
altura, largura, _ = imagem.shape
if altura == 0 or largura == 0:
    print("A imagem possui dimensões inválidas.")
    exit()

# Exibir a imagem original
cv2.imshow('Imagem Original', imagem)
cv2.waitKey(0)

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Exibir o histograma em escala de cinza
exibir_histograma(imagem_cinza, 'Histograma em Escala de Cinza')

# Exibir o histograma em RGB
cores = ('b', 'g', 'r')
plt.figure()
plt.title('Histograma em RGB')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Frequência')
for i, cor in enumerate(cores):
    hist = cv2.calcHist([imagem], [i], None, [256], [0, 256])
    plt.plot(hist, color=cor)
    plt.xlim([0, 256])
plt.legend(cores)
plt.show()

# Aplicar alteração de brilho
brilho = 50  # Valor positivo para aumentar o brilho, negativo para diminuir
imagem_alterada = np.clip(imagem.astype(int) + brilho, 0, 255).astype(np.uint8)

# Exibir a imagem alterada
cv2.imshow('Imagem Alterada', imagem_alterada)
cv2.waitKey(0)

# Converter a imagem alterada para escala de cinza
imagem_alterada_cinza = cv2.cvtColor(imagem_alterada, cv2.COLOR_BGR2GRAY)

# Exibir o histograma em escala de cinza para a imagem alterada
exibir_histograma(imagem_alterada_cinza, 'Histograma em Escala de Cinza (Imagem Alterada)')

# Exibir o histograma em RGB para a imagem alterada
plt.figure()
plt.title('Histograma em RGB (Imagem Alterada)')
plt.xlabel('Intensidade de pixel')
plt.ylabel('Frequência')
for i, cor in enumerate(cores):
    hist = cv2.calcHist([imagem_alterada], [i], None, [256], [0, 256])
    plt.plot(hist, color=cor)
    plt.xlim([0, 256])
plt.legend(cores)
plt.show()

# Fechar todas as janelas
cv2.destroyAllWindows()
