import random, short_url, string
from flask import Flask, render_template, request, redirect



#variables
app = Flask(__name__)
short_prefix = "www.short.url/"
long_urls = {}
short_urls = {}

def store_url(url):
    return print(long_urls, short_urls)

#below is the function that will shorten the url given by the user
def shorten_url(url):
    if url in long_urls and shortcode in shortcode:
        return short_urls[url]
    else:
        shortcode = request.form.get('shortcode')
        short_url = short_prefix + shortcode
        short_urls[url] = short_url + shortcode
        for lurl in long_urls:
            long_urls + shortcode
            
        return short_url 
   
#below is the function that will handle the request from the user
@app.route('/', methods=['GET', 'POST'])
def shortener():
    if request.method == 'POST':
        url = request.form.get('url')
        short_url = shorten_url(url)
        short_urls[short_url] = url
        return render_template('shortened-url.html', short_url=short_url)
    return render_template('shortener.html')

if __name__ == '__main__':
    app.run(debug=True, port=9999)