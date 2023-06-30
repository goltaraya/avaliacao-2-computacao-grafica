import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função de callback para selecionar o objeto no frame
def select_object(event, x, y, flags, param):
    global selection, tracking

    if event == cv2.EVENT_LBUTTONDOWN:
        selection = (x, y)
        tracking = True
    elif event == cv2.EVENT_LBUTTONUP:
        tracking = False

# Inicialização
selection = None
tracking = False
positions = []

# Carregar o vídeo
cap = cv2.VideoCapture('questao-2\husky.mp4')

# Verificar se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

# Obter o primeiro frame do vídeo
ret, frame = cap.read()

# Verificar se o frame foi obtido corretamente
if not ret:
    print("Erro ao ler o frame")
    exit()

# Criar a janela e definir a função de callback do mouse
cv2.namedWindow("Selecione o objeto")
cv2.setMouseCallback("Selecione o objeto", select_object)

while True:
    # Exibir o frame e esperar por uma tecla
    cv2.imshow("Selecione o objeto", frame)
    key = cv2.waitKey(1) & 0xFF

    # Sair do loop se a tecla 'q' for pressionada
    if key == ord("q"):
        break

    # Acompanhar o objeto selecionado
    if tracking:
        # Desenhar o retângulo de seleção
        clone = frame.copy()
        cv2.rectangle(clone, selection, (clone.shape[1] - 1, clone.shape[0] - 1), (0, 255, 0), 2)
        cv2.imshow("Selecione o objeto", clone)

    # Obter o próximo frame do vídeo
    ret, frame = cap.read()

    # Verificar se o frame foi obtido corretamente
    if not ret:
        break

    # Armazenar as posições do objeto
    if tracking:
        positions.append(selection)

    # Imprimir as posições do objeto
    if len(positions) > 0:
        print("Posições do objeto:")
        for position in positions:
            print(" - x:", position[0], "y:", position[1])

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()

# Plotar o gráfico
x = [position[0] for position in positions]
y = [position[1] for position in positions]

plt.plot(x, y)
plt.xlabel("Largura")
plt.ylabel("Altura")
plt.title("Posições do objeto")
plt.show()