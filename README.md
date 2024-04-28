Flask URL Shortener
The Flask URL Shortener is a simple web application built with Flask, a lightweight Python web framework. It allows users to shorten long URLs into concise, easy-to-share links.

Features
URL Shortening: Shorten long URLs into shorter, more manageable links.
Redirection: Automatically redirect users to the original long URLs when they access the shortened links.
Random Short URLs: Generate unique short URLs using a random combination of letters and numbers.
User-friendly Interface: Clean and intuitive web interface for generating and sharing shortened URLs.
Debugging: Includes debugging features for troubleshooting and monitoring server activity.
Deployment: Easy deployment on local machines for testing and development.
Technologies Used
Flask: Lightweight web framework for Python.
HTML/CSS: Designing the user interface and styling the web pages.
Python: Backend logic and URL generation.
Random Module: Generating random characters for short URLs.
HTTP Status Codes: Handling redirection and error responses.
Usage
The Flask URL Shortener can be interacted with using curl or Postman:

Using curl:
bash
Copy code
curl -X POST -d "url=YOUR_LONG_URL_HERE" http://localhost:5000/shorten
Using Postman:
Method: POST
URL: http://localhost:5000/shorten
Body: Select "x-www-form-urlencoded" and add the long URL as a key-value pair.
Once you have the shortened URL, you can share it with others for easy access to the original link.
