from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect("books-collection.db", check_same_thread=False)
cursor = db.cursor()
#database

""" def create_database():    
    try:
        cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
    except sqlite3.OperationalError as e:
        return print('Table exist')
create_database()  """

def insert_database(pk, title, author, rating):
    try:
        cursor.execute(f"INSERT INTO books (id, title, author, rating) VALUES (?, ?, ?, ?)", (pk, title, author, rating))
        db.commit()
    except Exception as e:
        return str(e)

all_books = []

@app.route('/')
def home():
    return render_template('index.html', books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    pk = len(all_books) + 1
    if request.method == 'POST':
        all_books.append(
            {
                'id': pk,
                'title': request.form.get('title'),
                'author': request.form.get('author'),
                'rating': float(request.form.get('rating'))
            }
        )
        insert_database(
            pk=pk,
            title=request.form.get('title'),
            author=request.form.get('author'),
            rating=float(request.form.get('rating'))
        )
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)

