# Ryan Bachman
# University of Advancing Technology
# MS587, Databases and Web Development
# Summer 2024, Grad 1
# Assignment 2.1 - Building Your Own eBook and Audiobook Web Application

from flask import Flask, render_template, send_file, request, session, redirect, url_for

import book_database
from book_database import data, BOOKS, get_books, get_specific_book, get_book_details, db_session, Book, BookDetails
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
    """Views for the book details that a user can pick to read from the database."""
    try:
        books = get_books()
        return render_template('Reading.html', books=books)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route('/second/<book_id>')
def ereader_page(book_id):
    """Views for the book details that a user can pick to read from the database."""
    try:
        books = get_specific_book(book_id)
        book_details = get_book_details(book_id)

        text_to_speech("Hello, my name is Ryan!", "Male")

        return render_template('eReader.html', books=books, book_details=book_details)
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@app.route('/third')
def reference_page():
    """Views for the city details"""
    return render_template('References.html')


def text_to_speech(text, gender):
    """
    Function to convert text to speech
    :param text: text
    :param gender: gender
    :return: None
    """
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    app.run()