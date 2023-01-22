def val(msg, numopc=1, zero=True, conflito=0.8):  # Válidação de entrada de dados dos menus
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        # except KeyboardInterrupt:
        #    print('\033[31mUsuário preferiu não digitar esse número.\033[m')
        #    return 'Erro !!'
        else:
             if n > numopc or n < 0 or (zero == False and n == 0):
                print('Opção inválida, tente novamente')
                continue
             if n == conflito:
                print('Vendedor já escalado nesse período, tente outa opção')
                #continue
             return n


def men(lista, txt, c=1):  # exibição de menu
    cabeçalho(txt)
    for item in lista:
        print(f'{c} - {item}')
        c += 1


def linha(tam=74):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(75))
    print(linha())


def cor(cod, msg):  # colorir nome do vendedor já formatado para a tabela
    c = f'\033[{cod}m{msg:<13}\033[m'
    return c


def am(msg):  # amarelo
    amarelo = f'\033[33m{msg}\033[m'
    return amarelo


def cya(msg):  # cyan
    c = f'\033[36m{msg}\033[m'
    return c


def cabPlanilhaR1():
    print('\033[7m          |          Superquadra          |           Paulistano          \033[m|')
    print('Data |Dia |09:00 às 15:00 |15:00 às 20:00 |09:00 às 14:00 |14:00 às 18:00 |')
    print('\033[7m     |    |     Manhã     |     Tarde     |     Manhã     |     Tarde     \033[m|')


def listaIni(listap, vend):  # lista inicial para alimentação da tabela
    listap.clear()
    cv = 0
    for c in range(0, 124, ):
        listap.append(cv)
        cv += 1
        if cv == len(vend):
            cv = 0
    return listap


def aprPlanilha(listsemana, listvendedores, listaplan):  # apresentação da planilha
    dia = z = c = cd = 0  # dia - dias da semana, z = zero à esquerda, c = datas
    cabeçalho('IMOBILIÁRIA X5 - PLANILHA DE OUTUBRO - PLANTÕES: SUPERQUADRA E PAULISTANO ')
    cabPlanilhaR1()
    while True:
        if c >= 31:
            break
        if c > 8:
            z = ''
        if c % 2 == 0:
            print(f'\033[40m{z}{c + 1}   |{listsemana[dia]}\033[40m |\033[m', end='')
            c += 1
            for c2 in range(1, 5):
                print(f'\033[40m  {listvendedores[listaplan[cd]]:<13}\033[40m|', end='')
                cd += 1
            print('\033[m')
        else:
            print(f'{z}{c + 1}   |{listsemana[dia]} |', end='')
            for c2 in range(1, 5):
                print(f'  {listvendedores[listaplan[cd]]:<14}|', end='')
                cd += 1
            print('')
            c += 1
        dia += 1
        if dia == 7:
            dia = 0
    print('Número de escalas por vendedor durante este mês:')
    print(f' Roberto ({listaplan.count(0)}), João ({listaplan.count(1)}), Jorge ({listaplan.count(2)}),'
          f' Bertim ({listaplan.count(3)}), Marta({listaplan.count(4)}), Yanca ({listaplan.count(5)})')


def menuAlterac(dia, periodos, vendedoresf, vendedores, listaplan):  # menu de alteração da escala
    men(periodos, f'OPÇÕES PARA ALTERAÇÃO DA ESCALA, DIA {dia} ', 1)
    y = val('Digite o número da sua opção: ', 4, False)
    men(vendedoresf, 'LISTA DE VENDEDORES CADASTRADOS')
    posicao = ((dia - 1) * 4) + (y - 1)
    vend = val('Digite o número do vendedor para concluir: ', 6, False)
    if y == 1 and listaplan[posicao + 2] == vend - 1 or y == 2 and listaplan[posicao + 2] == vend - 1 \
            or y == 3 and listaplan[posicao - 2] == vend - 1 or y == 4 and listaplan[posicao - 2] == vend - 1:
        print(f'Erro, vendedor(a) {vendedores[vend - 1]}, já está escalado em outro plantão nesse período !')
    else:
        listaplan[posicao] = vend - 1
        print(f'Vendedor(a) {vendedores[vend - 1]} escalado no dia {dia}, plantão {periodos[y - 1]} com sucesso !')
