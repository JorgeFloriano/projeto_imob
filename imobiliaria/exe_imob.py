from imobiliaria import *

import os

x = 0
arq = 'escala.txt'
periodos = ['Superquadra / Manhã', 'Superquadra / Tarde', 'Paulistano / Manhã', 'Paulistano / Tarde']
semana = [am('sáb'), am('dom'), 'seg', 'ter', 'qua', 'qui', 'sex']
listaplan = []  # lista de dados para salvar planilha
vendedores = ['Roberto', 'João', 'Jorge', 'Bertim', 'Marta', 'Yanca']
vendedoresf = [cor(33, 'Roberto'), cor(97, 'João'), cor(34, 'Jorge'),
               cor(32, 'Bertim'), cor(35, 'Marta'), cor(31, 'Yanca')]
opc = 1
while True:
    if opc == 0:
        break
    elif opc == 2:
        if arquivoExiste(arq):
            os.remove('escala.txt')
        criarArquivo(arq)
        listaIni(listaplan, vendedoresf)  # cria lista inicial
        cadastroLista(arq, listaplan)  # salva lista inicial em arq
        aprPlanilha(semana, vendedoresf, listaplan)  # apresenta planilha a partir da lista inicial
    else:
        while True:
            txtInt(arq, listaplan)  # converte o conteudo de arq para uma lista de inteiros
            aprPlanilha(semana, vendedoresf, listaplan)  # apresenta planilha a partir da lista
            cabeçalho('Menu de alteração de escala.')
            x = val('Digite o dia que deseja alterar ou 0 para voltar: ', 31)
            if x == 0 or x > 31:
                break
            menuAlterac(x, periodos, vendedoresf, vendedores, listaplan)  # menu de alteração da lista
            cadastroLista(arq, listaplan)  # salva lista em arq apos alterações
            s = input(f'Pressione enter para voltar para o menu inicial.')
    opc = val('Editar lista - 1 / Reiniciar lista - 2 / Sair - 0: ', 3)


