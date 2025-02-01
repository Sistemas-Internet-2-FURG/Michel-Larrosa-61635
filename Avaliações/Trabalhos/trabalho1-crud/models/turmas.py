from flask import current_app, jsonify
from app.models import db

# ### ### ### ### ### ### DEFINIÇÃO DA CLASSE TURMAS ### ### ### ### ### ###

class Turma(db.Model):
    __tablename__ = 'turmas'
    identificador = db.Column(db.String(50), primary_key=True)
    disciplina = db.Column(db.String(100), nullable=False)
    professor = db.Column(db.Integer, db.ForeignKey('equipe.matricula'), nullable=False)
    # relações estrangeiras
    alunos = db.relationship('Aluno', backref='turma_ref', lazy=True)

    def __repr__(self):
        return f"<Turma {self.identificador}: {self.disciplina}, Professor: {self.professor}>"


# ### ### ### ### ### ### GERENCIAMENTO DE TURMAS ### ### ### ### ### ###
# from models.turmas import Turma # descomentar caso as funções ñ fiquem no arquivo da classe

def inserir_turma(identificador, disciplina, professor):
    try:
        turma = db.session.query(Turma).filter_by(identificador=identificador).first()
        if turma:
            return {"message": "Turma Já existente", "status":409}, 409
        novo_turma = Turma(identificador=identificador, disciplina=disciplina, professor=professor)
        db.session.add(novo_turma)
        db.session.commit()
        return {"message": "Turma criado com sucesso", "status":201}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

def obter_turmas():
    try:
        result = db.session.query(Turma).with_entities(Turma.identificador, Turma.disciplina, Turma.professor).order_by(Turma.identificador)
        turmas = [dict(row) for row  in result]
        return {"Turmas":turmas}, 200
    except Exception as e:
        return {"message": f"Erro ao buscar turmas: {str(e)}"}, 500

def ler_turma(identificador):
    try:
        turma = db.session.query(Turma).filter_by(identificador=identificador).first()
        if turma:
            return jsonify({
                "identificador": turma.identificador,
                "disciplina": turma.disciplina,
                "professor": turma.professor
            }), 200
        return {"error": "Turma não encontrado"}, 404
    except Exception as e:
        return {"error": str(e)}, 500

def editar_turma(identificador, disciplina, professor):
    if not (professor and disciplina):
        return {"Bad Request": "Todos os campos devem ser fornecidos para PUT"}, 400
    try:
        turma = db.session.query(Turma).filter_by(identificador=identificador).first()
        if turma:
            if disciplina:
                turma.disciplina = disciplina
            if professor:
                turma.professor = professor
            db.session.commit()
            return {"message": "Turma editado com sucesso", "status":200}, 200
        return {"error": "Turma não encontrado"}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def editar_parcialmente_turma(identificador, disciplina=False, professor=False):
    if not (professor or disciplina):
        return {"Bad Request": "Pelo menos um campo opcional deve ser fornecido para PATCH"}, 400
    try:
        turma = db.session.query(Turma).filter_by(identificador=identificador).first()
        if turma:
            if professor:
                turma.professor = professor
            if disciplina:
                turma.disciplina = disciplina
            db.session.commit()
            return {"message": "Turma editado com sucesso", "status":200}, 200
        return {"error": "Turma não encontrado"}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def delete_turma(identificador):
    try:
        turma = db.session.query(Turma).filter_by(identificador=identificador).first()
        if turma:
            db.session.delete(turma)
            db.session.commit()
            return {}, 204
        return {"error": "Turma não encontrado", "status":404}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e), "status":500}, 500
