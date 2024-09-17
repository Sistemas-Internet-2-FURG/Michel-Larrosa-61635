from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from app.auth import check_permission
from app.models import cria_user
import logging

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

# Definindo um blueprint para as rotas principais
main_routes = Blueprint('main_routes', __name__)

# Rota PÚBLICO (acesso livre a todos)
# testar assim e depois mudar "/publico" para "/"
@main_routes.route('/')
def publico():
    return render_template('index.html')

# Rota ALUNOS (PROFESSOR e superiores)
@main_routes.route('/alunos')
def alunos():
    if not check_permission('PROFESSOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('alunos.html')

# Rota TURMAS (COORDENADOR e superiores)
@main_routes.route('/turmas')
def turmas():
    if not check_permission('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('turmas.html')

@main_routes.route('/turmas/incluir')
def turmas_incluir():
    if not check_permission('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    if request.method == 'POST':
        campos_necessarios = ['identificador', 'disciplina', 'professor']
        dados = {campo: request.form.get(campo) for campo in campos_necessarios}
        if all(dados.values()):
            from flask import current_app  # Usar current_app para acessar o logger
            current_app.logger.info("ALL-DADOS-VALUES AFTER")
            identificador = request.form['identificador']
            disciplina = request.form['disciplina']
            professor = request.form['professor']
            cria_turma(identificador, disciplina, professor)
    return render_template('turmas.incluir.html')

@main_routes.route('/turmas/editar')
def turmas_editar():
    if not check_permission('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('turmas.editar.html')

@main_routes.route('/turmas/excluir')
def turmas_excluir():
    if not check_permission('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('turmas.excluir.html')

# ### Rota DIRETOR (somente DIRETOR) ###
@main_routes.route('/equipe')
def equipe():
    if not check_permission('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('equipe.html')



@main_routes.route('/equipe/incluir', methods=['GET', 'POST'])
def equipe_incluir():
    if not check_permission('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    if request.method == 'POST':
        campos_necessarios = ['nome', 'senha', 'cargo']
        dados = {campo: request.form.get(campo) for campo in campos_necessarios}
        if all(dados.values()):
            from flask import current_app  # Usar current_app para acessar o logger
            current_app.logger.info("ALL-DADOS-VALUES AFTER")
            nome = request.form['nome']
            senha = request.form['senha']
            cargo = request.form['cargo']
            cria_user(nome, senha, cargo)
    return render_template('equipe.incluir.html')



@main_routes.route('/equipe/editar')
def equipe_editar():
    if not check_permission('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('equipe.editar.html')

@main_routes.route('/equipe/excluir')
def equipe_excluir():
    if not check_permission('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main_routes.publico'))
    return render_template('equipe.excluir.html')


@main_routes.route('/login_ok')
def login_ok():
        return render_template('login_ok.html')

