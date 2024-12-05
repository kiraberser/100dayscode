from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

from api import TMDBMovieFetcher

from models import Movie, db
from models import EditForm, AddForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-website.db"
Bootstrap5(app)

db.init_app(app)

# 1.-Home page where you can see and add your movies 
@app.route("/")   
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    movies = list(all_movies)
    for index, movie in enumerate(movies, start=1):
        movie.ranking = index
    db.session.commit()
    movies.reverse()
    return render_template("index.html", movies=movies)

# 2.-User put the name of the movie and the api TMBD search the title and date  
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        movie_data = TMDBMovieFetcher(query=movie_title)
        movie_data.fetch_movies()
        data = movie_data.get_titles_and_date()
        return render_template('select.html', title_and_date=data)
    return render_template('add.html', form=form)

# 3.- When the user select the movie, the id is passed and search for the details of the movie
@app.route('/add-movie-details/<int:movie_id>', methods=['GET'])
def fetch_movie_details(movie_id):
    movie_details = TMDBMovieFetcher(query='')
    get_movie_details = movie_details.get_movies_details(movie=movie_id) 
    img_url = 'https://image.tmdb.org/t/p/original' + get_movie_details.get('poster_path')
    year = get_movie_details.get('release_date')
    if get_movie_details:
        new_movie = Movie(
            title=get_movie_details.get('original_title'),
            description=get_movie_details.get('overview'),
            img_url=img_url,
            year=year.split('-')[0]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', id=new_movie.id))
    else: 
        print('Error')

# 4.- When is added a movie, don't have any review or rating, the data should be created
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    update_review = form.update_review.data
    update_rating = form.update_rating.data
    if form.validate_on_submit():
        update_movie = db.get_or_404(Movie, movie_id)
        update_movie.rating = update_rating
        update_movie.review = update_review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)

@app.route('/delete/<int:movie_id>', methods=['GET'])
def delete(movie_id):
    with app.app_context():
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
