import urllib.request,json
from .models import Headlines,Sources,Articles

# Source = source.Source
# Article = article.Article

# Getting api key
api_key = None

#Getting base url
base_url = None
headlines_url = None
articles_url = None

def configure_request(app):
    global api_key,base_url,headlines_url,articles_url
    api_key = app.config['ARTICLE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    headlines_url = app.config['TOP_HEADLINES_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']


def get_headlines(source):
    '''
    Function that gets the json response to our url request
    Takes news source as an argument
    '''
    get_headlines_url = headlines_url.format(source,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)


    return headlines_results

def process_headlines(headlines_list):
    '''
    Function  that processes the headlines result and transform them to a list of Objects
    Args:
        headlines_list: A list of dictionaries that contain source details
    Returns :
        headlines_results: A list of headlines objects
    '''
    headlines_results = []
    for headlines_item in headlines_list:
        author = headlines_item.get('author')
        title = headlines_item.get('title')
        description = headlines_item.get('description')
        url = headlines_item.get('url')
        urlToImage = headlines_item.get('urlToImage')
        publishedAt = headlines_item.get('publishedAt')

        if urlToImage:
            headlines_object = Headlines(author,title,description,url,urlToImage,publishedAt)
            headlines_results.append(headlines_object)

    return headlines_results

def get_sources(category):
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        sources_list A list of dictionaries that contain catnews details
t:
    Returns :
        sources_results: A list of sources objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')

        if id:
            sources_object =Sources(id,name,description,url)
            sources_results.append(sources_object)

    return sources_results



def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(id,api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results

def process_articles(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain article details
    Returns :
        articles_results: A list of article objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        if url:
            articles_object = Articles(id,author,title,description,url,urlToImage,publishedAt)
            articles_results.append(articles_object)

    return articles_results


