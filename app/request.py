from app import app
import urllib.request,json
from app.models import article

Article = article.Article

# Getting api key
api_key = app.config['ARTICLE_API_KEY']

#Getting the articles base url
base_url = app.config["ARTICLE_API_BASE_URL"]

#Getting all articles base url
articles_url = app.config['ALL_ARTICLES_API_BASE_URL']

#Getting headline articles base url
headlines_url = app.config['HEADLINES_API_BASE_URL']

#Getting tech articles base url
tech_url = app.config['TECH_NEWS_API_BASE_URL']

#Getting business articles base url
business_url = app.config['BUSINESS_API_BASE_URL']


def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_articles: A list of article objects
    '''
    article_articles = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if url:
            article_object = Article(author,title,description,url,urlToImage,publishedAt)
            article_articles.append(article_object)

    return article_articles
