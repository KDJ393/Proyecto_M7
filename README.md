# Proyecto 7

Proyecto de detección de neumonía con modelado de inteligencia artificial. 

# Introducción

Las herramientas que hoy día nos ofrece la tecnología abren el campo de las opciones que se ofrecen en el día a día, uno de los campos en los que dicho impacto puede verse reflejado es el campo de la medicina. 
El tratamiento de diversas enfermedades depende ampliamente del análisis de especialistas calificados a los que, por desgracia, un buen porcentaje de la población no puede acceder. Es en estos casos donde la tecnología puede ofrecer ayuda no solo para los pacientes, también para un sistema de salud que se encuentra saturado y en busca de opciones que pueda ayudar al flujo de pacientes y su tratamiento. 

La neumonía es una de las afecciones de salud que más repercuten en la población mexicana actualmente. Según cifras del INEGI las afecciones respiratorias se encuentran entre las primeras 10 causas de muerte con respecto a los últimos 3 años. Como la mayoría de las afecciones de salud la pronta detección y tratamiento influyen directamente en el pronostico del avance de dicha enfermedad, por lo tanto este proyecto pretende otorgar una alternativa para ayudar a la rápida detección de la patología. 

![](Estadisticas_enfermedades.png)

# Dataset

Para el entrenamiento de nuestro modelo utilizamos una base de datos publica extraída de la pagina Kaggle. Dicha base de datos cuenta con tres apartados de imágenes, divididas a su vez en dos categorías: "Normal" y "Pneumonia".

Una vez se realiza el análisis exploratorio de la base de datos podemos anticipar el obvio inbalance del feed de datos, por lo que esto será tomado en cuenta en la interpretación de los datos. 

![](Casos.png)

# Entrenamiento

Para este modelo se utilizara el tratamiento de imágenes del modulo Keras de la paquetería TensorFlow, construyendo una red neuronal de 5 capas de procesamiento y una de salida y adecuación, evaluación estándar con 5 epocas (cantidad de epocas elegida por resultados exploratorios de una serie de pruebas). 

![](Entrenamiento.png)

Una vez construido el modelo tenemos los siguientes resultados de predicción, junto con sus marcadores estadísticos:

![](Matriz.png)

Según los resultados de nuestro modelo podemos consideres que el porcentaje de accuracy se encuentra en 83%, numero que si bien no es bajo también ofrece un panorama para la mejora de dicho modelado debido a que el campo de trabajo es la salud. 

![](output.png)

Una de las áreas de oportunidad con una repercusión mayor es el inbalance de las muestras y también la poca variación de estas, ya que un variedad de opciones podrían hacer a nuestro modelo aun mas especifico y por lo tanto mas seguro, por otro lado un procesamiento mucho mas especifico de las imágenes podría ayudar también a mejorar el modelo.

# Implementacón

Se diseño una interfaz ejecutable para que el modelo pueda ser probado con imágenes externas. 

![](Interfaz.png)

Este proyecto sienta una base para demostrar el impacto que se puede lograr con un desarrollo de herramientas alimentadas con el procesamiento de datos y la inteligencia artificial en aspectos tan variados como ayudar al campo de salud en general. 
