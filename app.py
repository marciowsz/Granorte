from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = YOLO('yolov8m.pt')
@app.route('/', methods=['GET', 'POST'])
def index():
    imagem_detectada = None
    if request.method == 'POST':
        arquivo = request.files['imagem']
        if arquivo:
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], arquivo.filename)
            arquivo.save(caminho_imagem)
            resultados = model(caminho_imagem)
            resultado = resultados[0]
            imagem = resultado.plot()
            caminho_saida = os.path.join(STATIC_FOLDER, 'caminhao_detectado.jpg')
            cv2.imwrite(caminho_saida, imagem)
            imagem_detectada = 'caminhao_detectado.jpg'
    return render_template(
        'index.html',
        placa="ABC-1234",
        peso="32 toneladas",
        status="APROVADO",
        carga="Brita",
        fraude="NÃO",
        imagem=imagem_detectada
    )
if __name__ == '__main__':
    app.run(debug=True)