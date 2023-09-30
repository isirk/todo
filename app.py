from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
items = {}

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    text = request.form['text']
    items[len(items) + 1] = {'text': text, 'done': False}
    return redirect(url_for('index'))

@app.route('/done/<int:id>')
def done(id):
    items[id]['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)