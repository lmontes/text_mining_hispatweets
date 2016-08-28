# Text Mining dataset HispaTweets

### Scripts en python

Se han creado una serie de script en python para extraer y transformar los tweets del dataset y así poder crear un modelo de Machine Learning que sirva para clasificarlos. Estos script son:

* **process_tweets.py**: lee todos los ficheros con los tweets para extraer solo el texto y dejarlos en una representación más compacta.
* **extract_vocabulary.py**: extrae las palabras de los tweets y calcula las frecuencias por clase y desviaciones típicas.
* **generate_bow.py**: obtiene un BoW (Bag of Words) a partir del vocabulario.
* **generate_samples.py**: dados los ficheros con los BOWs genera las representaciones de las muestras para poder aprender un modelo.

### Scripts en R

Dentro de la carpeta R se encuentra un proyecto de RStudio con dos scripts que se han usado para extraer estadísticas del dataset y entrenar los modelos de clasificación. Estos scripts son:

* **analyze.R**: este script lee los ficheros con la información de los autores y hace un conteo de la distribución de autores por clase.
* **check.R**: este script lee los ficheros usados para el entrenamiento y test y crea y evalua varios modelos de clasificación.

### Procedimiento a seguir

Si queremos reproducir el experimento debemos bajarnos el repositorio y descomprimir el dataset https://s3.amazonaws.com/cosmos.datasets/hispatweets.zip dentro de la carpeta data, tras este primer paso se deben ejecutar los siguientes scripts en este orden:

* **process_tweets.py**
* **extract_vocabulary.py**
* **generate_bow.py**
* **generate_samples.py**

Para finalizar hay que abrir el proyecto de RStudio y ejecutar el script **check.R**.
