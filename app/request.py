from app import app
import urllib.request,json
from .models import newsarticle
Article = newsarticle.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the newsAPI base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_NEWS(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)


    return news_articles
def process_articles(article_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain movie details

    Returns :
        news_articles: A list of movie objects
    '''
    news_articles = []
    for article_item in article_list:
        title = article_item.get('title')
        description = article_item.get('description')
        category= article_item.get('category')
        url = article_item.get('url')
        urlToImage= article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('source')

        if urlToImage:
            article_object = Article(title,description,category,url,urlToImage,publishedAt)
            news_articles.append(article_object)

    return news_articles