from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    #database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    database = SQLAlchemy(app)

    #routes
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/cv', methods = ['POST'])
    def result():
        result = request.form
        return render_template('result.html', result = result)

    return app

if(__name__ == "__main__"):
    app = create_app()
    app.run(debug = True)
