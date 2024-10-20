import re
from itertools import islice
import wordCleaner

def getMetadata(book, book_path):
    input_string = ''.join(islice(book, 50))
    match = re.search(r'(\d+)\.txt$', book_path)
    if match: book_id = match.group(1)

    title_pattern = r'Title:\s*(.*?)(?=\n|$)'
    author_pattern = r'Author:\s*(.*?)(?=\n|$)'
    language_pattern = r'Language:\s*(.*?)(?=\n|$)'

    # Search for patterns in the input string
    title_match = re.search(title_pattern, input_string)
    author_match = re.search(author_pattern, input_string)
    language_match = re.search(language_pattern, input_string)

    # Extracting the values or setting to None if not found
    title = title_match.group(1).strip() if title_match else None
    author = author_match.group(1).strip() if author_match else None
    language = language_match.group(1).strip() if language_match else None

    metadata_dict = dict()

    metadata_dict[book_id] = {
        "title": title,
        "author": author,
        "language": language,
        "download_link": f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    }

    return metadata_dict


def getWords1(book):
    word_dict = {}

    for line_number, line in enumerate(book, start=1):
        # Split the line into words
        words = line.split()  # Split on whitespace to get words

        for word in words:
            clean_word = wordCleaner.clean_and_evaluate_word(word)  # Clean the word
            if clean_word:
                # Add line number to the dictionary
                if clean_word in word_dict:
                    word_dict[clean_word].append(line_number)
                else:
                    word_dict[clean_word] = [line_number]

    # Sort and remove duplicates from line numbers
    for key in word_dict:
        word_dict[key] = sorted(set(word_dict[key]))

    print(word_dict)
    return word_dict


import re


def getWords(book):
    word_dict = {}
    start_pattern = r"\*\*\* START.*\*\*\*"  # Pattern to detect the start line
    end_pattern = r"\*\*\* END.*\*\*\*"  # Pattern to detect the end line
    start_processing = False

    for line_number, line in enumerate(book, start=1):
        if not start_processing:
            # Check if the start marker is found
            if re.search(start_pattern, line):
                start_processing = True
            continue  # Skip lines until the start marker is found

        # Stop processing when the end marker is found
        if re.search(end_pattern, line):
            break  # Exit the loop once the end marker is found

        # Split the line into words once processing starts
        words = line.split()  # Split on whitespace to get words

        for word in words:
            clean_word = wordCleaner.clean_and_evaluate_word(word)  # Clean the word
            if clean_word:
                # Add line number to the dictionary
                if clean_word in word_dict:
                    word_dict[clean_word].append(line_number)
                else:
                    word_dict[clean_word] = [line_number]

    # Sort and remove duplicates from line numbers
    for key in word_dict:
        word_dict[key] = sorted(set(word_dict[key]))

    print(word_dict)
    return word_dict

