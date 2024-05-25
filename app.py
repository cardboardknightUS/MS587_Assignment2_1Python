# Ryan Bachman
# University of Advancing Technology
# MS587, Databases and Web Development
# Summer 2024, Grad 1
# Assignment 2.1 - Building Your Own eBook and Audiobook Web Application

from flask import Flask, render_template, send_file, request, session, redirect, url_for
from book_database import data, BOOKS, get_books, get_book_summary, db_session
import pyttsx3


app = Flask(__name__)


def get_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'


@app.route('/')
def main():
    """Entry point; the view for the main page"""
    return render_template('index.html')


@app.route('/second')
def reading_page():
    """Views for the city details"""
    return render_template('Reading.html')


@app.route('/third')
def reference_page():
    """Views for the city details"""
    return render_template('References.html')


if __name__ == '__main__':
    app.run()
    # hello_world()
    # engine = pyttsx3.init()
    # engine.say('Sally sells seashells by the seashore.')
    # engine.say('The quick brown fox jumped over the lazy dog.')
    # engine.runAndWait()
