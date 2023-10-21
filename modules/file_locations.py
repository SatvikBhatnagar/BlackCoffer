import pandas as pd


def input_file():
    input_file_ = "files/input/Input.xlsx"
    df = pd.read_excel(input_file_)
    return df
