import os
from .file_locations import after_removing_stop_words_files, masteer_dictionary

directory = after_removing_stop_words_files()
Master_directory = masteer_dictionary()

positive_master = []  # list of all the positive words
negative_master = []  # list of all the negative words


def save_article(article, file_path, list_type):
    """Assumes the article is a list, file_path is the file path of the raw_article
        Saves the article in files/output/articles_after_removing_stop_words/{}.txt with '|' as a seperator"""
    url_id_txt = file_path.split('/')[3]
    url_id = url_id_txt.split('.')[0]
    text_file = "files/output/{}_from_articles/{}.txt".format(list_type, url_id)
    with open(text_file, 'w') as file:
        article_text = '\n'.join(article)
        file.write(article_text)


def MasterDict():
    """Reads positive and negative words from text files and save them in lists"""
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


def p_n_separation():
    """Compares all the words against the positive and negative word list and add them to
        local positive negative words list
        passes the list to save it in another file"""
    for file in directory:
        if file.endswith(".txt"):
            file_path = os.path.join("files/output/articles_after_removing_stop_words", file)
            with open(file_path, 'r') as f:
                line = f.read()
                words = line.split('|')
        positive_words_ = []
        negative_words_ = []
        for word in words:
            if word in positive_master:
                positive_words_.append(word)
            if word in negative_master:
                negative_words_.append(word)
            save_article(positive_words_, file_path, 'positive_words')
            save_article(negative_words_, file_path, 'negative_words')


MasterDict()
