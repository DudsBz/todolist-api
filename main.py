from flask import Flask, render_template
from tarefa import buscar_tarefas
app = Flask(__name__)


@app.route('/home/<usuario>')
def login(usuario):
    return render_template('index.html', usuario=usuario)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/tarefas')
def get_tarefa():
    tarefas = buscar_tarefas()
    return tarefas

if __name__ == '__main__':
    app.run(debug=True)