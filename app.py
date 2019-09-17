from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    # Extract query term from url
    search_term = request.args.get('search_term')
    print(search_term)
    trending = search_term is None

    # Make 'params' dict with query term and API key
    params = {'q': search_term, 'key': 'FFZUQ4CLKXOZ', 'limit': 10}

    urls = []
    # Make an API call to Tenor using the 'requests' library
    # Get the first 10 results from the search results
    if trending:
        r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" %
                         (params['key'], params['limit']))
    else:
        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (params['q'], params['key'], params['limit']))

    json_data = r.json()['results']
    for i in range(len(json_data)):
        url = json_data[i]['media'][0]['gif']['url']
        urls.append(url)
    # print(urls)
    # Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", urls=urls, trending=trending)


if __name__ == '__main__':
    app.run(debug=True)
