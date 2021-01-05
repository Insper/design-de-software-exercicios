'''
Faça uma função que recebe uma string contendo um texto e retorna uma nova string
mantendo apenas a primeira ocorrência de cada caractere inalterada e substituindo
as próximas ocorrências pelo caractere `'*'`. Exemplo:

- **Entrada:** `'banana'`
- **Saída:** `'ban***'`

- **Entrada:** `'abacaxi'`
- **Saída:** `'ab*c*xi'`

- **Entrada:** `'Um mago nunca se atrasa, nem se adianta, ele chega exatamente quando pretende chegar'`
- **Saída:** `'Um *ago*nu*c**se**tr***,*********di*******l***h*****x*********q******p**************'`

Note no último exemplo que os caracteres `'U'` e `'u'` são considerados distintos
(maiúsculo e minúsculo). Além disso, as vírgulas e espaços também são caracteres.

**Desafio:** faça sua função considerar letras maiúsculas e minúsculas como iguais.

Sua função deve se chamar `apaga_repetidos`.
'''

def apaga_repetidos(texto):
    ja_ocorreram = []
    novo_texto = ''
    for c in texto:
        if c in ja_ocorreram:
            novo_texto += '*'
        else:
            novo_texto += c
            ja_ocorreram.append(c)
    return novo_texto


def apaga_repetidos_desafio(texto):
    ja_ocorreram = []
    novo_texto = ''
    for c in texto:
        if c.lower() in ja_ocorreram:
            novo_texto += '*'
        else:
            novo_texto += c
            ja_ocorreram.append(c.lower())
    return novo_texto
