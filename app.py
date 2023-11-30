import random, short_url, string
from flask import Flask, render_template, request, redirect



#variables
app = Flask(__name__)
short_prefix = "www.short.url/"
long_urls = {}
short_urls = {}
url_store = {}

def store_url(url):
    return print(long_urls, short_urls)

#TODO: add longurl as a key and shortcode as a value to url_store Dictionary.
#below is the function that will shorten the url given by the user
def shorten_url(url):
    if url in long_urls and shortcode in shortcode: 
        return short_urls[url]
    else:
        shortcode = request.form.get('shortcode')
        short_url = short_prefix + shortcode
        short_urls[url] = short_url + shortcode
        return short_url 
   
#below is the function that will handle the request from the user
@app.route('/', methods=['POST'])
def shortener():
    if request.method == 'POST':
        data = request.form.to_dict('url', 'shortcode')
        data['shortcode'] = "url"
        url = request.form.get('url') 
        short_url = shorten_url(url)
        short_urls[short_url] = url
        print(data)
        return render_template('shortened-url.html', short_url=short_url)
    return render_template('shortener.html')

'''
#error codes TODO: implement these errorcodes in process


#errorhandeling variables for html pages
error400 - "Url not present"
error404 - "Shortcode not found"
error409 - "Shortcode already in use"
error412 = "The provided shortcode is invalid"

#Handling error 400 and displaying relevant web page
@app.error_handler(400)
def not_found_error(error):
    return render_template('error400.html'),400
 
#Handling error 404 and displaying relevant web page
@app.error_handler(404)
def internal_error(error):
    return render_template('error404.html'),404
 
#Handling error 409 and displaying relevant web page
@app.error_handler(409)
def not_found_error(error):
    return render_template('error409.html'),409
 
#Handling error 412 and displaying relevant web page
@app.error_handler(412)
def internal_error(error):
    return render_template('error412.html'),412
'''

if __name__ == '__main__':
    app.run(port=9999)