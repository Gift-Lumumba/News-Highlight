from flask import render_template
from app import app
from  app.request import get_articles,get_article,get_sports,get_business,get_technology,get_entertainment,get_health,get_science,get_sources

#Views
@app.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  #Getting articles sources
  article_sources = get_sources('general')
  print(article_sources)
  title = 'Home - Welcome to The Most Amazing News Highlight Website'
  return render_template('index.html', title = title,general = article_sources)

  #Getting articles
  topheadline_articles = get_articles('cnn')
  sports_articles = get_sports('us')
  business_articles = get_business('gb')
  technology_articles = get_technology('techcrunch')
  entertainment_articles = get_entertainment('entertainment_weekly')
  health_articles = get_health('google_news')
  science_articles = get_science('new_scientist')
  print(topheadline_articles)
  title = 'Home - Welcome to The Most Amazing News Highlight Website'
  return render_template('index.html',title=title,cnn=topheadline_articles,us=sports_articles,gb=business_articles,techcrunch=technology_articles,entertainment_weekly=entertainment_articles,google_news=health_articles,new_scientist=science_articles)

@app.route('/article/<int:id>')
def article(id):

    '''
    View article page function that returns the article details page and its data

    '''

    article = get_article(id)
    title = f'{article.title}'

    return render_template('article.html',title = title ,article = article)
