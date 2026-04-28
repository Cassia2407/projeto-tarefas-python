def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nSuas tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa}")


# carregar tarefas do arquivo
try:
    with open("tarefas.txt", "r") as arquivo:
        tarefas = [linha.strip() for linha in arquivo]
except FileNotFoundError:
    tarefas = []


while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        if tarefa.strip():
            tarefas.append(tarefa)

            with open("tarefas.txt", "w") as arquivo:
                for t in tarefas:
                    arquivo.write(t + "\n")

            print("Tarefa adicionada com sucesso!")
        else:
            print("Você não pode adicionar uma tarefa vazia!")

    elif opcao == "2":
        listar_tarefas(tarefas)

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            listar_tarefas(tarefas)

            try:
                numero = int(input("Digite o número da tarefa: "))

                if 1 <= numero <= len(tarefas):
                    removida = tarefas.pop(numero - 1)

                    with open("tarefas.txt", "w") as arquivo:
                        for t in tarefas:
                            arquivo.write(t + "\n")

                    print(f"Tarefa '{removida}' removida com sucesso!")
                else:
                    print("Número inválido.")

            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida.")