from links import links

from flask import (
        Flask,
        render_template,
        )


app = Flask(__name__, static_folder='static')

@app.route('/',methods=['GET', 'POST'])
def index():
    cursos= links()

    return render_template('index.html',cursos=cursos)



@app.errorhandler(404)
def error(e):
    return '<h1>ocorreu um error, Tente Mais tarde</h1>'



if __name__ == '__main__':
    import os
 
    host = '0.0.0.0'
    port  = int(os.environ.get("PORT", 5000))
 
    app.run(host, port)
