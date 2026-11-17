"""
PROJETO FINAL - UNIDADE 2 - CÁLCULO NUMÉRICO (UNIVASF 2026.2)
EQUIPE 14 - QUESTÕES: 01.3, 02.3, 03.2 e 04.2

Divisão de Tarefas:
- 1ª PARTE (João Emanuel): Sistemas Lineares (01.3 e 02.3)
- 2ª PARTE (Júlio César): Integração Numérica (04.2) e Menus das Opções 1, 2 e 4
- 3ª PARTE (Eduardo dos Santos): Interpolação Polinomial Completa (03.2)
"""


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
from menus import (
    ler_linha,
    ler_sistema,
    menu_questao_01_3,
    menu_questao_02_3,
    menu_questao_03_2,
    menu_questao_04_2,
    exibir_menu,
)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_questao_01_3()
        elif opcao == "2":
            menu_questao_02_3()
        elif opcao == "3":
            menu_questao_03_2()
        elif opcao == "4":
            menu_questao_04_2()
        elif opcao == "0":
            print("\nEncerrando o programa.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
