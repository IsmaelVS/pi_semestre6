"""Modulo para as rotas de login."""
from flask import (
    abort,
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
    json
)
from sistema_hotel.models.db_functions import query_user

app = Blueprint('login', __name__)


@app.route('/', methods=['GET'])
def view():
    return render_template('login.html',
                           login_error='false')


@app.route('/', methods=['POST'])
def do_login():
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    user = query_user(username=username, pwd=pwd)
    if user and pwd == user.pwd:
        return render_template('Menu_Principal.html')
    return render_template('login.html',
                           login_error='true')


@app.route('/api_login', methods=['POST','GET'])
def login_api():
    username = request.form.get('username')
    pwd = request.form.get('pwd')
    user = query_user(username=username, pwd=pwd)
    if user and pwd == user.pwd:
        result = {'user':user.username,'name':user.name,'adm':user.is_adm,'is_authenticated':1}
    else:
        result = {'user':username,'is_authenticated':0}

    return jsonify(result)


