from flask import Blueprint,jsonify

main = Blueprint('main', _name_)

@main.route('/add_movie', methods = ['POST'])
def add_movie()
return 'Done',201


@main.route('/movies', methods = ['POST'])
def movies()

movies = []

return jsonify({'movies' : movies})