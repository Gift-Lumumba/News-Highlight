from flask import render_template
from app import app
from  .request import get_articles

#Views
@app.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  #Getting articles sources
  sources_articles = get_articles('cnn')
  print(sources_articles)
  title = 'Home - Welcome to The Most Amazing News Highlight Website'
  return render_template('index.html',title=title,cnn=sources_articles)

@app.route('/article/<int:article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data

    '''
    return render_template('article.html',id= article_id)