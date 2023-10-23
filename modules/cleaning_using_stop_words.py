import os
from .file_locations import RawArticleFiles, StopWordsFiles


def is_url(word):
    """Check if a word is a URL based on common patterns."""
    return "http://" in word or "https://" in word or "www." in word


def save_article(article, file_path):
    """Assumes the article is a list, file_path is the file path of the raw_article
        Saves the article in files/output/articles_after_removing_stop_words/{}.txt with '|' as a seperator"""
    url_id = file_path.split('/')[2]
    text_file = "files/output/articles_after_removing_stop_words/{}".format(url_id)
    with open(text_file, 'w') as file:
        article_text = '\n'.join(article)
        file.write(article_text)


def cleaning():
    raw_articles = RawArticleFiles()
    stop_words_file = StopWordsFiles()

    all_the_stop_words = []  # list of all the stop words in lower case

    for file_name in stop_words_file:
        if file_name.endswith(".txt"):
            file_path = os.path.join("files/StopWords", file_name)
            with open(file_path, 'r', encoding='cp1252') as file:  # the encoding of the file is cp1252
                stop_words = file.read().split()  # split the stop words into a list
                non_url_stop_words = [word for word in stop_words if not is_url(word)]
                all_the_stop_words.extend(non_url_stop_words)  # Extend the list with non-URL words
        all_the_stop_words = [word.lower() for word in all_the_stop_words if word.isalnum()]

    def articles_without_stopWords(article, stop_words):
        """Assumes that stop_word_list contains list of all the Stop Words
            Returns a list of the words in the article without the stop words"""
        stop_words_ = stop_words
        article_list = []
        for word in article.split():
            if word.lower() not in stop_words_:
                article_list.append(word)
        return article_list

    for file_name in raw_articles:
        if file_name.endswith("-ERROR.txt"):
            continue

        if file_name.endswith(".txt"):
            file_path = os.path.join("files/text_data", file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                title = lines[0].strip()  # saves the first line as the title
                article_content = ''.join(lines[1:])  # save rest of the article content to process
            result = articles_without_stopWords(article_content, all_the_stop_words)  # list of the article as csv
            save_article(result, file_path)


if __name__ == "__main__":  # ensures that the file is executed if the script is run as the main program
    cleaning()
