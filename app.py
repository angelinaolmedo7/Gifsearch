from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # Extract query term from url
    search_term = request.args.get('search_term')

    # Make 'params' dict with query term and API key
    params = {'q': search_term, 'key': 'FFZUQ4CLKXOZ', 'limit': 10}

    # Make an API call to Tenor using the 'requests' library
    # Get the first 10 results from the search results
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
        (params['q'], params['key'], params['limit']))
    gifs = json.loads(r.content)['results']
    # Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", gifs=gifs)


if __name__ == '__main__':
    app.run(debug=True)
