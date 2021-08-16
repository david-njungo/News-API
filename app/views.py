from flask import render_template
from app import app
from .request import get_NEWS

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'NewsAPI'
    bbcnews = get_NEWS('bbc-news')
    abcnews = get_NEWS('abc-news')
    ansa = get_NEWS('ansa')
    aftenposten = get_NEWS('aftenposten')

    return render_template('index.html',title = title, bbcnews = bbcnews,abcnews = abcnews,ansa = ansa, aftenposten = aftenposten)