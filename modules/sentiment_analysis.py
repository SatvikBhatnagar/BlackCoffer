import os
from .file_locations import positive_words, negative_words, after_removing_stop_words_files
import pyphen
import string
import re

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
            url_id_parts = url_id_txt.split('.')
            url_id = float(f"{url_id_parts[0]}.{url_id_parts[1]}")
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
            url_id_parts = url_id_txt.split('.')
            url_id = float(f"{url_id_parts[0]}.{url_id_parts[1]}")
            negative_score_dict[url_id] = (negative_score * -1)
    return negative_score_dict


def polarity_score_calculate(positive_score_dict, negative_score_dict):
    polarity_scores_dict = {}
    for url_id, value_pos in positive_score_dict.items():
        value_neg = negative_score_dict.get(url_id)
        positive_score = value_pos
        negative_score = value_neg
        polarity_score_calc = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

        polarity_scores_dict[url_id] = polarity_score_calc
    return polarity_scores_dict


def subjectivity_score_calculate(positive_score_dict, negative_score_dict):
    subjectivity_score_calc_dict = {}
    number_of_total_words = {}
    for url_id, value_pos in positive_score_dict.items():
        value_neg = negative_score_dict.get(url_id)

        for file_name in articles_after_removing_stop_words_directory:
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r', ) as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    total_words_after_cleaning = len(words)
                    subjectivity_score_calculation = (value_pos + value_neg) / (total_words_after_cleaning + 0.000001)
                    subjectivity_score_calc_dict[url_id] = subjectivity_score_calculation
                    number_of_total_words[url_id] = total_words_after_cleaning

    return subjectivity_score_calc_dict, number_of_total_words


def average_sentence_length_calculate(dictionary_that_has_url_id):
    average_sentence_length_calc_dict = {}
    for url_id in dictionary_that_has_url_id:
        for file_name in articles_after_removing_stop_words_directory:
            sentences = 0
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r', ) as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    for word in words:
                        if word.endswith('.'):
                            sentences += 1
                    average_sentence_length_calc = len(words) / sentences
                    average_sentence_length_calc_dict[url_id] = average_sentence_length_calc

    return average_sentence_length_calc_dict


dic = pyphen.Pyphen(lang='en')


def count_syllables(word):
    return len(dic.inserted(word).split("-"))  # breaks down the word in syllables


def complex_word_calculate(dictionary_that_has_url_id):
    complex_word_calc_dict = {}
    for url_id in dictionary_that_has_url_id:
        for file_name in articles_after_removing_stop_words_directory:
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r', ) as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    total_words = len(words)
                    complex_word_count = 0
                    for word in words:
                        if count_syllables(word) > 2:
                            complex_word_count += 1

                    complex_word_calc_dict[url_id] = complex_word_count
    return complex_word_calc_dict


def percentage_of_complex_words_calculate(complex_word_count_dict, total_number_of_words_dict):
    percentage_of_complex_words_calc_dict = {}
    for url_id in complex_word_count_dict:
        if url_id in total_number_of_words_dict:
            total_words = total_number_of_words_dict[url_id]
            complex_w_count = complex_word_count_dict[url_id]
            percentage_of_complex_words_calculation = (complex_w_count / total_words) * 100
            percentage_of_complex_words_calc_dict[url_id] = percentage_of_complex_words_calculation
    return percentage_of_complex_words_calc_dict


def fog_index_calculate(percentage_of_complex_words_dict, average_sentence_length_dict):
    fog_index_dict = {}
    for url_id in percentage_of_complex_words_dict:
        if url_id in average_sentence_length_dict:
            avg_sentence_len = average_sentence_length_dict[url_id]
            percentage_complex_w = percentage_of_complex_words_dict[url_id]
            fog_index = 0.4 * (avg_sentence_len + percentage_complex_w)
            fog_index_dict[url_id] = fog_index
    return fog_index_dict


def remove_punctuation(word):
    translator = str.maketrans('', '', string.punctuation)
    clean_word = word.translate(translator)
    return clean_word


def word_counting(dict_that_has_url_id):
    word_counting_dict = {}
    for url_id in dict_that_has_url_id:
        for file_name in articles_after_removing_stop_words_directory:
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r', ) as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    words_without_punctuation = [remove_punctuation(word) for word in words]
                    cleaned_words = sum(1 for word in words_without_punctuation)
                    word_counting_dict[url_id] = cleaned_words

    return word_counting_dict


def syllable_counting_per_word(dict_that_has_url_id):
    syllable_count_dict = {}
    for url_id in dict_that_has_url_id:
        for file_name in articles_after_removing_stop_words_directory:
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r') as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    words = [remove_punctuation(word) for word in words]
                    syllable_counts_list = []

                    for word in words:
                        exceptions = ["es", "ed"]
                        is_exception = False
                        for exception in exceptions:
                            if word.endswith(exception):
                                is_exception = True
                                break
                        if is_exception:
                            syllables = 1
                        else:
                            syllables = count_syllables(word)
                        syllable_counts_list.append(syllables)

                    text_file = "files/output/syllable_count_per_word/{}.txt".format(url_id)
                    with open(text_file, 'w') as f:
                        for word, count in zip(words, syllable_counts_list):
                            f.write(f"{word}:{count}\n")
                    total_syllables = sum(sy for sy in syllable_counts_list)
                    syllable_count_dict[url_id] = (total_syllables, total_syllables / len(words))

    return syllable_count_dict


def count_personal_pronouns(dict_that_has_url_id):
    pronoun_dict = {}
    pronoun_pattern = r'\b(I|we|my|ours|us)\b'

    for url_id in dict_that_has_url_id:
        for file_name in articles_after_removing_stop_words_directory:
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r') as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    words = [remove_punctuation(word) for word in words]
                    pronoun_counts = {pronoun: 0 for pronoun in ["I", "we", "my", "ours", "us"]}
                    for word in words:
                        # Special care to exclude the country name "US"
                        if word.lower() != "US":
                            pronoun_matches = re.findall(pronoun_pattern, word, re.IGNORECASE)
                            # Count the number of matches and update the counts in the dictionary
                            for match in pronoun_matches:
                                if match == "i" or match == 'I':
                                    pronoun_counts['I'] += 1
                                else:
                                    pronoun_counts[match.lower()] += 1
                    pronoun_dict[url_id] = pronoun_counts

    return pronoun_dict


def average_word_length_calculate(dictionary_that_has_url_id):
    average_word_length_calc_dict = {}
    for url_id in dictionary_that_has_url_id:
        for file_name in articles_after_removing_stop_words_directory:
            total_chars = 0
            if file_name == f"{url_id}.txt":
                file_path = os.path.join("files/output/articles_after_removing_stop_words", file_name)
                with open(file_path, 'r', ) as file:
                    words = file.readlines()
                    words = [word.rstrip('\n') for word in words]
                    words = [remove_punctuation(word) for word in words]
                    # print(words)
                    for word in words:
                        total_chars += len(word)
                    if total_chars > 0:
                        average_word_length_calc = total_chars / len(words)
                    else:
                        average_word_length_calc = 0
                average_word_length_calc_dict[url_id] = average_word_length_calc

    return average_word_length_calc_dict


def sentiment_analysis():
    positive_score = positive_score_calculate()
    negative_score = negative_score_calculate()
    polarity_score = polarity_score_calculate(positive_score, negative_score)
    subjectivity_score, total_number_of_words = subjectivity_score_calculate(positive_score, negative_score)
    average_sentence_length = average_sentence_length_calculate(positive_score)
    complex_word_count = complex_word_calculate(positive_score)
    percentage_of_complex_words = percentage_of_complex_words_calculate(complex_word_count, total_number_of_words)
    fog_index = fog_index_calculate(percentage_of_complex_words, average_sentence_length)
    average_number_of_words_per_sentence = average_sentence_length  # both have same formula
    word_count = word_counting(positive_score)
    syllable_count_per_word = syllable_counting_per_word(positive_score)
    personal_pronouns = count_personal_pronouns(positive_score)
    average_word_length = average_word_length_calculate(positive_score)

    return (positive_score, negative_score, polarity_score, subjectivity_score, average_sentence_length, complex_word_count,
            percentage_of_complex_words, fog_index, average_number_of_words_per_sentence, word_count, syllable_count_per_word,
            personal_pronouns, average_word_length)