from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
imagem = cv2.imread('imagens/caminhao.jpg')
resultados = model(imagem)
resultado = resultados[0]
imagem_detectada = resultado.plot()
cv2.imshow("deteccao", imagem_detectada)
cv2.imwrite("resultado.jpg", imagem_detectada)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Detecçao completa")