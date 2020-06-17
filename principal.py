from pessoa import Pessoa
from fornecedor import Fornecedor
import os

logado = False

def cadastrar_fornecedor():

    os.system('cls')
    #willian gay

    nome = input('Digite o nome do fornecedor: ')

    fornecedor = Fornecedor()
    fornecedor.cadastrar_fornecedor(nome)
    fornecedor.fechar_conexao()

def editar_fornecedor():

    os.system('cls')

    fornecedor = Fornecedor()

    lista_fornecedores = fornecedor.buscar_fornecedores()

    print('Lista de fornecedores: \n')

    cont = 1
    for forn in lista_fornecedores:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15}')
        cont += 1

    numero_forn = int(input('\nEscolha um fornecedor: '))
    nome = input('\nDigite o novo nome do fornecedor: ')

    fornecedor.editar_fornecedor(lista_fornecedores[numero_forn - 1][0], nome)


while(not logado):
    usuario = input('Usuário: ')
    senha = input('Senha: ')

    pessoa = Pessoa()
    usuario_logado = pessoa.buscar_pessoa_usuario_senha(usuario, senha)

    if(usuario_logado != None):
        logado = True
    else:
        os.system('cls')
        print('Usuário ou senha incorretos, tente novamente')

while(logado):

    os.system('cls')

    menu = """
    Menu do sistema: 

    [ 1 ] - Cadastrar produto
    [ 2 ] - Editar produto
    [ 3 ] - Excluir produto
    [ 4 ] - Listar produtos 
    [ 5 ] - Cadastrar Fornecedor
    [ 6 ] - Editar fornecedor
    [ 7 ] - Excluir fornecedor
    [ 8 ] - Listar forncedores
    [ 9 ] - Sobre a empresa
    [ 0 ] - Sair do sistema
    """

    print(menu)

    opcao = int(input('Selecione uma opção: '))

    if(opcao == 5):
        cadastrar_fornecedor()
        input()
    if(opcao == 6):
        editar_fornecedor()
    



