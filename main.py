from modules import file_locations as fl
from modules import data_extraction as de

input_file = fl.input_file()  # reading and loading Input.xlsx
de.data_(input_file)  # passing input file to the Data Extraction module
