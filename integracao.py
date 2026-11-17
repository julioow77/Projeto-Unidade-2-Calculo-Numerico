# ==============================================================================
# 2ª PARTE: INTEGRAÇÃO (04.2) E MENUS DAS OPÇÕES 1, 2 E 4 (Júlio César)
# ==============================================================================


def regra_trapezio_repetida(h: float, y: list) -> float:
    if(h <= 0 or len(y) < 2):
        raise ValueError("Informe uma passo positivo e pelo menos dois valores de y.")

    area_total = 0.0

    # Cada par de pontos consecutivos define um intervalo de integração 
    for i in range(len(y) - 1):
        area_trecho = (y[i] + y[i + 1]) * h / 2
        area_total = area_total + area_trecho

    return area_total


def regra_simpson_repetida(h: float, y: list) -> float:
    intervalos = len(y) - 1

    if (h <= 0 or intervalos < 2 or intervalos % 2 != 0):
        raise ValueError("Informe um passo positivo e um número par de intervalos (mínimo de 2).")

    area_total = 0.0

    # Cada grupo de três pontos corresponde a dois intervalos
    for i in range(0, intervalos, 2):
        area_trecho = (y[i] + 4 * y[i + 1] + y[i + 2]) * h / 3
        area_total = area_total + area_trecho

    return area_total
