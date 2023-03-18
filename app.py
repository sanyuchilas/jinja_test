from flask import Flask, render_template, request

app = Flask(__name__)

class Card:
    def __init__(self, title, body):
        self.title = title
        self.body = body

cards = [
    Card('Todo', 'Сделать template'),
    Card('Done', 'Защитить проект')
]

@app.route('/')
def index():
    return render_template('index.html.j2',
        cards=cards,
        test=True
    )
@app.route('/card/', methods=['POST'])
def create_card():
    body = request.json

    return ['adafadf', 'aafadf']