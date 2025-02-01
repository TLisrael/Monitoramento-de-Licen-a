from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Software(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    versao = db.Column(db.String(50), nullable=False)
    fornecedor = db.Column(db.String(120), nullable=False)
    data_aquisicao = db.Column(db.Date, nullable=False)
    data_expiracao = db.Column(db.Date, nullable=False)
    numero_licenca = db.Column(db.String(50), nullable=False)
    instalacoes = db.relationship('Instalacao', backref='software', lazy=True)

class Instalacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dispositivo = db.Column(db.String(120), nullable=False)
    usuario = db.Column(db.String(120), nullable=False)
    data_instalacao = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'), nullable=False)
