import requests

# Función para realizar una consulta a la API de Procesamiento de Lenguaje Natural de Google Cloud (análisis de sentimiento)
def consultar_sentimiento(texto):
    url = "https://language.googleapis.com/v1/documents:analyzeSentiment?key=AIzaSyBDvg-0Nu6rMfzIsD1zuIG42h37rtDZGGE"
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": texto
        }
    }
    response = requests.post(url, json=payload)
    data = response.json()
    return data

# Función para realizar una consulta a la API de Procesamiento de Lenguaje Natural de Google Cloud (análisis de entidades)
def consultar_entidades(texto):
    url = "https://language.googleapis.com/v1/documents:analyzeEntities?key=AIzaSyBDvg-0Nu6rMfzIsD1zuIG42h37rtDZGGE"
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": texto
        }
    }
    response = requests.post(url, json=payload)
    data = response.json()
    return data

# Función para realizar una consulta a la API de Reconocimiento de Imágenes de Google Cloud
def reconocer_texto_en_imagen(url_imagen):
    url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyC9SNl-Tdeqqs3v71XfgYIklBqmQc8-5h8"
    payload = {
        "requests": [
            {
                "image": {
                    "source": {
                        "imageUri": url_imagen
                    }
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ]
            }
        ]
    }
    response = requests.post(url, json=payload)
    data = response.json()
    return data

# Función para mostrar los resultados de la consulta de sentimiento
def mostrar_sentimiento(data, texto):
    score = data['documentSentiment']['score']
    magnitude = data['documentSentiment']['magnitude']
    print("Análisis de Sentimiento del Texto:")
    print(f"Texto: {texto}")
    print(f"Puntuación general: {score}")
    print(f"Magnitud general: {magnitude}\n")

    print("Puntuaciones de sentimiento por oración:")
    for i, sentence in enumerate(data['sentences']):
        sentence_text = sentence['text']['content']
        sentence_score = sentence['sentiment']['score']
        sentence_magnitude = sentence['sentiment']['magnitude']
        print(f"Oración {i + 1}: {sentence_text}")
        print(f"  Puntuación: {sentence_score}")
        print(f"  Magnitud: {sentence_magnitude}\n")

# Función para mostrar los resultados de la consulta de entidades
def mostrar_entidades(data, texto):
    print("Análisis de Entidades del Texto:")
    print(f"Texto: {texto}\n")
    
    for entity in data['entities']:
        name = entity['name']
        type_ = entity['type']
        salience = entity['salience']
        print(f"Entidad: {name}")
        print(f"  Tipo: {type_}")
        print(f"  Importancia: {salience}\n")

# Función para mostrar los resultados de la consulta de reconocimiento de texto en imagen
def mostrar_texto_en_imagen(data):
    if 'textAnnotations' in data['responses'][0]:
        texto_detectado = data['responses'][0]['textAnnotations'][0]['description']
        print("Texto detectado en la imagen:")
        print(texto_detectado)
    else:
        print("No se detectó texto en la imagen.")

# Programa principal
if __name__ == "__main__":
    # Consulta de sentimiento
    texto = input("Introduce el texto para analizar su sentimiento: ")
    data_sentimiento = consultar_sentimiento(texto)
    mostrar_sentimiento(data_sentimiento, texto)
    
    # Consulta de entidades
    texto = input("Introduce el texto para analizar sus entidades: ")
    data_entidades = consultar_entidades(texto)
    mostrar_entidades(data_entidades, texto)
    
    # Consulta de reconocimiento de texto en imagen
    url_imagen = input("Introduce la URL de la imagen para reconocer texto: ")
    data_texto_imagen = reconocer_texto_en_imagen(url_imagen)
    mostrar_texto_en_imagen(data_texto_imagen)
