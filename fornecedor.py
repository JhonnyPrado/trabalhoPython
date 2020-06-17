import psycopg2


class Fornecedor:

    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='banco_python', user='postgres', password='admin')

    def cadastrar_fornecedor(self, nome):
        cursor = self.connection.cursor()
        cursor.execute('insert into fornecedor (nome, status) values (%s, %s)', (nome, True))
        self.connection.commit()

    def editar_fornecedor(self, id, nome):
        cursor = self.connection.cursor()
        cursor.execute(
            'update fornecedor set nome = %s where id = %s', (nome, id))
        self.connection.commit()

    def buscar_fornecedores(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from fornecedor')
        recset = cursor.fetchall()
        return recset

    def buscar_fornecedor_id(self, idforncedor):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from fornecedor where id = '{idforncedor}'")
        forn = cursor.fetchone()
        return forn

    def fechar_conexao(self):
        self.connection.close()

