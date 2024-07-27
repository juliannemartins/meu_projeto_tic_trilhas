
def lista_de_compras():

    produtos = []
    id_counter = 1

    while True:
        print("Menu de compras: ")
        print()
        print("1 - Adionar produto")
        print("2 - Remover produto")
        print("3 - Pesquisar produtos")
        print("4 - Imprimir produtos")
        print("0 - Sair")
        operacao = input("Selecione uma opção ou 0 para sair: ")

        if operacao == "0":
            print("Saindo...")
            print("Obrigado por utilizar a Lista de Compras!")
            break

        if operacao not in ["1", "2", "3", "4"]:
            print("Opção inválida")
            continue

        if operacao == "1":
            nome = input("Nome do produto: ")
            unidade = input("Unidade do produto: ")
            quantidade = float(input("Quantidade do produto: "))
            descricao = input("Descrição do produto: ")

            produto = {
                "id": id_counter,
                "nome": nome,
                "unidade": unidade,
                "quantidade": quantidade,
                "descricao": descricao
            }
            produtos.append(produto)
            id_counter += 1

        elif operacao == "2":
            id_remover = input("Id do produto que deseja remover: ")

            if not id_remover.isdigit():
                print("ID inválido")
                print()
                continue

            id_remover = int(id_remover)
            produto_removido = False

            for produto in produtos:
                if produto["id"] == id_remover:
                    produtos.remove(produto)
                    produto_removido = True
                    print(f"Produto com id {id_remover} removido com sucesso!")
                    print()
                    break
            if not produto_removido:
                print(f"Nenhum produto encontrado com o ID {id_remover} na lista")
                print()
                continue

        elif operacao == "3":
            nome_pesquisa = input("Nome do produto: ").lower()
            produtos_encontrados = [produto for produto in produtos if produto['nome'].lower() == nome_pesquisa.lower()]
            print(f"Produtos encontrados: {len(produtos_encontrados)}")
            for produto in produtos_encontrados:
                print(f"ID: {produto['id']}, Nome: {produto['nome']}, Unidade: {produto['unidade']}, Quantidade: {produto['quantidade']}, Descrição: {produto['descricao']}")
                print()

        else:
            for produto in produtos:
                print("Id : ", produto['id'])
                print("Nome : ", produto['nome'])
                print("Unidade : ", produto['unidade'])
                print("Quantidade : ", produto['quantidade'])
                print("Descrição : ", produto['descricao'])
                print()

lista_de_compras()