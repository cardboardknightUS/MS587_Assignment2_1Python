from sqlalchemy import MetaData, create_engine, Integer, String, Float, ForeignKey, Column
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

metadata = MetaData()
engine = create_engine('sqlite:///book_database', connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()


# Table for books.
class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_name = Column(String)
    book_summary = Column(String)
    book_genre = Column(String)
    book_details_data = relationship("BookDetails", backref="books")


# Table for book details.
class BookDetails(Base):
    __tablename__ = 'book_details'
    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('books.book_id'))
    book_summary = Column(String)


# Retrieving data from the database
def get_books():
    return db_session.query(Book)


# Generating the summaries of the books in the book_details table.
def get_book_summary(books):
    return [book_id.book_summary for book_id in books.book_details_data]


data = get_books()
BOOKS = [books.book_name for books in data]