from modules.sentiment_analysis import sentiment_analysis
import pandas as pd

def write_output(input_file, output_file):
    values = {}

    for index, row in input_file.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        values[url_id] = (url, )

    (positive_score, negative_score, polarity_score, subjectivity_score,
     average_sentence_length, complex_word_count, percentage_of_complex_words,
     fog_index, average_number_of_words_per_sentence, word_count,
     syllable_count_per_word, personal_pronouns, average_word_length) = sentiment_analysis()

    for url_id, p_score in positive_score.items():
        if url_id in values.keys():

            values[url_id] = values[url_id] + (p_score,)

    for url_id, n_score in negative_score.items():
        if url_id in values.keys():
            values[url_id] = values[url_id] + (n_score,)

    print(values)