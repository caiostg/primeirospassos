#conding: utf-8
list=[]
while True:
    print('Lista telefonica  ')
    print('1)Adicionar')
    print('2)Consultar')
    print('3)Remover')
    print('0)Sair ')
    op=int(input('Escolha uma das opções acima:\n'))
    if op == 0:
        break
    elif op == 1:
        nome=input('Digite o nome e Sobrenome do Contato:\n')
        tel = int(input('Digite o número do Telefone:\n'))
        contato= {'nome':nome,'telefone':tel}
        list.append(contato)
        print(f'{nome} foi adicionado com sucesso')
    elif op == 3:
        nome = input('Digite o nome do contato:\n ')
        contato_encontrado = False
        for contato in list:
            if contato['nome'] == nome:
                list.remove(contato)
                print(f'{nome} foi removido.')
                contato_encontrado = True
                break
        if contato_encontrado == False:
            print(f'{nome} não foi encontrado na lista.')
    elif op == 2:
        print('\nLista de contatos :')
        for contato in list:
            print(f"Nome: {contato['nome']}")
            print(f'Telefone: {contato["telefone"]}')
    else:
        print('Opção invalida')

        



