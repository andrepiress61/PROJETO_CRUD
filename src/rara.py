# pega a função "get_connet"
import random
from connection import get_connet

# biblioteca
from passlib.hash import pbkdf2_sha256 as sha256
desc = input("Digite um numero")
preco = input("Digite o preço")
quant = input("Digite a quantidade")
id = random.randint(1, 1000)
print (id) 
# função para criar usuario
'''def criar_produto( desc, preco, quant):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa codigos na sql
        cursor.execute('INSERT INTO TB_PRODUTO(desc, preco, quant) VALUES (?, ?, ?)',
                       (desc, preco, quant)
        )

        # commita no banco
        conn.commit()
        print('Produto cadastrado com sucesso!')

    # trata erros
    except Exception as e:
        print(f'Falha ao criar produto: {e}')

# função para listar usuarios
def listar_produto():
    # trata erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, DESC, PRECO, QUANT FROM TB_PRODUTO')

        #
        produtos = cursor.fetchall()

        # se tiver usuarios
        if produtos:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')

            # mostrar os usuarios
            for u in produtos:
                print(f'| {u}')

        # se nao tiver usuarios
        else:
            print('Nenhum usuário encontrado!')

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

def editar_produto(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet(id)

        # comanda o banco
        cursor = conn.cursor()

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

def vender():
    try:
        conn = get_connet()

        cursor = conn.cursor()

        cursor.execute('SELECT ID, DESC, PRECO, QUANT FROM TB_PRODUTO')

        produtos = cursor.fetchall()

        escolha = input("Digite a sua escolha")

        if produtos:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')

            for u in produtos:
                print(f'| {u}')
            escolha
            if escolha == produtos:
                print("Produto vendido com sucesso")

            elif escolha != produtos:
                print('Escolha uma opção valida')
            else:
                ("Produto não encontrado")
    except:
        ...
criar_produto()
listar_produto()
vender()

'''
