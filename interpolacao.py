# ==============================================================================
# 3ª PARTE: INTERPOLAÇÃO POLINOMIAL - QUESTÃO 03.2 COMPLETA (Eduardo dos Santos)
# ==============================================================================


def selecionar_pontos_proximos(x_todos: list, y_todos: list, x_alvo: float, grau: int):
    if grau < 0:
        raise ValueError("O grau do polinômio deve ser maior ou igual a zero.")
    
    n = len(x_todos)

    if n <= 0 or n != len(y_todos):
        raise ValueError("As listas x e y devem ter a mesma quantidade positiva de pontos.")

    if n < grau + 1:
        raise ValueError(f"São necessários pelo menos {grau + 1} pontos para o grau {grau}.")

    # Verifica se há valores de x repetidos na tabela informada
    for i in range(n):
        for j in range(i + 1, n):
            if abs(x_todos[i] - x_todos[j]) < 1e-12:
                raise ValueError("Não são permitidas coordenadas 'x' repetidas.")

    x = x_todos[:]
    y = y_todos[:]

    for i in range(n - 1):  
        for j in range(n - i - 1):
            if abs(x[j] - x_alvo) > abs(x[j + 1] - x_alvo):
                aux = x[j]
                x[j] = x[j + 1]
                x[j + 1] = aux 

                aux_y = y[j]
                y[j] = y[j + 1]
                y[j + 1] = aux_y


    x_base = x[:grau + 1]
    y_base = y[:grau + 1]

    return x_base, y_base


def interpolacao_lagrange(x_base: list, y_base: list, x_alvo: float) -> float:
    n = len(x_base)

    if n < 1 or n != len(y_base):
            raise ValueError("Quantidade inválida de pontos base.")


    y_resultado = 0.0

    for i in range(n):
        L = 1.0    
        for j in range(n):
            if i != j:
                numerador = x_alvo - x_base[j]
                denominador = x_base[i] - x_base[j]

                if abs(denominador) < 1e-12:
                    raise ValueError("Divisão por zero: existem coordenadas 'x' repetidas.")
                
                L = L * (numerador/denominador)

        y_resultado = y_resultado + (y_base[i] * L)    
        
    return y_resultado


def interpolacao_newton(x_base: list, y_base: list, x_alvo: float) -> float:
    n = len(x_base)

    if n < 1 or n != len(y_base):
            raise ValueError("Quantidade inválida de pontos base.")

    if n == 1:
        return y_base[0]
    
    elif n > 1:
        b = y_base[:]
        resultado = y_base[0]
        produtorio_x = 1.0

        for j in range(1 , n):
            for i in range(n - 1, j - 1, -1):
                numerador = b[i] - b[i - 1]
                denominador = x_base[i] - x_base[i - j]

                if abs(denominador) < 1e-12:
                    raise ValueError("Divisão por zero: existem coordenadas 'x' repetidas.")
            
                b[i] = numerador/denominador
            
            produtorio_x = produtorio_x * (x_alvo - x_base[j - 1])
            resultado = resultado + (produtorio_x * b[j])

        return resultado
