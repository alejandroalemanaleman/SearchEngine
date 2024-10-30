from JSONcontroller import readJSON
import os

def search_book(words_dict, word):
    """cargamos los libros asociados a una palabra del datamart si esta se encuentra"""
    if word in words_dict:
        return words_dict.get(word)
    else:
        return {}


def preview_lines(datalake_path, id_book, lines):

    book_path = os.path.join(datalake_path, f"{id_book}.txt")

    try:
        with open(book_path, 'r') as file:
            for current_number, line_content in enumerate(file, start=1):
                if current_number in lines[:3]:
                    print(f"Line {current_number}: {line_content.strip()}")
                    if 3 == lines.index(current_number)+1:  # If all lines have been printed
                        break
    except FileNotFoundError:
        print(f"File {id_book} not found.")



def print_results(word_dict, metadata_dict, datalake_path):
    # tenemosel diccionario asociado a una sola palabra, 2º nivel de profundidad del datamart

    for id_book in word_dict:
        if metadata_dict.get(id_book) is not None:
            for key, value in metadata_dict.get(id_book).items():
                print(f"{key}: {value}")

            frecuency = word_dict.get(id_book).get("frecuency")
            lines = word_dict.get(id_book).get("lines")
            print(f"Frecuency: {frecuency}")
            print(f"Lines: {lines}")
            print("Preview lines:")
            preview_lines(datalake_path, id_book, lines)
            print("-----------------------------------------------------------------------------------")



def execute(words_data, metadata, datalake_path):

    words_datamart = readJSON(words_data) # dict
    metadata_datamart = readJSON(metadata) # dict


    while True:
        entry = input("Enter a word (or type 'exit' to finish): ")

        if entry.lower() == 'exit':
            break

        words = [] # list of words of the query
        words.extend(entry.split())

        while len(words) > 0:
            word = words.pop(0)
            print(f"buscando: {word}")
            books = search_book(words_datamart, word) # diccionario con todos los codigos de los libros
            print_results(books, metadata_datamart, datalake_path)
