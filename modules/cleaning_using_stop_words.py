import os
from .file_locations import RawArticleFiles, StopWordsFiles


def cleaning():
    raw_articles = RawArticleFiles()

    for file_name in raw_articles:
        if file_name.endswith("-ERROR.txt"):
            continue

        if file_name.endswith(".txt"):
            file_path = os.path.join("files/text_data", file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                title = lines[0].strip()  # saves the first line as the title
                article_content = ''.join(lines[1:])  # save rest of the article content to process
                print("Title:", title)
                print("Article:", article_content)


if __name__ == "__main__":
    cleaning()
