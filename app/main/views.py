from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'NewsAPI'
    general = get_sources('general')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')
    health = get_sources('health')
   
    return render_template('index.html',title = title,general = general, business = business,entertainment = entertainment,sports = sports,health = health)

@main.route('/article/id')
def article(id):

    '''
    View article page function that returns the movie details page and its data
    '''
    article = get_articles('id')
    title = f'{article.title}'

    return render_template('article.html',title = title,article = article)