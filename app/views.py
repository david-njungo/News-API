from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
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