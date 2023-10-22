import os
from .file_locations import positive_words, negative_words

positive_words_directory = positive_words()
negative_words_directory = negative_words()


def positive_score_calculate():
    """Reads positive words from text file and store them in a dictionary with URL as key and score as value"""
    positive_score_dict = {}

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
    return positive_score_dict


def negative_score_calculate():
    """Reads positive words from text file and store them in a dictionary with URL as key and score as value"""
    negative_score_dict = {}

    for file_name in negative_words_directory:
        if file_name.endswith(".txt"):
            file_path = os.path.join("files/output/negative_words_from_articles", file_name)
            with open(file_path, 'r', ) as file:
                words = file.readlines()
                words = [word.rstrip('\n') for word in words]

                negative_score = sum(-1 for _ in words)  # calculates positive score
            url_id_txt = file_path.split('/')[-1]
            url_id = url_id_txt.split('.')[0]
            negative_score_dict[url_id] = (negative_score * -1)
    return negative_score_dict

def polarity_score(positive_score_dict, negative_score_dict):
    for url_id, value_pos in positive_score_dict.items():
        value_neg = negative_score_dict.get(url_id)
        positive_score = value_pos
        negative_score = value_neg
        polarity_score_calc = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        print(polarity_score_calc)


def sentiment_analysis():
    positive_score = positive_score_calculate()
    negative_score = negative_score_calculate()
    polarity_score(positive_score, negative_score)
