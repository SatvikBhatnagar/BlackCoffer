from .file_locations import input_file as i_file
import pandas as pd

input_file = pd.read_excel(i_file)

url_ids = data.iloc[:, 0]
urls = data.iloc[:, 1]
