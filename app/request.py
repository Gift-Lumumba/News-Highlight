from app import app

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting base url
articles_url = app.config['ALL_ARTICLES_API_BASE_URL']

#Getting base url
headlines_url = app.config['HEADLINES_API_BASE_URL']

#Getting base url
tech_url = app.config['TECH_NEWS_API_BASE_URL']

#Getting base url
business_url = app.config['BUSINESS_API_BASE_URL']
