from flask import render_template
from app import app
from  .request import get_articles,get_article

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

@app.route('/article/<int:id>')
def article(id):

    '''
    View article page function that returns the article details page and its data

    '''

    article = get_article(id)
    title = f'{article.title}'
    
    return render_template('article.html',title = title ,article = article)
