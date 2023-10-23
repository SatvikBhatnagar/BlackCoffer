from modules import cleaning_using_stop_words as cw
from modules import data_extraction as de
from modules import file_locations as fl
from modules import positive_negative_separation as pns
from modules import sentiment_analysis as sa
from modules import write_output_file

input_file = fl.input_file()  # reading and loading Input.xlsx

# extracting data
# data_extraction = input("Do you want to extract articles? (Type 'y' to extract): ")
# if data_extraction == 'y':
#     de.data_(input_file)  # passing input file to the Data Extraction module
#
#
# cleaning using Stop Words Lists
# cw.cleaning()

# using Master Dictionary to separate positive negative words
# pns.p_n_separation()

sa.sentiment_analysis()
#
# output_file = fl.output_file()
# write_output_file.write_output(input_file, output_file)
