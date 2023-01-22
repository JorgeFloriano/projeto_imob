from imobiliaria.def_imob import *


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def cadastroLista(arq, lista):
    try:
        a = open(arq, 'wt')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{lista}')
        except:
            print('houve um erro na hora de escrever os dados!')
        else:
            a.close()


def txtInt(arquivo, lista):
    lista.clear()
    dado = []
    cl = 0
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        for i in a:
            dado = i.split(',')
            dado[0] = dado[0].replace('[', '')
            dado[-1] = dado[-1].replace(']', '')
        for i in dado:
            dado[cl] = dado[cl].replace(' ', '')
            cl += 1
        for i in dado:
            inteiro = int(i)
            lista.append(inteiro)
        a.close()
    return lista
