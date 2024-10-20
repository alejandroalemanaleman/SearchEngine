import re


def clean_and_evaluate_word(word):
    # Lista de stop words
    stopwords = [
        # Stop words en español
        "el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "a", "al", "con", "sin", "por", "para",
        "en", "entre", "sobre", "hasta", "ante", "bajo", "desde", "hacia", "durante", "mediante", "tras", "excepto",
        "y", "o", "pero", "porque", "cuando", "donde", "qué", "quién", "cómo", "cuál", "quiénes", "que", "este",
        "esta", "estos", "estas", "ese", "esos", "esa", "esas", "mi", "tu", "su", "nos", "vosotros", "ellos", "ellas",
        "yo", "tú", "usted", "nosotros", "ustedes",

        # Stop words en inglés
        "the", "a", "an", "of", "for", "on", "in", "with", "by", "at", "to", "from", "up", "down", "through",
        "under", "between", "among", "until", "over", "about", "before", "after", "across", "behind", "below",
        "above", "around", "and", "or", "but", "because", "when", "where", "what", "who", "how", "which",
        "this", "that", "these", "those", "my", "your", "his", "her", "our", "their", "you", "they", "it", "we", "he",
        "she", "me", "us", "him", "her", "them",

        # Stop words en francés
        "le", "la", "les", "un", "une", "des", "du", "de", "à", "au", "aux", "avec", "sans", "pour", "par", "dans",
        "sur", "entre", "jusqu’à", "avant", "après", "derrière", "devant", "chez", "sous", "vers", "pendant",
        "parmi", "sauf", "et", "ou", "mais", "parce que", "quand", "où", "quoi", "qui", "comment", "quel", "quelle",
        "ce", "cette", "ces", "mon", "ton", "son", "notre", "votre", "leur", "ils", "elles", "nous", "vous", "je", "tu",
        "il", "elle", "on", "nous", "vous", "ils", "elles"
    ]

    # Modificación de la expresión regular para capturar solo el dominio principal sin la ruta
    # Modificación de la expresión regular para capturar solo el dominio principal sin importar cuántas 'w' haya
    url_pattern = r'https?://[^\s]+'
    word = re.sub(url_pattern, '', word)
    match = re.search(r'^(?:w{3,}\.)?([^\.]+)\.\w+', word)
    if match:
        clean_word = match.group(1)  # Captura solo el nombre del dominio (gutenberg en este caso)
    else:
        clean_word = re.sub(r'\b(\w+\')', '', word)  # Eliminar palabras que terminan en apóstrofo
        clean_word = clean_word.lower().strip("\\/.,!?;:()[]\"'")  # Limpieza de puntuaciones
        clean_word = re.sub(r'[^A-Za-zÀ-ÿ]', '', clean_word)  # Eliminar caracteres no alfabéticos

    # Verifica si la palabra es válida
    if clean_word and clean_word not in stopwords and len(clean_word) > 1:
        return clean_word
    return None

