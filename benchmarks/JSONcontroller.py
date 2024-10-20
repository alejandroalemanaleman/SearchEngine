import json

def readJSON(path: str):
    try:
        with open(path, 'r') as file:
            dictionary = json.load(file)
    except FileNotFoundError:
        dictionary = dict()

    return dictionary

def writeJSON(path: str, input):
    with open(path, 'w') as file:
        json.dump(input, file, indent=1)
