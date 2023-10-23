import csv

from modules.sentiment_analysis import sentiment_analysis
import pandas as pd


def write_output(input_file, output_file):
    values = {}

    for index, row in input_file.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        values[url_id] = (url,)

    (positive_score, negative_score, polarity_score, subjectivity_score,
     average_sentence_length, percentage_of_complex_words,
     fog_index, average_number_of_words_per_sentence, complex_word_count, word_count,
     syllable_count_per_word, personal_pronouns, average_word_length) = sentiment_analysis()

    analysis_var = [positive_score, negative_score, polarity_score, subjectivity_score,
                    average_sentence_length, percentage_of_complex_words,
                    fog_index, average_number_of_words_per_sentence, complex_word_count, word_count,
                    syllable_count_per_word, personal_pronouns, average_word_length]

    for var in analysis_var:
        for url_id, var_to_append in var.items():
            values[url_id] = values[url_id] + (var_to_append,)

    fields = ['URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
              'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
              'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT', 'WORD COUNT',
              'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']

    filename = "write_output_file_.csv"
    rows = [[url_id] + list(values[url_id]) for url_id in values]

    with open(filename, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
