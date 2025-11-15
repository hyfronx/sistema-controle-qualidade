# Sistema de Controle de Qualidade

todas_pecas = []
pecas_aprovadas = []
pecas_reprovadas = []
caixa_atual = []
caixas_fechadas = []


PESO_MIN = 95
PESO_MAX = 105
COMPRIMENTO_MIN = 10
COMPRIMENTO_MAX = 20


def verificar_peca(peso, cor, comprimento):
    motivo = ""
    aprovada = True

    if peso < PESO_MIN or peso > PESO_MAX:
        motivo = motivo + "Peso fora do padrão. "
        aprovada = False

    if cor != "azul" and cor != "verde":
        motivo = motivo + "Cor inválida. "
        aprovada = False

    if comprimento < COMPRIMENTO_MIN or comprimento > COMPRIMENTO_MAX:
        motivo = motivo + "Comprimento fora do padrão. "
        aprovada = False

    return aprovada, motivo


def cadastrar_peca():
    print("\n--- CADASTRAR NOVA PEÇA ---")
    id_peca = input("ID da peça: ")

    for peca in todas_pecas:
        if peca["id"] == id_peca:
            print("✗ Erro! Já existe uma peça com este ID.")
            return

    peso = float(input("Peso (g): "))
    cor = input("Cor: ")
    comprimento = float(input("Comprimento (cm): "))

    aprovada, motivo = verificar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": "aprovada" if aprovada else "reprovada",
        "motivo": motivo
    }

    todas_pecas.append(peca)

    if aprovada:
        print("✓ Peça APROVADA")
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)

        # Verificar se a caixa está cheia
        if len(caixa_atual) == 10:
            print("📦 Caixa cheia! Fechando caixa número", len(caixas_fechadas) + 1)
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
    else:
        print("✗ Peça REPROVADA")
        print("Motivo:", motivo)
        pecas_reprovadas.append(peca)


def listar_pecas():
    print("\n--- LISTAR PEÇAS ---")
    print("1. Ver peças aprovadas")
    print("2. Ver peças reprovadas")
    print("3. Ver todas as peças")

    sub_opcao = input("\nEscolha: ")

    if sub_opcao == "1":
        print("\n=== PEÇAS APROVADAS ===")
        if len(pecas_aprovadas) == 0:
            print("Nenhuma peça aprovada ainda.")
        else:
            for peca in pecas_aprovadas:
                print(
                    f"ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")

    elif sub_opcao == "2":
        print("\n=== PEÇAS REPROVADAS ===")
        if len(pecas_reprovadas) == 0:
            print("Nenhuma peça reprovada.")
        else:
            for peca in pecas_reprovadas:
                print(
                    f"ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
                print(f"Motivo: {peca['motivo']}")
                print()

    elif sub_opcao == "3":
        print("\n=== TODAS AS PEÇAS ===")
        if len(todas_pecas) == 0:
            print("Nenhuma peça cadastrada ainda.")
        else:
            for peca in todas_pecas:
                print(
                    f"ID: {peca['id']} | Status: {peca['status']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")


def remover_peca():
    print("\n--- REMOVER PEÇA ---")
    id_remover = input("Digite o ID da peça que deseja remover: ")

    peca_encontrada = False

    for peca in todas_pecas:
        if peca["id"] == id_remover:
            peca_encontrada = True

            todas_pecas.remove(peca)

            if peca["status"] == "aprovada":
                pecas_aprovadas.remove(peca)
                if peca in caixa_atual:
                    caixa_atual.remove(peca)
            else:
                pecas_reprovadas.remove(peca)

            print(f"✓ Peça {id_remover} removida com sucesso!")
            break

    if not peca_encontrada:
        print("✗ Peça não encontrada!")


def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")
    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa foi fechada ainda.")
    else:
        for i in range(len(caixas_fechadas)):
            print(f"\nCaixa {i + 1}:")
            print(f"Total de peças: {len(caixas_fechadas[i])}")
            print("IDs das peças:", end=" ")
            for peca in caixas_fechadas[i]:
                print(peca["id"], end=" ")
            print()

    if len(caixa_atual) > 0:
        print(f"\nCaixa em preenchimento (Caixa {len(caixas_fechadas) + 1}):")
        print(f"Peças na caixa: {len(caixa_atual)}/10")
        print("IDs das peças:", end=" ")
        for peca in caixa_atual:
            print(peca["id"], end=" ")
        print()


def gerar_relatorio():
    print("\n" + "=" * 50)
    print("RELATÓRIO FINAL DE PRODUÇÃO")
    print("=" * 50)

    total_pecas = len(todas_pecas)
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_caixas = len(caixas_fechadas)
    if len(caixa_atual) > 0:
        total_caixas = total_caixas + 1

    print(f"\nTotal de peças processadas: {total_pecas}")
    print(f"Peças aprovadas: {total_aprovadas}")
    print(f"Peças reprovadas: {total_reprovadas}")
    print(f"Caixas utilizadas: {total_caixas}")

    if len(pecas_reprovadas) > 0:
        print("\n--- DETALHES DAS REPROVAÇÕES ---")
        for peca in pecas_reprovadas:
            print(f"Peça {peca['id']}: {peca['motivo']}")

    print("\n--- DETALHES DAS CAIXAS ---")
    for i in range(len(caixas_fechadas)):
        print(f"Caixa {i + 1}: 10 peças (FECHADA)")

    if len(caixa_atual) > 0:
        print(f"Caixa {len(caixas_fechadas) + 1}: {len(caixa_atual)} peças (EM PREENCHIMENTO)")

    print("\n" + "=" * 50)


def mostrar_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("6. Sair")


def main():
    print("Sistema de Controle de Qualidade")
    print("-" * 40)

    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("\nEncerrando o sistema...")
            print("Até logo!")
            break
        else:
            print("✗ Opção inválida! Tente novamente.")


main()