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
