import urllib.request,json
from .models import Article
from .models import Source

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config["ARTICLE_URL"]

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_sources = None

        if get_sources_response['sources']:
            news_sources_list = get_sources_response['sources']
            news_sources = process_sources(news_sources_list)
    

    return news_sources
def get_articles(id): 
    get_article_details_url = article_url.format(id,api_key)
    url = get_article_details_url .replace(" ","")

    with urllib.request.urlopen(url) as url:
        article_details_data = url.read()
        get_articles_response = json.loads(article_details_data)
        
        news_articles  = []

        if get_articles_response['articles']:
            news_articles_list = get_articles_response ['articles']
            news_articles = process_articles(news_articles_list)
    return news_articles

def process_sources(source_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        news_sources: A list of source objects
    '''
    news_sources = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category=source_item.get('category')
        if url:
            source_object = Source(id,name,description,url,category)
            news_sources.append(source_object)

    return news_sources

def process_articles(article_list):
    news_articles = []
    for article_item in article_list:
        id = article_item.get('id')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')

        if url:
            article_object = Article(id,url,urlToImage,description,publishedAt)
            news_articles.append(article_object)
    
    return news_articles
    