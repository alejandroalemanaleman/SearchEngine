from JSONcontroller import readJSON
import os
import time
def buscar_libros(words_dict, word):
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
                    if len(lines) == lines.index(current_number)+1:  # If all lines have been printed
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



def execute(words_datamart, metadata_datamart, datalake_path, query_word=None):
    metadata_datamart = readJSON(metadata_datamart)  # dict

    if query_word is None:
        # If no word is provided, fall back to asking the user for input
        while True:
            entry = input("Enter a word (or type 'exit' to finish): ")
            if entry.lower() == 'exit':
                break
            words = entry.split()  # list of words from the query

            # Start measuring time
            start_time = time.time()
            while len(words) > 0:
                word = words.pop(0)
                print(f"buscando: {word}")
                books = buscar_libros(words_datamart, word)
                print_results(books, metadata_datamart, datalake_path)
            end_time = time.time()

            elapsed_time = end_time - start_time
            print(f"Time taken for search and display: {elapsed_time:.4f} seconds")
    else:
        # If a query word is provided, use it directly
        words = query_word.split()  # list of words from the query

        # Start measuring time
        start_time = time.time()
        while len(words) > 0:
            word = words.pop(0)
            print(f"buscando: {word}")
            books = buscar_libros(words_datamart, word)
            print_results(books, metadata_datamart, datalake_path)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"Time taken for search and display: {elapsed_time:.4f} seconds")