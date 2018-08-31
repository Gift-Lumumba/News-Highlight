from app import app
import urllib.request,json
from app.models import article

Article = article.Article

# Getting api key
api_key = app.config['ARTICLE_API_KEY']

#Getting the article source base url
# base_url = app.config['SOURCES_API_BASE_URL']

#Getting all articles base url
# articles_url = app.config['EVERYTHING_API_BASE_URL']

#Getting top-headline articles base url
base_url = app.config['TOP_HEADLINES_API_BASE_URL']

def get_articles(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(sources,api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        article_results = None

        if get_sources_response['articles']:
            article_results_list = get_sources_response['articles']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if url:
            article_object = Article(author,title,description,url,urlToImage,publishedAt)
            article_results.append(article_object)

    return article_results

def get_article(id):
    get_article_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_object = None
        if article_details_response:
            id = article_details_response.get('id')
            author = article_details_response.get('author')
            description = article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            publishedAt = article_details_response.get('publishedAt')

            article_object = Article(id,author,description,url,urlToImage,publishedAt)

    return article_object


