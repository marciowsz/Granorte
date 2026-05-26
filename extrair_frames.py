import cv2
import os
caminho_video = 'videos/placa_tras/placa_tras.mp4'
if not os.path.exists(caminho_video):
    print('VIDEO NAO ENCONTRADO')
    exit()
print('VIDEO ENCONTRADO')
os.makedirs('frames', exist_ok=True)
video = cv2.VideoCapture(caminho_video)
pasta_saida = 'frames/placa_tras'
os.makedirs(pasta_saida, exist_ok=True)
if not video.isOpened():
    print('ERRO AO ABRIR O VIDEO')
    exit()
print('VIDEO ABERTO COM SUCESSO')
count = 0
salvos = 0
while True:
    ret, frame = video.read()
    if not ret:
        print('fim do video ou erro de leitura')
        break
    if count % 30 == 0:
        nome = f'{pasta_saida}/frame_{count}.jpg'
        cv2.imwrite(nome, frame)
        print(f'frame salvo: {nome}')
        salvos += 1
    count += 1
video.release()
print(f'{salvos} frames extraidos!')
print(f' total de frames lidos: {count}')