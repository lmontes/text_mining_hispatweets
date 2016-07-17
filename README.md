# Text Mining dataset HispaTweets

### Scripts en python

Se han creado una serie de script en python para extraer y transformar los tweets del dataset y así poder crear un modelo de Machine Learning que sirva para clasificarlos. Estos script son:

* **process_tweets.py**: lee todos los ficheros con los tweets para extraer solo el texto y dejarlos en una representación más compacta.
* **extract_vocabulary.py**: extrae las palabras de los tweets y calcula las frecuencias por clase y desviaciones típicas.
* **generate_bow.py**: obtiene un BoW (Bag of Words) a partir del vocabulario.
* **generate_samples.py**: dados los ficheros con los BOWs genera las representaciones de las muestras para poder aprender un modelo.
