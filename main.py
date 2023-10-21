from modules import file_locations as fl
from modules import data_extraction as de
from modules import cleaning_using_stop_words as cw

input_file = fl.input_file()  # reading and loading Input.xlsx

# extracting data
"""data_extraction = input("Do you want to extract articles? (Type 'y' to extract): ")
if data_extraction == 'y':
    de.data_(input_file)  # passing input file to the Data Extraction module
"""

# cleaning using Stop Words Lists
cw.cleaning()
