class Headlines:
    """
    Headlines class to define headlines objects
    """
    def __init__(self,author,title,description,urlToImage,url,publishedAt):
        self.author=author
        self.title=title
        self.description=description
        self.urlToImage=urlToImage
        self.url=url
        self.publishedAt=publishedAt



class Sources:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url):
        self.id =id
        self.name = name
        self.description = description
        self.url = url

class Articles:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.author =author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt