from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    #return "hello!".decode('cp1251').encode('utf8')
    return "А вот и сайтик"

app.run(port=8000)
