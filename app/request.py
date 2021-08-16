from app import app
import urllib.request,json
from .models import newsarticle
from .models import newssource

Article = newsarticle.Article
Source = newssource.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the newsAPI base url
base_url = app.config["NEWS_API_BASE_URL"]
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
def get_article(id):
    get_article_details_url = article_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            title = article_details_response.get('title')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            description = artcle_details_response.get('description')
           publishedAt = article_details_response.get('publishedAt')

            article_object = Article(id,title,url,urlToImage,description,publishedAt)

    return article_object
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