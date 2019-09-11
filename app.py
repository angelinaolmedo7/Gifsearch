from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # Extract query term from url
    search_term = request.args.get('search_term')
    # TODO: Make 'params' dict with query term and API key
    params = {'query term': search_term, 'API key': 'FFZUQ4CLKXOZ'}
    # TODO: Make an API call to Tenor using the 'requests' library
    
    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html") + str(search_term)


if __name__ == '__main__':
    app.run(debug=True)
