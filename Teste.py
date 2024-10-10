import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
db = create_engine("sqlite:///meubanco.db")
# Conexão com o banco de dados
Session = sessionmaker(bind=db)
session = Session()

# Criando tabela
Base = declarative_base()

class Usuario(Base):
    # Definindo tabela.
    __tablename__ = "usuarios"

    # Definindo atributos de tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)


    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

#Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

# Salvar no banco de dados.
usuario = Usuario(nome="Rafael", email="Rafaelsd@...", senha="123456")
session.add(usuario)
session.commit()

# Mostrando conteúdo do bando de dados.
print("Lista de usuários do banco de dados: ")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

# Deletando um usuário.
usuario = session.query(Usuario).filter_by(email = "Rafaelsd@...").first()
session.delete(usuario)
session.commit()
print(f"Usuário {usuario.nome} foi deletado com sucesso!")

# Mostrando conteúdo do bando de dados.
print("\nLista de usuários do banco de dados: ")
lista_usuarios = session.query(Usuario).all()