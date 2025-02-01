from flask import current_app, jsonify
from app.models import db

# ### ### ### ### ### ### DEFINIÇÃO DA CLASSE EQUIPE ### ### ### ### ### ###

class Equipe(db.Model):
    __tablename__ = 'equipe'
    matricula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)
    # relações estrangeiras
    cargos = db.relationship('Turma', backref='professor_ref', lazy=True)

    def __repr__(self):
        return f"<Equipe {self.matricula}: {self.nome}, Cargo: {self.cargo}>"


# ### ### ### ### ### ### GERENCIAMENTO DE EQUIPE ### ### ### ### ### ###
# from models.equipe import Equipe # descomentar caso as funções ñ fiquem no arquivo da classe

def inserir_equipe(matricula, nome):
    try:
        equipe = db.session.query(Equipe).filter_by(matricula=matricula).first()
        if equipe:
            return {"message": "Equipe Já existente", "status":409}, 409
        # ação padrão: primeiro acesso senha = identificação
        # ação padrão: cadastro inicial como PÚBLICO
        novo_equipe = Equipe(matricula=matricula, nome=nome, cargo="PÚBLICO", senha=matricula)
        db.session.add(novo_equipe)
        db.session.commit()
        return {"message": "Equipe criado com sucesso", "status":201}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

def obter_equipes():
    try:
        result = db.session.query(Equipe).with_entities(Equipe.matricula, Equipe.nome, Equipe.cargo).order_by(Equipe.matricula)
        equipes = [dict(row) for row  in result]
        return {"Equipes":equipes}, 200
    except Exception as e:
        return {"message": f"Erro ao buscar equipes: {str(e)}"}, 500

def ler_equipe(matricula):
    try:
        equipe = db.session.query(Equipe).with_entities(Equipe.matricula, Equipe.nome, Equipe.cargo).filter_by(matricula=matricula).first()
        if equipe:
            return jsonify({
                "matricula": equipe.matricula,
                "nome": equipe.nome,
                "cargo": equipe.cargo
            }), 200
        return {"error": "Equipe não encontrado"}, 404
    except Exception as e:
        return {"error": str(e)}, 500

def editar_equipe(matricula, nome, cargo, senha):
    if not (cargo and nome and senha):
        return {"Bad Request": "Todos os campos devem ser fornecidos para PUT"}, 400
    try:
        equipe = db.session.query(Equipe).filter_by(matricula=matricula).first()
        if equipe:
            if nome:
                equipe.nome = nome
            if cargo:
                equipe.cargo = cargo
            if senha:
                equipe.senha = senha
            db.session.commit()
            return {"message": "Equipe editado com sucesso", "status":200}, 200
        return {"error": "Equipe não encontrado"}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def editar_parcialmente_equipe(matricula, nome=False, cargo=False, senha=False):
    if not (cargo or nome or senha):
        return {"Bad Request": "Pelo menos um campo opcional deve ser fornecido para PATCH"}, 400
    try:
        equipe = db.session.query(Equipe).filter_by(matricula=matricula).first()
        if equipe:
            if cargo:
                equipe.cargo = cargo
            if nome:
                equipe.nome = nome
            if senha:
                equipe.senha = senha
            db.session.commit()
            return {"message": "Equipe editado com sucesso", "status":200}, 200
        return {"error": "Equipe não encontrado"}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def delete_equipe(matricula):
    try:
        equipe = db.session.query(Equipe).filter_by(matricula=matricula).first()
        if equipe:
            db.session.delete(equipe)
            db.session.commit()
            return {}, 204
        return {"error": "Equipe não encontrado", "status":404}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e), "status":500}, 500

