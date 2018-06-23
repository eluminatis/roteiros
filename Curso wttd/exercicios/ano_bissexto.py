"""

A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas (mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as festas religiosas.

Um determinado ano é bissexto se:

O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.

"""


def bissexto(ano):
    if ano % 4 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    assert bissexto(1600) == True
    assert bissexto(1732) == True
    assert bissexto(1888) == True
    assert bissexto(1944) == True
    assert bissexto(2008) == True

    assert bissexto(1742) == False
    assert bissexto(1889) == False
    assert bissexto(1951) == False
    assert bissexto(2011) == False