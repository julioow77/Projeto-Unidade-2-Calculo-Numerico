from enunciados import MINAS, CIRCUITO, RESISTOR, RIO
from dados import (
    dados_questao_01_3,
    dados_questao_02_3,
    dados_questao_03_2,
    dados_questao_04_2,
)
from sistemas_lineares import eliminacao_gauss, gauss_seidel
from integracao import regra_trapezio_repetida, regra_simpson_repetida
from interpolacao import (
    selecionar_pontos_proximos,
    interpolacao_lagrange,
    interpolacao_newton,
)


def ler_linha(mensagem: str, quantidade: int) -> list:
    texto = input(mensagem)
    partes = texto.split()

    #Cada equação precisa de um coeficiente apra cada incognita
    if len(partes) != quantidade:
        raise ValueError(f"Digite exatamente {quantidade} números separados por espaços.")

    linha = []
    for parte in partes:
        numero = float(parte)
        linha.append(numero)

    return linha


def ler_sistema():
    texto = input("Quantas incógnitas tem o sistema? ")
    ordem = int(texto)

    if ordem < 1:
        raise ValueError("A ordem do sistema deve ser pelo menos 1.")

    # Cada linha da matriz A contém os coeficientes de uma equação.
    A = []
    for i in range(ordem):
        linha = ler_linha(f"Coeficientes da equação {i + 1}: ", ordem)
        A.append(linha)

    b = ler_linha("Termos independentes, na ordem das equações: ", ordem)
    return A, b


def menu_questao_01_3():
    print("\nEliminação de Gauss")
    print("1 - Usar os dados das minas (questão 01.3)")
    print("2 - Informar outro sistema linear")
    print("0 - Voltar ao menu principal")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == "0":
        return

    try:
        if opcao == "1":
            print("\n" + MINAS + "\n")
            A, b = dados_questao_01_3()
            print("Solução:")
        elif opcao == "2":
            A, b = ler_sistema()
        else:
            print("Opção inválida. Escolha 0, 1 ou 2.")
            return

        solucao = eliminacao_gauss(A, b)
    except ValueError as erro:
        print(erro)
        return

    for i in range(len(solucao)):
        if opcao == "1":
            print(f"Mina {i + 1}: {solucao[i]:.2f} m³")
        else:
            print(f"x{i + 1} = {solucao[i]}")


def menu_questao_02_3():
    print("\nMétodo de Gauss-Seidel")
    print("1 - Usar os dados do circuito (questão 02.3)")
    print("2 - Informar outro sistema linear")
    print("0 - Voltar ao menu principal")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        return

    try:
        if opcao == "1":
            print("\n" + CIRCUITO + "\n")
            A, b, tol = dados_questao_02_3()
            print("Solução:")
        elif opcao == "2":
            A, b = ler_sistema()
            tol = float(input("Digite a tolerância (por exemplo, 0.0001): "))
            if tol <= 0:
                raise ValueError("A tolerância deve ser positiva.")
        else:
            print("Opção inválida. Escolha 0, 1 ou 2.")
            return

        # Os dois caminhos usam o mesmo método de cálculo.
        resultado = gauss_seidel(A, b, tol)
    except ValueError as erro:
        print(erro)
        return
    if resultado["convergiu"]:
        solucao = resultado["solucao"]
        for i in range(len(solucao)):
            if opcao == "1":
                print(f"I{i + 1} = {solucao[i]:.4f} A")
            else:
                print(f"x{i + 1} = {solucao[i]:.4f}")
    else:
        print("O método atingiu o limite de iterações sem convergir.")


def menu_questao_04_2():
    print("\nIntegração Numérica")
    print("1 - Usar os dados do rio (questão 04.2)")
    print("2 - Informar outra tabela de pontos")
    print("0 - Voltar ao menu principal")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "0":
        return
    elif opcao == "1":
        print("\n" + RIO + "\n")
        x, m1, m2, y, h = dados_questao_04_2()
        print("Solução:")
    elif opcao == "2":
        # O passo h é a distância entre dois pontos consecutivos da tabela.
        try:
            texto_h = input("Digite o passo h (por exemplo, 0.5): ")
            h = float(texto_h)
            texto_y = input("Digite os valores de y separados: ")
            partes = texto_y.split()

            y = []
            for parte in partes:
                numero = float(parte)
                y.append(numero)
        
        except ValueError:
            print("Digite números válidos. Use ponto nos decimais e separe os valores de y")
            return
            
    else:
        print("Opção inválida. Escolha 0, 1 ou 2.")
        return

    try:
        area_trapezio = regra_trapezio_repetida(h, y)
        print("Integral pelo trapézio:", area_trapezio)

        area_simpson = regra_simpson_repetida(h, y)
        print("Integral por Simpson 1/3:", area_simpson)
    except ValueError as erro:
        print(erro)


def menu_questao_03_2():
    print("\nInterpolação Polinomial (Lagrange e Newton)")
    print("1 - Usar os dados do resistor (questão 03.2)")
    print("2 - Informar outra tabela de pontos manualmente")
    print("0 - Voltar ao menu principal")

    escolha_inicial = input("Escolha uma opção: ").strip()
    if escolha_inicial == "0":
        return

    try:
        if escolha_inicial == "1":
            print("\n" + RESISTOR + "\n")
            lista_x, lista_y, x_alvo = dados_questao_03_2()
            print("Solução:")
            for grau in [2, 3, 4]:
                x_base, y_base = selecionar_pontos_proximos(lista_x, lista_y, x_alvo, grau)
                res_lag = interpolacao_lagrange(x_base, y_base, x_alvo)
                res_new = interpolacao_newton(x_base, y_base, x_alvo)
                print(f"\n--- Grau {grau} (Pontos i usados: {x_base}) ---")
                print(f"Lagrange: V({x_alvo}) = {res_lag:.4f} V")
                print(f"Newton:   V({x_alvo}) = {res_new:.4f} V")

        elif escolha_inicial == "2":
            try:
                grau = int(input("Defina o Grau do Polinômio: "))
                total_pontos = int(input("Defina o total de pontos da tabela: "))
            except ValueError:
                print("Erro: Digite apenas números inteiros válidos para o grau e total de pontos.")
                return

            if grau < 0:
                print("Erro: O grau do polinômio não pode ser negativo.")
                return

            if total_pontos <= 0:
                print("Erro: A quantidade de pontos deve ser maior que zero.")
                return

            if total_pontos < grau + 1:
                print(f"Erro: São necessários pelo menos {grau + 1} pontos para um polinômio de grau {grau}.")
                return

            try:
                x_alvo = float(input("Defina o Ponto que vai ser Alvo dentro da Função: "))
                lista_x = []
                lista_y = []

                for i in range(total_pontos):
                    numero_x = float(input(f"Digite o {i + 1}º número para a coordenada 'x': "))
                    if any(abs(numero_x - x_existente) < 1e-12 for x_existente in lista_x):
                        print("Erro: Coordenada 'x' repetida! Todos os valores de 'x' devem ser distintos.")
                        return
                    lista_x.append(numero_x)
                
                for j in range(total_pontos):
                    numero_y = float(input(f"Digite o {j + 1}º número para a coordenada 'y': "))
                    lista_y.append(numero_y)
            except ValueError:
                print("Erro: Digite apenas números reais válidos (use ponto para decimais).")
                return

            x_base, y_base = selecionar_pontos_proximos(lista_x, lista_y, x_alvo, grau)

            print("\nMENU DO MÉTODO DE INTERPOLAÇÃO")
            print("1. INTERPOLAÇÃO POLINOMIAL - MÉTODO DE LAGRANGE")
            print("2. INTERPOLAÇÃO POLINOMIAL - MÉTODO DE NEWTON")
            
            opcao = input("ESCOLHA: ").strip()

            if opcao == "1":
                res = interpolacao_lagrange(x_base, y_base, x_alvo)
                print(f"Resultado por Lagrange: {res:.4f}")
            elif opcao == "2":
                res = interpolacao_newton(x_base, y_base, x_alvo)
                print(f"Resultado por Newton: {res:.4f}")
            else:
                print("Opção inválida! Escolha 1 ou 2.")
        else:
            print("Opção inválida. Escolha 0, 1 ou 2.")

    except ValueError as erro:
        print(f"Erro de validação: {erro}")


def exibir_menu():
    print("\n" + "=" * 60)
    print("   PROJETO FINAL UNIDADE 2 - CÁLCULO NUMÉRICO (EQUIPE 14)")
    print("=" * 60)
    print("1 - Questão 01.3: Sistemas Lineares - Eliminação de Gauss (3 Minas)")
    print("2 - Questão 02.3: Sistemas Lineares - Gauss-Seidel (Circuito)")
    print("3 - Questão 03.2: Interpolação de Lagrange e Newton (Resistor)")
    print("4 - Questão 04.2: Integração - Trapézio e Simpson (Área do Rio)")
    print("0 - Sair")
