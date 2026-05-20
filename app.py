from flask import Flask, render_template
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)
dados = {
    "placa": "ABC-1234",
    "peso": "32 toneladas",
    "status": "APROVADO",
    "carga": "Brita",
    "fraude":"NÃO"
}



@app.route('/')
def home():
    return render_template('index.html', dados=dados)
if __name__ == '__main__':
    app.run(debug=True)