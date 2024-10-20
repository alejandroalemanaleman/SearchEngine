import re

def language_filter(book):
    language_pattern = r'Language:\s*(.*?)(?=\n|$)'
    language_match = re.search(language_pattern, book)
    language = language_match.group(1).strip() if language_match else None
    if language in ["Spanish", "English", "French"]:
        return False
    else:
        return True