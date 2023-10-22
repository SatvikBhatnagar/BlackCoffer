import os
from .file_locations import positive_words, negative_words

positive_words_directory = positive_words()
negative_words_directory = negative_words()

positive_score_dict = {}
negative_score_dict = {}


def positive_score_calculate():
    """Reads positive words from text file and store them in a dictionary with URL as key and score as value"""
    for file_name in positive_words_directory:
        if file_name.endswith(".txt"):
            file_path = os.path.join("files/output/positive_words_from_articles", file_name)
            with open(file_path, 'r', ) as file:
                words = file.readlines()
                words = [word.rstrip('\n') for word in words]

                positive_score = sum(1 for _ in words)  # calculates positive score
            url_id_txt = file_path.split('/')[-1]
            url_id = url_id_txt.split('.')[0]
            positive_score_dict[url_id] = positive_score


def negative_score_calculate():
    """Reads positive words from text file and store them in a dictionary with URL as key and score as value"""
    for file_name in negative_words_directory:
        if file_name.endswith(".txt"):
            file_path = os.path.join("files/output/negative_words_from_articles", file_name)
            with open(file_path, 'r', ) as file:
                words = file.readlines()
                words = [word.rstrip('\n') for word in words]

                negative_score = sum(1 for _ in words)  # calculates positive score
            url_id_txt = file_path.split('/')[-1]
            url_id = url_id_txt.split('.')[0]
            negative_score_dict[url_id] = negative_score


def sentiment_analysis():
    positive_score_calculate()
    negative_score_calculate()
