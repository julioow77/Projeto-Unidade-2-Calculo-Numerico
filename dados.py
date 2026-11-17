# ==============================================================================
# DADOS OFICIAIS DAS QUESTÕES SORTEADAS DA EQUIPE 14
# ==============================================================================


def dados_questao_01_3():
    """Questão 01.3: Matriz de composição das 3 minas e demandas."""
    A = [
        [0.55, 0.25, 0.25],
        [0.30, 0.45, 0.20],
        [0.15, 0.30, 0.55]
    ]
    b = [4800.0, 5800.0, 5700.0]
    return A, b


def dados_questao_02_3():
    """Questão 02.3: Circuito de 5 malhas e precisão de 0.0001."""
    A = [
        [ 9.5, -2.5,  0.0, -2.0,  0.0],
        [-2.5, 11.0, -3.5,  0.0, -5.0],
        [ 0.0, -3.5, 15.5,  0.0, -4.0],
        [-2.0,  0.0,  0.0,  7.0, -3.0],
        [ 0.0, -5.0, -4.0, -3.0, 12.0]
    ]
    b = [12.0, -16.0, 14.0, 10.0, -30.0]
    tol = 0.0001
    return A, b, tol


def dados_questao_03_2():
    """Questão 03.2: Tabela de corrente vs tensão para estimar i = 1.15 A."""
    i_pontos = [0.25, 0.75, 1.25, 1.50, 2.00]
    v_pontos = [-0.45, -0.60, 0.70, 1.88, 6.00]
    i_alvo = 1.15
    return i_pontos, v_pontos, i_alvo


def dados_questao_04_2():
    """Questão 04.2: Margens M1 e M2 do rio no intervalo [0, 40] e passo h = 10."""
    x = [0.0, 10.0, 20.0, 30.0, 40.0]
    m1 = [50.8, 86.2, 136.0, 72.8, 51.0]
    m2 = [113.6, 144.5, 185.0, 171.2, 95.3]
    larguras = [m2[k] - m1[k] for k in range(len(x))]
    h = 10.0
    return x, m1, m2, larguras, h
