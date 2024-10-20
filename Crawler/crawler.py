import requests
import random
import time
from language_filter import language_filter

def execute(num_of_books, datalake_directory):
    counter = 0
    while counter < num_of_books:
        i = random.randint(1, 99999)
        url = f"https://www.gutenberg.org/cache/epub/{i}/pg{i}.txt"

        if counter >= num_of_books:
            break
        response = requests.get(url)

        if response.status_code == 200:
            book = response.text
            if language_filter("\n".join(book.splitlines()[:50])):
                print(f"Error. Book {i} not in English, Spanish or French.")
                continue
            with open(f"{datalake_directory}/{i}.txt", "w", encoding="utf-8") as file:
                file.write(book)
            print(f"Archive downloaded and saved in 'datalake' as '{i}.txt'")
            counter += 1

        else:
            print(f"Error while downloading archive {i}. State code: {response.status_code}")
        time.sleep(3)
