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


def save_words(wordsdatamartDirectory, word_dict, book_ID):

   for word, line_number in word_dict.items():
       wordFilePath = os.path.join(wordsdatamartDirectory, word)

       wordFile = readJSON(wordFilePath) # it's a dictionary

       wordFile[book_ID] = dict(frecuency = len(line_number),
                                lines = line_number)

       writeJSON(wordFilePath, wordFile)



def saveToDatamart(word_dict: dict, metadata: dict, datamartDirectory: str):
    # create a datamart directory
    if not os.path.exists(datamartDirectory):
        os.makedirs(datamartDirectory)

    # save book metadata
    metadataDatamartDirectory = os.path.join(datamartDirectory, f"metadatos")

    if not os.path.exists(metadataDatamartDirectory):
        os.makedirs(metadataDatamartDirectory)

    save_metadata(metadataDatamartDirectory, metadata)

    # save words
    wordsDatamartDirectory = os.path.join(datamartDirectory, f"words")

    if not os.path.exists(wordsDatamartDirectory):
        os.makedirs(wordsDatamartDirectory)

    save_words(wordsDatamartDirectory, word_dict, list(metadata.keys())[0])


def inverted_index(datalakeDirectory, datamartDirectory):
    with open(datalakeDirectory, 'r', encoding='utf-8') as book:
        metadataBook = getMetadata(book, datalakeDirectory)

    with open(datalakeDirectory, 'r', encoding='utf-8') as book:
        word_dict = getWords(book)

    saveToDatamart(word_dict, metadataBook, datamartDirectory)
