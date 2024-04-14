from flask import Flask, render_template
from dict import pages

app = Flask(__name__, static_folder="Stylesheets")


@app.route('/')
def index():
    bob = ""
    return render_template('index.html', pages=pages)

@app.route('/<categorie>/<page>')
def pageName(categorie, page):
    return render_template('pagina.html', opera=pages[categorie][page])

app.run(debug=True)