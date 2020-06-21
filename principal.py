from pessoa import Pessoa
from fornecedor import Fornecedor
from produto import Produto
import os, sys
import time

logado = False

os.system('cls')

def sobre_a_empresa():
    os.system('cls')

    print('\n\n\t SoftRARE \n')
    print('Somos uma empresa que desenvolve aplicativos e softwares para os diversos tipos de necessidades.\n')
    print('Sabia que os programadores só podem ser encontrados em dois lugares no mundo?')
    print('Onde? No hemisfério Norte e no hemisferio Sul.\n')

    time.sleep(3)
    continuar = input("\n\nTecle Enter para continuar")


def listar_fornecedor():
    os.system('cls')

    fornecedor = Fornecedor()

    lista_fornecedores = fornecedor.buscar_fornecedores()

    print('Lista de fornecedores: \n')

    cont = 1
    for forn in lista_fornecedores:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15}')
        cont += 1
    
    time.sleep(3)
    continuar = input("\n\nTecle Enter para continuar")
            



def cadastrar_fornecedor():

    os.system('cls')
    

    nome = input('Digite o nome do fornecedor: ')

    fornecedor = Fornecedor()
    fornecedor.cadastrar_fornecedor(nome)
    fornecedor.fechar_conexao()

def cadastrar_produto():
    
    os.system('cls')    

    nome = input('Digite o nome do produto: ')
    quantidade = int(input('\nDigite a quantidade desse produto: '))

    fornecedor = Fornecedor()

    lista_fornecedores = fornecedor.buscar_fornecedores()

    print('Lista de fornecedores: \n')

    cont = 1
    for forn in lista_fornecedores:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15}')
        cont += 1

    numero_forn = int(input('\nEscolha um fornecedor para atribuir o produto: '))

    produto = Produto()
    produto.cadastrar_produto(nome, quantidade, lista_fornecedores[numero_forn - 1][0])
    produto.fechar_conexao()

def editar_produto():
    
    os.system('cls')

    produto = Produto()

    lista_produto = produto.buscar_produtos()

    print('Lista de produtos: \n')

    cont = 1
    for forn in lista_produto:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15} - Quantidade:  {forn[2]:^15} - ID Fornecedor: {forn[3]:^15} ')
        cont += 1

    numero_forn = int(input('\nEscolha um produto para editar: '))
    nome = input('\nDigite o novo nome do produto: ')
    quantidade = int(input('\nEscolha a quantidade do produto: \n'))

    fornecedor = Fornecedor()

    lista_fornecedores = fornecedor.buscar_fornecedores()

    print('Lista de fornecedores: \n')

    cont = 1
    for forn in lista_fornecedores:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15}')
        cont += 1

    idForn = int(input('\nEscolha um fornecedor para atribuir o produto: '))

    produto.editar_produto(lista_produto[numero_forn - 1][0], nome, quantidade, lista_fornecedores[idForn - 1][0])        

def listar_produto() :  #falta puxar nome do fornecedor aqui!
    os.system('cls')

    produto = Produto()

    lista_produto = produto.buscar_produtos()

    print('Lista de produtos: \n')

    cont = 1
    for forn in lista_produto:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15} - Quantidade:  {forn[2]:^15} - ID Fornecedor: {forn[3]:^15}' )
        cont += 1
    
    time.sleep(3)
    continuar = input("\n\nTecle Enter para continuar") 

def excluir_produto():
    os.system('cls')

    produto = Produto()

    lista_produto = produto.buscar_produtos()

    print('Lista de produtos: \n')

    cont = 1
    for forn in lista_produto:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15} - Quantidade:  {forn[2]:^15} - ID Fornecedor: {forn[3]:^15}')
        cont += 1

    
    numero_forn = int(input('\nEscolha um fornecedor para excluir: '))
    produto.excluir_produto(lista_produto[numero_forn - 1][0])               

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

def excluir_fornecedor():
    os.system('cls')

    fornecedor = Fornecedor()

    lista_fornecedores = fornecedor.buscar_fornecedores()

    print('Lista de fornecedores: \n')

    cont = 1
    for forn in lista_fornecedores:
        print(f'[ {cont:^3} ] - Nome: {forn[1]:^15}')
        cont += 1

    
    numero_forn = int(input('\nEscolha um fornecedor para excluir: '))
    fornecedor.excluir_fornecedor(lista_fornecedores[numero_forn - 1][0])


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
    [ 8 ] - Listar fornecedores
    [ 9 ] - Sobre a empresa
    [ 0 ] - Sair do sistema
    """
    #fazer todos

    print(menu)

    opcao = int(input('Selecione uma opção: '))

    if(opcao == 1):
        cadastrar_produto()
    if(opcao == 2):
        editar_produto()
    if(opcao == 3):
        excluir_produto()
    if(opcao == 4):
        listar_produto()            
    if(opcao == 5):
        cadastrar_fornecedor()
        input()
    if(opcao == 6):
        editar_fornecedor()
    if(opcao == 7):
        excluir_fornecedor()        
    if(opcao == 8):
        listar_fornecedor()        
    if(opcao == 9):
        sobre_a_empresa()  
    if(opcao == 0):
        print('\n\nEncerrando o sistema....\n')
        print('Falou!')
        sys.exit(0)                        
    