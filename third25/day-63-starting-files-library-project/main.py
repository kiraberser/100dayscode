from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer,  String, Float
import sqlite3
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app, db)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    def __repr__(self):
        return f'<Book {self.title}>'    
    
@app.route('/')
def home():
    return render_template('index.html', books=Book.query.all())

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            rating=request.form.get('rating')
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    book_id = request.args.get('id')
    if request.method == 'GET':
        book_to_update = Book.query.get(book_id)
        return render_template('edit.html', book=book_to_update)    
    
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.get_or_404(Book, book_id)  
            book_to_update.rating = request.form['rating']
            db.session.commit()
        return redirect(url_for('home'))

@app.route('/delete/<int:book_id>', methods=['GET'])
def delete(book_id):
    with app.app_context():
        book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)


# CRUD WITH FLASK

#with app.app_context():
#    #All
#    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
#    
#    #Read by query
#    book = db.session.execute(db.select(Book).where(Book.title == 'Habitos Atomicos')).scalar()
#    
#    #Update by query
#    book_to_update = db.session.execute(db.select(Book).where(Book.title == 'Habitos Atomicos')).scalar()
#    book_to_update.title = "Atomic Habits"
#    
#    #Update by Primary Key
#    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#    # or book_to_update = db.get_or_404(Book, book_id)  
#    book_to_update.title = "Harry Potter and the Goblet of Fire"
#    db.session.commit()  
#
#    #Delete by Primary Key
#    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#    # or book_to_delete = db.get_or_404(Book, book_id)
#    db.session.delete(book_to_delete)
#    db.session.commit()
