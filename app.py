from flask import Flask, render_template, request, url_for
from  apithing import movie_resource
import os
app = Flask(__name__)

@app.route('/')
def index():
    print(os.getcwd())
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/music')
def music():
   return render_template('music.html') 
   
  

@app.route('/movies')
def movies():
    return render_template('movies.html',  genre = movie_resource.list_genres_all())


@app.route('/action_page')
def action_page():
  def movie_to_displ():
      movie_to_displ =movie_resource.ttle_naming(movie_resource.popular_movies(request.args.get('movie', type = str)))
      return dict(movie_to_displ)
  def img():
      image = movie_to_displ.get('image')
      return image
  return render_template('action_page.html', film=movie_to_displ(), image =img())