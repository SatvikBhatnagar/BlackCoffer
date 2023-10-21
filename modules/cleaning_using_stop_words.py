import os
from .file_locations import RawArticleFiles, StopWordsFiles


def cleaning():
    raw_articles = RawArticleFiles()
    stop_words = StopWordsFiles()

    for file_name in raw_articles:
        if file_name.endswith("-ERROR.txt"):
            continue

        if file_name.endswith(".txt"):
            file_path = os.path.join("files/text_data", file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                title = lines[0].strip()  # saves the first line as the title
                article_content = ''.join(lines[1:])  # save rest of the article content to process

    for file_name in stop_words:
        if file_name.endswith(".txt"):
            file_path = os.path.join("files/StopWords", file_name)
            with open(file_path, 'r', encoding='cp1252') as file: # the encoding of the file is cp1252
                stop_word = file.read()  # this variable has all the Stop Words
                print(stop_word)


if __name__ == "__main__":  # ensures that the file is executed if the script is run as the main program
    cleaning()
