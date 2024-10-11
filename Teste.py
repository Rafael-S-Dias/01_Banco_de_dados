import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

os.system("cls || clear")

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
for i in range(2):
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite seu senha: ")

    usuario = Usuario(nome=nome,email=email, senha=senha)
    session.add(usuario)
    session.commit()
    print()

# Mostrando conteúdo do bando de dados.
print("Lista de usuários do banco de dados: ")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

# Deletando um usuário.
print("\nExcluindo usuário no banco de dados: ")
email_usuario = input("Informe o e-mail do usuário: ")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
if usuario:
    session.delete(usuario)
    session.commit()
    print(f"Usuário {usuario.nome} foi deletado com sucesso!")
else:
    print("Usuário não encontrado.")

# Mostrando conteúdo do bando de dados.
print("\nLista de usuários do banco de dados: ")
lista_usuarios = session.query(Usuario).all()

# Atualizar um  usuário.
print("\nAtualizando os dados de um usuário: ")
email_usuario = input("Informe o e-mail do usuário: ")

usuario = session.query(Usuario).filter_by(email = email_usuario ).first()

if usuario:
    usuario.nome = input("Digite seu nome: ")
    usuario.email = input("Digite seu e-mail: ")
    usuario.senha = input("Digite seu senha: ")
    session.commit()
else:
    print("Usuário não encontrado.")

# Pesquisando um usuário.
print("\nPesquisando um usuário pelo e-mail: ")
email_usuario = input("Informe o e-mail do usuário: ")

usuario = session.query(Usuario).filter_by(email = email_usuario ).first()
if usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
else:
    print("Usuário não encontrado.")

#Fechando conexão
session.close()