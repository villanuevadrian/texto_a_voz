import nltk
from newspaper import Article
from gtts import gTTS
from tempfile import TemporaryFile

# Descargamos los recursos lingüistícos para el correcto funcionamiento del programa
nltk.download()

# Solicitamos al usuario que introduzca la URL del artículo para descargar el texto
url = input("Introduce la url del artículo desesado: ")

# Creamos el objeto de la clase Article y lo descargamos
article = Article(url)
article.download()

# Analizamos la sintaxis
article.parse()

# Podemos mostrar por pantalla el texto para comprobar que el archivo mp3 se ha creado correctamente
print(article.text)

# Convierto el texto en un archivo mp3
tts= gTTS(article.text,lang="es")

# Creamos un objeto de la clase BytesIO que nos leera el archivo mp3
mp3_fp = TemporaryFile()
tts.write_to_fp(mp3_fp)

# Guardamos el archivo mp3
tts.save("audio.mp3")
