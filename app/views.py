from flask import render_template
from app import app
from  .request import get_articles

#Views
@app.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  #Getting popular news articles
  business_articles = get_articles('business')
  print(business_articles)
  title = 'Home - Welcome to The Most Amazing News Highlight Website'
  return render_template('index.html',title = title,business_articles = business_articles)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data

    '''
    return render_template('news.html',id= news_id)