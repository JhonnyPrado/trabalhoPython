import psycopg2


class Produto:

    def __init__(self):
        self.connection = psycopg2.connect(
            host='localhost', database='banco_python', user='postgres', password='admin')

    def cadastrar_produto(self, nome, quantidade, idFornecedor):
        cursor = self.connection.cursor()
        cursor.execute('insert into produto (nome, quantidade, idFornecedor, status) values (%s, %s, %s, %s)',
                       (nome, quantidade, idFornecedor, True))
        self.connection.commit()
        self.connection.close()

    def editar_produto(self, id, nome, quantidade, idFornecedor):
        cursor = self.connection.cursor()
        cursor.execute('update produto set nome = %s, quantidade = %s, idFornecedor = %s where id = %s',
                       (nome, quantidade, idFornecedor, id))
        self.connection.commit()
        self.connection.close()

    def excluir_produto(self, id):
        #print(id)
        cursor = self.connection.cursor()        
        cursor.execute(
            f"delete from produto where id = '{id}'")
        self.connection.commit()         

    def buscar_produtos(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from produto')
        recset = cursor.fetchall()
        #self.connection.close()
        return recset

    def buscar_produto_id(self, idproduto):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from produto where id = '{idproduto}'")
        recset = cursor.fetchone()
        self.connection.close()
        return recset

    def fechar_conexao(self):
        self.connection.close()    
