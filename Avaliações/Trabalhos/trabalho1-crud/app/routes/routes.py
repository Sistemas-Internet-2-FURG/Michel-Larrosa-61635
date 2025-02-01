from flask import Blueprint, render_template, redirect, url_for, session, flash, request, jsonify, current_app

import logging
# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)  # Configura o nível do log para DEBUG

from app.routes.auth import acl
from app.routes.auth import acl
from app.models import *

# Definindo um blueprint para as rotas principais
main = Blueprint('main', __name__)

# ROTAS PARA CARREGAMENTO DE TEMPLATES ### ### ROTAS WEB ### ### ### ### ### ### ### ### ### ###

# Rota PÚBLICO (acesso livre a todos)
# Mostrar turmas com número de alunos
# Selecionar/Clicar turma e mostrar a lista de alunos

@main.route('/')
def publico():
    return render_template('index.html')

@main.route('/testes')
def testes():
    return render_template('testes.html')

# Rota ALUNOS (PROFESSOR e superiores)
@main.route('/alunos')
def alunos():
    # if not acl('PROFESSOR'):
    #     flash('Acesso negado.', 'danger')
    #     return redirect(url_for('main.publico'))
    return render_template('alunos.html')

# Rota TURMAS (COORDENADOR e superiores)
@main.route('/turmas')
def turmas():
    # if not acl('COORDENADOR'):
    #     flash('Acesso negado.', 'danger')
    #     return redirect(url_for('main.publico'))
    return render_template('turmas.html')

# Rota DIRETOR (somente DIRETOR)
@main.route('/equipe')
def equipe():
    # if not acl('DIRETOR'):
    #     flash('Acesso negado.', 'danger')
    #     return redirect(url_for('main.publico'))
    return render_template('equipe.html')

# ROTAS ANTIGAS ### ### ROTAS ANTIGAS ### ### ### ### ### ### ### ### ### ###

@main.route('/turmas/incluir')
def turmas_incluir():
    if not acl('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.publico'))
    if request.method == 'POST':
        campos_necessarios = ['identificador', 'disciplina', 'professor']
        dados = {campo: request.form.get(campo) for campo in campos_necessarios}
        if all(dados.values()):
            # current_app.logger.info("ALL-DADOS-VALUES AFTER")
            identificador = request.form['identificador']
            disciplina = request.form['disciplina']
            professor = request.form['professor']
            cria_turma(identificador, disciplina, professor)
    return render_template('turmas.incluir.html')

@main.route('/turmas/editar')
def turmas_editar():
    if not acl('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.publico'))
    return render_template('turmas.editar.html')

@main.route('/turmas/excluir')
def turmas_excluir():
    if not acl('COORDENADOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.publico'))
    return render_template('turmas.excluir.html')


@main.route('/equipe/incluir', methods=['GET', 'POST'])
def equipe_incluir():
    if not acl('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.publico'))
    if request.method == 'POST':
        campos_necessarios = ['nome', 'senha', 'cargo']
        dados = {campo: request.form.get(campo) for campo in campos_necessarios}
        if all(dados.values()):
            # current_app.logger.info("ALL-DADOS-VALUES AFTER")
            nome = request.form['nome']
            senha = request.form['senha']
            cargo = request.form['cargo']
            cria_user(nome, senha, cargo)
    return render_template('equipe.incluir.html')


@main.route('/equipe/editar')
def equipe_editar():
    if not acl('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.publico'))
    return render_template('equipe.editar.html')

@main.route('/equipe/excluir')
def equipe_excluir():
    if not acl('DIRETOR'):
        flash('Acesso negado.', 'danger')
        return redirect(url_for('main.publico'))
    return render_template('equipe.excluir.html')


@main.route('/login_ok')
def login_ok():
        return render_template('login_ok.html')

