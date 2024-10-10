import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

os.system("cls || clear")

# Criando banco de dados
db = create_engine("sqlite:///banco_alunos.db")

Session = sessionmaker(bind=db)
session = Session()

Tabela = declarative_base()

class Alunos(Tabela):
    __tablename__ = "alunos"

    ra = Column("R.A", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    idade = Column("idade", Integer)
    email = Column("email", String)

    def __init__(self, nome: str, email: str, idade: str) -> None:
        self.nome = nome
        self.idade = idade
        self.email = email

Tabela.metadata.create_all(bind=db)

for i in range(1):
    nome = input("Digite seu nome: ")
    idade = input("Digite seu idade: ")
    email = input("Digite seu e-mail: ")

    aluno = Alunos(nome=nome, idade=idade, email=email)
    session.add(aluno)
    session.commit()
    print()

# Mostrando conteúdo do bando de dados.
print("Lista de usuários do banco de dados: ")
lista_alunos = session.query(Alunos).all()

for aluno in lista_alunos:
    print(f"R.A: {aluno.ra} - Nome: {aluno.nome} - Idade: {aluno.idade} - E-mail: {aluno.email}")

aluno = session.query(Alunos).filter_by(email = "Rafaelsd@...").first()
session.delete(aluno)
session.commit()
print(f"Usuário {aluno.ra} foi deletado com sucesso!")

print("\nLista de usuários do banco de dados: ")
lista_alunos = session.query(Alunos).all()

for aluno in lista_alunos:
    print(f"R.A: {aluno.ra} - Nome: {aluno.nome} - Idade: {aluno.idade} - E-mail: {aluno.email}")