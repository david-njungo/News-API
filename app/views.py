from flask import render_template
from app import app
from .request import get_NEWS

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    business_category = get_NEWS('business')
    print(business_category)
    title = 'NewsAPI'
    return render_template('index.html',title = title, business = business_category)