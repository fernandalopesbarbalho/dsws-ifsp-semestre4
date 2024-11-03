from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'fhoeo67g293bsdt62h#5555&gididwei'

class UserInfoForm(FlaskForm):
    name = StringField('Informe o seu nome', validators=[DataRequired()])
    surname = StringField('Informe o seu sobrenome', validators=[DataRequired()])
    institution = StringField('Informe a sua Instituição de ensino', validators=[DataRequired()])
    discipline = SelectField('Informe a sua disciplina', choices=[
        ('DSWA5', 'DSWA5'),
        ('DWBA4', 'DWBA4'),
        ('Gestão de projetos', 'Gestão de projetos')
    ])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserInfoForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        new_name = form.name.data

        if old_name and old_name != new_name:
            flash('Você alterou o seu nome!')

        session['name'] = new_name
        session['surname'] = form.surname.data
        session['institution'] = form.institution.data
        session['discipline'] = form.discipline.data
        session['ip'] = request.remote_addr
        session['host'] = request.host

        return redirect(url_for('index'))

    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        surname=session.get('surname'),
        institution=session.get('institution'),
        discipline=session.get('discipline'),
        ip=session.get('ip', 'None'),
        host=session.get('host', 'None'),
        current_time=datetime.utcnow()
    )

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