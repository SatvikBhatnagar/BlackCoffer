from modules import sentiment_analysis as s_a
import pandas as pd

def write_output(input_file, output_file):
    values = {}

    for index, row in input_file.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        values[url_id] = url
