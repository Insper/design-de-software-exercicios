#!/usr/bin/env python
from pathlib import Path
import sys
import os
import json
import click
from strtest import str_test

from cmd_utils import success, danger, info


CUR_DIR = Path(__file__).parent
EXERCICIOS = CUR_DIR / 'exercicios'
DETALHES = 'detalhes.json'
ENUNCIADO = 'enunciado.md'
TESTES = 'testes.py'
with open(CUR_DIR / 'tags.txt') as f:
    TAGS = [t for t in f.read().split() if t]


TEMPLATE_DETALHES = '''{
    "titulo": "",
    "publicado": true,
    "terminal": true,
    "nome_funcao": null,
    "tags": ""
}
'''

TEMPLATE_TESTES = '''"""
Consulte a documentação do strtest para mais detalhes: https://github.com/Insper/python-string-test-runner

Guia rápido:
===========
O TestCaseWrapper possui os seguintes atributos:
    - function: função fornecida pelo usuário
    - program: função que executa o programa fornecido pelo usuário
    - module: arquivo fornecido pelo usuário carregado como um módulo Python
Asserts úteis:
    - assert_similar(self, string1, string2, dist_max=1, case_sensitive=False, msg=None)
    - assert_printed(self, value, index=None, msg=None)
    - assert_printed_all(self, values, msg=None, **kwargs)
Mocks (todas as funções tem os atributos calls, args e kwargs, que guardam a quantidade de chamadas realizadas e os argumentos):
    - mock_print: atributo printed guarda a lista de strings impressas
    - mock_input: atributo input_list recebe uma sequência de entradas a serem utilizadas
    - mock_open: atributo opened é uma lista de arquivos que não foram fechados e é possível adicionar arquivos falsos no dicionário files (chave é o nome do arquivo e o valor é o seu conteúdo)
    - mock_random: chaves são tuplas com os argumentos esperados e valores são sequências de números

Se for implementar os métodos setUpClass, setUp e tearDown lembre-se de chamar a função da classe mãe.
"""
from strtest import str_test


class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 3  # Segundos

    def test_1(self):
        # Implemente quantas funções de teste forem necessárias. Basta que o nome do método comece com test_
        pass
'''


@click.group(help='Administração dos exercícios de Design de Software.')
def cli():
    pass


@cli.command(help='Criar novo exercício.')
@click.argument('slug')
def novo(slug):
    info('Criando exercício', slug)
    ex_dir = EXERCICIOS / slug
    if ex_dir.is_dir():
        danger(f'Já existe um exercício chamado {slug}')
        sys.exit()

    os.mkdir(ex_dir)
    cria_arquivo(ex_dir / DETALHES, TEMPLATE_DETALHES)
    cria_arquivo(ex_dir / ENUNCIADO)
    cria_arquivo(ex_dir / TESTES, TEMPLATE_TESTES)
    cria_arquivo(ex_dir / 'solucao.py')
    cria_arquivo(ex_dir / 'errado.py')


@cli.command(help='Executar testes. Nome do teste a ser executado é opcional.')
@click.argument('nome_teste', default=None, required=False)
def teste(nome_teste):
    if nome_teste:
        if not (EXERCICIOS / nome_teste).is_dir():
            danger(f'O exercício {nome_teste} não existe.')
            sys.exit()
        valida_exercicio(EXERCICIOS / nome_teste)
    else:
        info('Testando todos os exercícios')
        ok = True
        for ex_dir in EXERCICIOS.iterdir():
            if not ex_dir.is_dir(): continue
            if not valida_exercicio(ex_dir):
                ok = False
        if ok:
            success('Tudo ok!')
        else:
            danger('Falhou em alguma validação')


def valida_exercicio(ex_dir):
    info('Testando exercício', ex_dir)
    ok = True
    try:
        detalhes = valida_detalhes(ex_dir)
        valida_enunciado(ex_dir)
        aplica_testes(ex_dir, detalhes.get('nome_funcao'))
    except AssertionError as e:
        danger('Erro de validação:', e)
        ok = False
    if ok:
        success("OK")
    else:
        danger('FALHA')
    return ok


def valida_detalhes(ex_dir):
    arq_detalhes = ex_dir / DETALHES
    detalhes_str = carrega_arquivo(arq_detalhes)
    try:
        detalhes = json.loads(detalhes_str)
    except json.decoder.JSONDecodeError:
        raise AssertionError(f'Arquivo {arq_detalhes} não é um JSON válido.')
    assert isinstance(detalhes, dict), f'Arquivo {arq_detalhes} deveria ser um dicionário em formato JSON.'
    assert detalhes.get('titulo'), f'Arquivo {arq_detalhes} deveria conter a chave "titulo".'
    assert detalhes.get('publicado'), f'Arquivo {arq_detalhes} deveria conter a chave "publicado".'
    assert detalhes.get('terminal'), f'Arquivo {arq_detalhes} deveria conter a chave "terminal".'
    assert detalhes.get('tags'), f'Arquivo {arq_detalhes} deveria conter a chave "tags".'
    tags = detalhes['tags'].split(',')
    for tag in tags:
        if tag:
            assert tag in TAGS, f'A tag {tag} não existe'
    return detalhes


def valida_enunciado(ex_dir):
    arq_enunciado = ex_dir / ENUNCIADO
    enunciado = carrega_arquivo(arq_enunciado)
    assert enunciado.strip(), f'Arquivo {arq_enunciado} não deveria estar vazio.'


def aplica_testes(ex_dir, nome_funcao):
    corretos = list(ex_dir.glob('solucao*.py'))
    errados = list(ex_dir.glob('errado*.py'))
    arq_testes = ex_dir / TESTES
    assert corretos, 'Deveria ter pelo menos uma solução correta.'
    assert errados, 'Deveria ter pelo menos uma solução incorreta.'
    for arq_codigo in corretos + errados:
        aplica_teste(arq_codigo, arq_testes, nome_funcao)


def aplica_teste(arq_codigo, arq_testes, nome_funcao):
    codigo = carrega_arquivo(arq_codigo)
    testes = carrega_arquivo(arq_testes)
    resultado = str_test.run_tests(codigo, testes, nome_funcao)
    esperado = 'solucao' in str(arq_codigo)
    assert esperado == resultado.success, f'Resultado diferente do esperado para o arquivo {arq_codigo}'


def carrega_arquivo(arquivo):
    if not arquivo.is_file():
        raise AssertionError(f'Arquivo {arquivo} não existe.')
    with open(arquivo) as f:
        return f.read()


def cria_arquivo(arquivo, conteudo=None):
    if not conteudo:
        conteudo = ''
    with open(arquivo, 'w') as f:
        f.write(conteudo)


if __name__ == "__main__":
    cli()
