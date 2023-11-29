import random, short_url, string
from flask import Flask, render_template, request, redirect



#variables
app = Flask(__name__)
shortened_urls = {}
shorty_prefix = "http://short.url/"
url_store = {}

def shorten_url(url):
    if url in url_store:
        return url_store[url]
    else:
        short_url = shorty_prefix + ''.join(random.choice(string.ascii_letters) for i in range(5))
        url_store[url] = short_url
        return short_url
   

@app.route('/', methods=['GET', 'POST'])
def shortener():
    if request.method == 'POST':
        url = request.form.get('url')
        short_url = shorten_url(url)
        shortened_urls[short_url] = url
        return render_template('shortened-url.html', short_url=short_url)
    return render_template('shortener.html')


@app.route('/<short_url>')
def short_url():
    
    return render_template('shortened-url.html')



if __name__ == '__main__':
    app.run(debug=True)