import psycopg2


class Pessoa:

    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='banco_python', user='postgres', password='admin')

    def cadastrar_pessoa(self, usuario, senha):
        cursor = self.connection.cursor()
        cursor.execute(
            'insert into pessoa (usuario, senha) values (%s, %s)', (usuario, senha))
        self.connection.commit()
        self.connection.close()

    def editar_pessoa(self, id, usuario, senha):
        cursor = self.connection.cursor()
        cursor.execute(
            'update pessoa set usuario = %s, senha = %s where id = %s', (usuario, senha, id))
        self.connection.commit()
        self.connection.close()

    def buscar_pessoas(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from pessoa')
        recset = cursor.fetchall()
        self.connection.close()
        return recset

    def buscar_pessoa_id(self, idpessoa):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from pessoa where id = '{idpessoa}'")
        recset = cursor.fetchone()
        self.connection.close()
        return recset

    def buscar_pessoa_usuario_senha(self, usuario, senha):
        cursor = self.connection.cursor()
        cursor.execute("select * from pessoa where usuario = %s and senha = %s", (usuario, senha))
        result = cursor.fetchone()
        self.connection.close()
        return result
