# app.py
from flask import Flask, render_template, request, jsonify
import MiniProject_Backend

app = Flask(__name__, static_folder='static', template_folder='templates')
MiniProject_Backend.MovieData()

def row_to_dict(r):
    return {"dbid": r[0], "movie_id": r[1], "name": r[2], "date": r[3],
            "director": r[4], "cast": r[5], "budget": r[6], "duration": r[7], "rating": r[8]}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/movies", methods=["GET"])
def get_movies():
    rows = MiniProject_Backend.ViewMovieData()
    return jsonify([row_to_dict(r) for r in rows])

@app.route("/api/search", methods=["GET"])
def search_movies():
    q = request.args
    rows = MiniProject_Backend.SearchMovieData(q.get("movie_id",""), q.get("name",""), q.get("date",""),
                                              q.get("director",""), q.get("cast",""), q.get("budget",""),
                                              q.get("duration",""), q.get("rating",""))
    return jsonify([row_to_dict(r) for r in rows])

@app.route("/api/movie", methods=["POST"])
def add_movie():
    d = request.json
    MiniProject_Backend.AddMovieRec(d.get("movie_id",""), d.get("name",""), d.get("date",""),
                                   d.get("director",""), d.get("cast",""), d.get("budget",""),
                                   d.get("duration",""), d.get("rating",""))
    return jsonify(success=True)

@app.route("/api/movie/<int:dbid>", methods=["DELETE"])
def delete_movie(dbid):
    MiniProject_Backend.DeleteMovieRec(dbid)
    return jsonify(success=True)

# optional update by delete/add
@app.route("/api/movie/<int:dbid>", methods=["PUT"])
def update_movie(dbid):
    d = request.json
    # delete original
    MiniProject_Backend.DeleteMovieRec(dbid)
    MiniProject_Backend.AddMovieRec(d.get("movie_id",""), d.get("name",""), d.get("date",""),
                                   d.get("director",""), d.get("cast",""), d.get("budget",""),
                                   d.get("duration",""), d.get("rating",""))
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
