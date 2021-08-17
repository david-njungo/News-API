class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        
class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt