import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def data_(df):
    """Assumes df an .xlsx file with first column having ID for articles and second column having URL of the articles
        Saves the articles in the 'files/text_data/' directory with URL_ID as the text file name and .txt as format"""
    print('Total number of Articls: {}'.format(len(df)))
    def save_article_data(URL_ID, title, article):
        """Saves the article with Title and the paragraph in different lines with URL_ID as the text file name and
            .txt as file name"""
        text_file = "files/text_data/{}.txt".format(URL_ID)

        with open(text_file, 'w') as file:
            # write the title to the file
            file.write(f"{title}\n")
            # write the article content to the file
            file.write(article)

    def error(URL_ID, error):
        text_file = "files/text_data/{}-ERROR.txt".format(URL_ID)

        with open(text_file, 'w') as file:
            file.write(f"{error}")

    def data_extraction(URL_ID, URL, index):
        """Assumes URL as a valid URL of the article
            Extracts the Title and Article form the URL"""

        print('Extracting article number {}'.format(index))
        r = requests.get(url=URL, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.find("h1")
        try:
            title_text = title.get_text()
        except AttributeError:
            error(URL_ID, 'Error on page')
            print('ERROR IN ARTICLE NUMBER{}, URL_ID: {}'.format(index, URL_ID))
            print('CHECK ERROR IN URL WITH URL_ID: {} MANUALLY.'.format(URL_ID))
            return  # exit the function

        divs = soup.select("div.td-post-content.tagdiv-type")
        paragraph = ''
        for div in divs:
            # find all the <p> tags inside the current div
            p_tags = div.find_all('p')
            for p in p_tags:
                text = p.get_text()
                paragraph = paragraph + '\n' + text
        print('Saving article number {}'.format(index))
        save_article_data(URL_ID, title_text, paragraph)
        print('Article number {} saved. Moving ahead.'.format(index))

    for index, row in df.iterrows():
        index = index + 1  # index in the XLSX file
        print('Working on article number {}'.format(index))
        URL_ID = row['URL_ID']
        URL = row['URL']
        data_extraction(URL_ID, URL, index)

    print('DATA EXTRACTION SUCCESSFUL')
