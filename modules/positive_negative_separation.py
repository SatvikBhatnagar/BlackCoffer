import os
from .file_locations import after_removing_stop_words_files, masteer_dictionary

directory = after_removing_stop_words_files()
Master_directory = masteer_dictionary()

positive_master = []  # list of all the positive words
negative_master = []  # list of all the negative words

def save_article(article, file_path):
    """Assumes the article is a list, file_path is the file path of the raw_article
        Saves the article in files/output/articles_after_removing_stop_words/{}.txt with '|' as a seperator"""
    url_id_txt = file_path.split('/')[3]
    url_id = url_id_txt.split('.')[0]
    text_file = "files/output/positive_words_from_articles/{}.txt".format(url_id)
    with open(text_file, 'w') as file:
        article_text = '|'.join(article)
        file.write(article_text)


def MasterDict():
    for file in Master_directory:
        if file == "positive-words.txt":
            file_path = os.path.join("files/MasterDictionary", file)
            with open(file_path, 'r', encoding='cp1252') as f:
                words = f.readlines()
                words = [word.rstrip('\n') for word in words]
                positive_master.extend(words)


    for file in Master_directory:
        if file == "negative-words.txt":
            file_path = os.path.join("files/MasterDictionary", file)
            with open(file_path, 'r', encoding='cp1252') as f:
                words = f.readlines()
                words = [word.rstrip('\n') for word in words]
                negative_master.extend(words)


def positive_separation():

    for file in directory:
        if file.endswith(".txt"):
            file_path = os.path.join("files/output/articles_after_removing_stop_words", file)
            with open(file_path, 'r') as f:
                line = f.read()
                words = line.split('|')
        positive_words = []
        negative_words = []
        for word in words:
            if word in positive_master:
                positive_words.append(word)
            if word in negative_master:
                negative_words.append(word)
        save_article(positive_words, file_path)

MasterDict()