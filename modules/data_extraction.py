import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def data_(df):
    def data_extraction(URL_ID, URL):
        r = requests.get(url=URL, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.select("h1.entry-title")
        title_text = title[0].get_text()
        print(title_text)
        divs = soup.select("div.td-post-content.tagdiv-type")
        for div in divs:
            #find all the <p> tags inside the current div
            p_tags = div.find_all('p')
            for p in p_tags:
                text = p.get_text()
                print(text)


        return None

    for index, row in df.iterrows():
        URL_ID = row['URL_ID']
        URL = row['URL']
        data_extraction(URL_ID, URL)
