import pandas as pd
import os


def input_file():
    input_file_ = "files/input/Input.xlsx"
    df = pd.read_excel(input_file_)
    return df


def RawArticleFiles():
    directory_path = "files/text_data/"
    raw_text_files_directory = os.listdir(directory_path)
    return raw_text_files_directory


def StopWordsFiles():
    directory_path = "files/StopWords/"
    stop_words_files = os.listdir(directory_path)
    return stop_words_files


def after_removing_stop_words_files():
    directory_path = "files/output/articles_after_removing_stop_words/"
    file = os.listdir(directory_path)
    return file


def master_dictionary():
    directory_path = "files/MasterDictionary/"
    file = os.listdir(directory_path)
    return file


def positive_words():
    directory_path = "files/output/positive_words_from_articles/"
    file = os.listdir(directory_path)
    return file


def negative_words():
    directory_path = "files/output/negative_words_from_articles/"
    file = os.listdir(directory_path)
    return file


def output_file():
    file = "files/output/output_data_structure.csv"
    df = pd.read_csv(file)
    return df
