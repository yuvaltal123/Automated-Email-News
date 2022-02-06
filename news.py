import requests
from pprint import pprint
import dotenv
import os

dotenv.load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')


class NewsFeed:
    """Representing a new feed report which is a string including
        the requested news - multiple titles and urls"""
    api_key = NEWS_API_KEY
    base_url = 'https://newsapi.org/v2/everything?'

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        articles = self._get_articles_from_web(url)
        email_body = ''
        for article in articles:
            email_body += f"{article['title']}\n{article['url']}\n\n"
        return email_body

    def _get_articles_from_web(self, url):
        request = requests.get(url)
        json_content = request.json()
        articles = json_content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}&' \
              f'to={self.to_date}&' \
              f'sortBy=popularity&' \
              f'language={self.language}&' \
              f'apiKey={self.api_key}'
        return url


# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2022-01-31&'
#        'sortBy=popularity&'
#        'apiKey=87d45c63be0d4283b23607e76e70c2c4')
# url = ('https://newsapi.org/v2/top-headlines?'
#        'sources=bbc-news&'
#        'apiKey=87d45c63be0d4283b23607e76e70c2c4')
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=87d45c63be0d4283b23607e76e70c2c4')
# url = ('https://newsapi.org/v2/everything?'
#        'qInTitle=Nadal&'
#        'from=2022-01-31&'
#        'to=2022-01-31&'
#        'sortBy=popularity&'
#        'language=en&'
#        'apiKey=87d45c63be0d4283b23607e76e70c2c4')

if __name__ == "__main__":
    news_feed = NewsFeed(interest='Nadal', from_date='2022-01-31', to_date='2022-01-31', language='en')
    print(news_feed.get())
