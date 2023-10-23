import os
from .file_locations import positive_words, negative_words, after_removing_stop_words_files

positive_words_directory = positive_words()
negative_words_directory = negative_words()
articles_after_removing_stop_words_directory = after_removing_stop_words_files()


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


def polarity_score_calculate(positive_score_dict, negative_score_dict):
    for url_id, value_pos in positive_score_dict.items():
        value_neg = negative_score_dict.get(url_id)
        positive_score = value_pos
        negative_score = value_neg
        polarity_score_calc = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
        return polarity_score_calc


def subjectivity_score_calculate(positive_score_dict, negative_score_dict):
    subjectivity_score_calc_dict = {}
    for url_id, value_pos in positive_score_dict.items():
        value_neg = negative_score_dict.get(url_id)

        for file_name in articles_after_removing_stop_words_directory:
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r', ) as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    total_words_after_cleaning = len(words)
                    subjectivity_score_calculation = (value_pos + value_neg) / ((total_words_after_cleaning) + 0.000001)
                    subjectivity_score_calc_dict[url_id] = subjectivity_score_calculation

    return subjectivity_score_calc_dict


def sentiment_analysis():
    positive_score = positive_score_calculate()
    negative_score = negative_score_calculate()
    polarity_score = polarity_score_calculate(positive_score, negative_score)
    subjectivity_score = subjectivity_score_calculate(positive_score, negative_score)
