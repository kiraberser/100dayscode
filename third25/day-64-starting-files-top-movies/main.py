from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

from api import TMDBMovieFetcher

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-website.db"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(200), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>' 

class EditForm(FlaskForm):
    update_rating = FloatField('Your rating Out of 10 e.g 7.5', validators=[DataRequired()])
    update_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

#with app.app_context():
#    db.session.add(second_movie)
#    db.session.commit()

@app.route("/")   
def home():
    all_movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html", movies=all_movies)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        TMDB = TMDBMovieFetcher(query=movie_title)
        TMDB.fetch_movies()
        data = TMDB.get_titles_and_date()
        return render_template('select.html', title_and_date=data)
    return render_template('add.html', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    update_review = form.update_review.data
    update_rating = form.update_rating.data
    if form.validate_on_submit():
        with app.app_context():
            update_movie = db.one_or_404(db.select(Movie).filter_by(id=movie_id))
            update_movie.rating = update_rating
            update_movie.review = update_review
            db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('edit.html', form=form, id=movie_id)

@app.route('/delete/<int:movie_id>', methods=['GET'])
def delete(movie_id):
    with app.app_context():
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
