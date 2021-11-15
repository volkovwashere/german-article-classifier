import re
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")

GERMAN_STOP_WORDS = stopwords.words('german')
GERMAN_STOP_WORDS.append("fur")


def remove_punctuation(document: str) -> str:
    """
    This function removes punctuation from a given str type sentence.
    Args:
        document (str): Input string. Eg.: This is, a sentence.

    Returns (str): Subbed sentence. Eg.: This is a sentence

    """
    return re.sub(r'[^\w\s]', '', document)


def remove_numbers(document: str) -> str:
    """
    This function removes every number from a given sentence.
    Args:
        document (str): Input string. Eg.: This is, 4 a sentence1

    Returns (str): Subbed sentence. Eg.: This is, a sentence

    """
    return re.sub(r'$\d+\W+|\b\d+\b|\W+\d+$', '', document)


def map_umlaut(document: str) -> str:
    """
    This function maps some umlaut characters to their corresponding "english" one.
    Args:
        document (str): Input string. Eg.: Über alles

    Returns (str): Subbed sentence. Eg.: Uber alles

    """
    umlaut_mapping = {
        "ß": "b",
        "ü": "u",
        "ä": "a",
        "ö": "o",
        "ë": "e",
    }
    for k, v in umlaut_mapping.items():
        document = document.replace(k, v)
    return document


def stop_word_removal(document: str) -> str:
    """
    This function removes german stopwords based on the nltk german stop word set and some word added after
    data analysis.
    Args:
        document (str): Input string. Eg.:  Das ist ein....

    Returns (str): Subbed sentence. Eg.: ist ein

    """
    return " ".join(w for w in document.split() if w not in GERMAN_STOP_WORDS)
