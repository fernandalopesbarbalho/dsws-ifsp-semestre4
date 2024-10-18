from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>/<register>/<institution>')
def user(name, register, institution):
    return render_template('user.html', name=name, register=register, institution=institution)

@app.route('/contextorequisicao/<name>')
def contexto_requisicao(name):
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.headers.get('Host')
    return render_template('contexto.html', name=name, user_agent=user_agent, ip=ip, host=host)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500