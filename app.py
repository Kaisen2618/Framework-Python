from flask import Flask, request
from models.task import Task

app =  Flask(__name__)

#CRUD
#Create, Read, Update, and Delete = Criar, Ler, Atualizar e Deletar

@app.route('/')
def hello_world():
    return "Hello World!"

tasks = []

@app.route('/tasks', methods = ['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True)