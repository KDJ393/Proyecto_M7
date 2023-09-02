# Importación de bibliotecas para crear una aplicación web con Flask
from flask import Flask
from flask import request
import pandas as pd 
import joblib
import cv2
import pandas as pd
import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
import urllib.request

# Inicializar la aplicación Flask
app = Flask(__name__)

# Definir una ruta y función para predecir basado en un modelo previamente entrenado
@app.route('/predecir', methods=['POST'])
def predecir():

    json_= request.form
    image= cv2.imread(json_)


    if image is None:
        print(f"Failed to load image: {json_}")
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (150, 150))
        image = np.expand_dims(image, axis=0) 
        
    query=image

    # Cargar el modelo entrenado previamente
    clasificador = joblib.load('model.pkl')
    prediccion = clasificador.predict(query)

    if prediccion[0] == True:
        return "Placa Normal"
    else:
        return "Pneumonia"

# Si este script se ejecuta como el programa principal, se inicia la aplicación Flask
if __name__ == 'main':
    app.run(port=6000, debug=True)

 # app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444))) - Cuando ya se pone en producción hay que remplazar la linea anterior por esta