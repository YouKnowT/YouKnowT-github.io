from flask import Flask, render_template

app = Flask(__name__)


@app.route('/PlanarTracking')
def homepage():  # put application's code here
    return index()


@app.route('/')
def index():  # put application's code here
    return render_template('PlanarTracking.html')


if __name__ == '__main__':
    app.run()
