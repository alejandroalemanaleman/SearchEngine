import json
import os

from JSONcontroller import readJSON, writeJSON
from dataExtractor import getMetadata, getWords


def save_metadata(metadataDirectory: str, metadata_dict: dict):
    metadataPath = os.path.join(metadataDirectory, f"metadatos")

    book_info = readJSON(metadataPath)

    book_info.update(metadata_dict)

    # Save dictionary serialized in JSON in a datamart file
    writeJSON(metadataPath, book_info)


def save_words(datamartDirectory: str, word_dict: dict, book_ID):
    wordsDatamartPath = os.path.join(datamartDirectory, f"words")

    # Load the dictionary serialized in JSON from a file
    wordsDatamart = readJSON(wordsDatamartPath)

    for word, line_number in word_dict.items():
        auxiliar = dict()
        auxiliar[book_ID] = dict(frecuency = len(line_number),
                                 lines = line_number)
        if wordsDatamart.get(word) is None:
            wordsDatamart[word] = auxiliar
        else:
            wordsDatamart[word].update(auxiliar)

    # Save dictionary serialized in JSON in a datamart file
    writeJSON(wordsDatamartPath, wordsDatamart)


def saveToDatamart(word_dict: dict, metadata: dict, datamartDirectory: str):
    # create a datamart directory
    if not os.path.exists(datamartDirectory):
        os.makedirs(datamartDirectory)

    save_metadata(datamartDirectory, metadata)

    save_words(datamartDirectory, word_dict, list(metadata.keys())[0])


def inverted_index(datalakeDirectory, datamartDirectory):
    with open(datalakeDirectory, 'r', encoding='utf-8') as book:
        metadataBook = getMetadata(book, datalakeDirectory)

    with open(datalakeDirectory, 'r', encoding='utf-8') as book:
        word_dict = getWords(book)

    saveToDatamart(word_dict, metadataBook, datamartDirectory)
