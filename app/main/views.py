from flask import render_template,request,redirect,url_for
from . import main
from  ..request import get_headlines,get_sources,get_articles

#Views
@main.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  #Getting articles sources
  headlines_articles = get_headlines('bbc-news')
  print(headlines_articles)
  technology_articles = get_sources('technology')
  business_articles = get_sources('business')
  health_articles = get_sources('health')
  sports_articles = get_sources('sports')
  entertainment_articles = get_sources('entertainment')
  title = 'Home - Welcome to The Most Amazing News Highlight Website'
  return render_template('index.html', title = title, bbc_news = headlines_articles,technology = technology_articles,business = business_articles, health = health_articles, sports = sports_articles,entertainment = entertainment_articles)

@main.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the article details page and its data
    '''

    info_articles = get_articles(id)
    print(info_articles)

    return render_template('article.html',info = info_articles)
