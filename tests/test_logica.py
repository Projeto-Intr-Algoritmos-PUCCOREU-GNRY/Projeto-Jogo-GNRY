from src.funcoes import atualizar_recorde


def test_recorde_maior():

    recorde = 10
    pontos = 20

    assert atualizar_recorde(recorde, pontos) == 20


def test_recorde_menor():

    recorde = 20
    pontos = 10

    assert atualizar_recorde(recorde, pontos) == 20


def test_recorde_igual():

    recorde = 15
    pontos = 15

    assert atualizar_recorde(recorde, pontos) == 15