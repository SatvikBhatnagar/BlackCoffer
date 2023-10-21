def data_(df):
    for index, row in df.iterrows():
        URL_ID = row['URL_ID']
        URL = row['URL']
        print(URL_ID, URL)
