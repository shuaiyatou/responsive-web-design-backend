from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/backend')
def backend():
    return render_template('back_stage.html')


@app.route('/backend/user')
def user():
    return render_template('user.html')


@app.route('/backend/content')
def content():
    return render_template('content.html')


@app.route('/backend/tag')
def tag():
    return render_template('tag.html')


@app.route('/backend/user_search')
def user_search():
    return render_template('user_search.html')


@app.route('/backend/add_title')
def add_title():
    return render_template('add_title.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
