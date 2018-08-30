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
    get_article_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['results']:
            article_results_list = get_article_response['results']
            article_results = process_results(article_results_list)


    return article_results
