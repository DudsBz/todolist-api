from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home/<usuario>')
def login(usuario):
    return render_template('index.html', usuario=usuario)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)