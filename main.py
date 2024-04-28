from flask import Flask, redirect, request
import string
import random

# Initialize Flask app
app = Flask(__name__)

# Dictionary to store short URL as key and long URL as value
url_database = {}


# Function to generate a random 8-character string for short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(8))
    return short_url


# Route for the home page
@app.route('/')
def home():
    """
    Route handler for the home page.

    Returns:
        str: HTML content for the home page of the URL Shortener.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>URL Shortener</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the URL Shortener!</h1>
        <p>This is a simple URL shortening service built with Flask.</p>
        <p> Konstantinos Pavlakis </p>
    </body>
    </html>
    """
    return html_content


# Route to handle shortening
@app.route('/shorten', methods=['POST'])
def shorten_url():
    """
    Route handler to shorten a URL.

    Returns:
        str: Confirmation message with the shortened URL.
    """
    long_url = request.form['url']
    short_url = generate_short_url()
    url_database[short_url] = long_url
    return f'Shortened URL: http://localhost:5000/redirect/{short_url} has been created successfully!'


# Route to handle redirection
@app.route('/redirect/<short_url>')
def redirect_to_long_url(short_url):
    """
    Route handler to redirect to a long URL.

    Example:
        curl -X POST -d "url=https://www.facebook.com" http://localhost:5000/shorten
    Args:
        short_url (str): Short URL to redirect to the corresponding long URL.

    Returns:
        redirect: Redirects to the corresponding long URL if found, else returns a 404 error.
    """
    if short_url in url_database:
        long_url = url_database[short_url]
        return redirect(long_url)
    else:
        return 'Shortened URL not found', 404



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
