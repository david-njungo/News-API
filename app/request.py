from app import app
import urllib.request,json
# from .models import newsarticle
from .models import newssource

# Article = newsarticle.Article
Source = newssource.Source

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the newsAPI base url
base_url = app.config["NEWS_API_BASE_URL"]

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