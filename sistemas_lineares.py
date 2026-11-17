# ==============================================================================
# 1ª PARTE: SISTEMAS LINEARES - QUESTÕES 01.3 E 02.3 (João Emanuel)
# ==============================================================================


def eliminacao_gauss(A: list, b: list) -> list:
    n = len(b)
    M = [linha[:] + [float(b[i])] for i, linha in enumerate(A)]

    for k in range(n):
        linha_pivo = max(range(k, n), key=lambda i: abs(M[i][k]))
        if abs(M[linha_pivo][k]) < 1e-12:
            raise ValueError("Sistema singular ou sem solucao unica.")

        if linha_pivo != k:
            M[k], M[linha_pivo] = M[linha_pivo], M[k]

        for i in range(k + 1, n):
            fator = M[i][k] / M[k][k]
            for j in range(k, n + 1):
                M[i][j] -= fator * M[k][j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - soma) / M[i][i]

    return x


def gauss_seidel(A: list, b: list, tol: float = 0.0001, max_iter: int = 1000) -> dict:
    n = len(b)
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError("Diagonal principal contem elemento nulo.")

    x = [float(b[i]) / float(A[i][i]) for i in range(n)]
    x_inicial = x[:]

    erro_rel = float("inf")
    for k in range(1, max_iter + 1):
        x_ant = x[:]

        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / A[i][i]

        erro_abs = max(abs(x[i] - x_ant[i]) for i in range(n))
        max_x = max(abs(v) for v in x)
        erro_rel = erro_abs / max_x if max_x > 1e-12 else erro_abs

        if erro_abs < tol and erro_rel < tol:
            return {
                "x_inicial": x_inicial,
                "solucao": x,
                "iteracoes": k,
                "erro_rel": erro_rel,
                "convergiu": True
            }

    return {
        "x_inicial": x_inicial,
        "solucao": x,
        "iteracoes": max_iter,
        "erro_rel": erro_rel,
        "convergiu": False
    }
