from flask import Blueprint, request, redirect, url_for, session, flash, render_template
from app.models import check_login

# Definindo um blueprint para as rotas de autenticação
auth= Blueprint('auth', __name__)

# Rota de login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        campos_necessarios = ['username', 'password']
        dados = {campo: request.form.get(campo) for campo in campos_necessarios}
        if all(dados.values()):
            username = request.form['username']
            password = request.form['password']
            user = check_login(username, password)
            # print(f'Todos os campos foram enviados corretamente: {dados}')
            if user:
                session['username'] = user[1]
                session['nivel_user'] = user[3]
                flash('Login efetuado com sucesso!', 'success')

                # Definindo cookie opcionalmente
                response = redirect(url_for('main_routes.publico'))
                response.set_cookie('username', username)
                return response
            else:
                flash('Credenciais inválidas.', 'danger')
        else:
            print(f'Faltando ou vazio: {campos_faltando}')
    return render_template('login_ok.html')

# Rota de logout
@auth.route('/logout')
def logout():
    session.clear()
    flash('Logout efetuado com sucesso!', 'success')

    # Removendo cookie opcional
    response = redirect(url_for('auth_routes.login'))
    response.set_cookie('username', '', expires=0)
    return response

# Função para verificar permissões
def acl(nivel_necessario):
    if 'nivel_user' not in session:
        return False
    nivel_user = session['nivel_user']
    # ### sempre nessa ordm
    roles = ['PÚBLICO', 'PROFESSOR', 'COORDENADOR', 'DIRETOR']
    return roles.index(nivel_user) >= roles.index(nivel_necessario)
