import os

fluxo_caixa = []
total_receita = 0
total_despesa = 0

while True:
    # Limpar tela
    os.system("clear" if os.name == "posix" else "cls")
    # Imprimir Menu
    print("-" * 50)
    print("@ Fluxo de Caixa @")
    print("-" * 50)
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Verificar Fluxo")
    print("4 - Sair")
    print("-" * 50)
    # Requisitar opção
    while True:
        try:
            opcao = int(input("Digite a opção: "))
            break
        # Tratamento de erro
        except ValueError:
            print("Por favor, insira um número válido.")

    # Adicionar Receita
    if opcao == 1:
        nome = input("Nome: ")
        # Tratamento de erro
        try:
            valor = float(input("Valor: "))
            total_receita += valor  # Atualizar o total de receitas
        except ValueError:
            print("Por favor, insira um número válido.")
        fluxo_caixa.append({"nome": nome, "valor": valor, "tipo": "receita"})
    # Adicionar Despesa
    elif opcao == 2:
        nome = input("Nome: ")
        # Tratamento de erro
        try:
            valor = float(input("Valor: "))
            total_despesa += valor  # Atualizar o total de despesas
        except ValueError:
            print("Por favor, insira um número válido.")
        fluxo_caixa.append({"nome": nome, "valor": valor, "tipo": "despesa"})
    # Verificar Fluxo
    elif opcao == 3:
        # Calcular o saldo
        saldo = total_receita - total_despesa
        for fc in fluxo_caixa:
            print(f"Nome: {fc['nome']:>15} | Valor: {fc['valor']:>15} | Tipo: {fc['tipo']:>15}")
        print(f"Total Receita: {total_receita} | Total Despesa: {total_despesa}")
        print(f"Saldo: {saldo}")
        # Pausar o programa
        os.system("pause" if os.name == "nt" else "read")
    elif opcao == 4:
        break