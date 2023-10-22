import os
from .file_locations import after_removing_stop_words_files

directory = after_removing_stop_words_files()

def positive_serperation():
    positive = []  # list of all the positive words

    for file in directory:
        if file.endswith(".txt"):
            file_path = os.path.join("files/output/articles_after_removing_stop_words", file)
            with open(file_path, 'r') as f:
                line = f.read()
                words = line.split('|')
                print(words)
