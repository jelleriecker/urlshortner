from flask import Flask, render_template, request, redirect
import short_url
import string



app = Flask(__name__)
shortened_urls = {}
root_url = "short.url/"


def generate_short_url(length=8):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url.encode_url(l)

@app.route('/', methods=['GET', 'POST'])
def shortener():
    if request.method == 'POST':
        long_url = request.form['url']
        short_url = generate_short_url(long_url)
        shortcode = request.form['shortcode']
        while short_url in short_url:
            short_url = generate_short_url(long_url)
        return f"shortened URL: {request.root_url}{short_url}{shortcode}"
    return render_template('shortener.html')

@app.route('/short_url')
def short_url():
    return render_template('shortened-url.html')




if __name__ == '__main__':
    app.run(debug=True)