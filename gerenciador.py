def menu():

    tarefas = {}
    opcao = 0

    while opcao != -1:

        print("1 - Adicionar nova tarefa\n"
              "2 - Marcar tarefa como concluida\n"
              "3 - Marcar tarefa como pendência\n"
              "4 - Marcar todas como concluídas\n"
              "5 - Marcar todas como pendências\n"
              "6 - Deletar tarefa\n"
              "7 - Deletar todas as tarefas\n"
              "8 - Passar para .txt\n"
              "9 - Visualizar tarefas\n"
              "-1 - Sair do programa\n\n")

        opcao = int(input("Qual opcão você deseja executar? "))

        if opcao == 1:

            addTarefa(tarefas)

        elif opcao == 2:

            alterarValor(tarefas, "1")

        elif opcao == 3:

            alterarValor(tarefas, "0")

        elif opcao == 4:

            alterarTodas(tarefas, "1")

        elif opcao == 5:

            alterarTodas(tarefas, "0")

        elif opcao == 6:

            delTarefa(tarefas)

        elif opcao == 7:

            deletarTodas(tarefas)

        elif opcao == 8:

            convTxt(tarefas)

        elif opcao == 9:

            printTarefas(tarefas)

        else:

            print("Valor inválido! Digite novamente.")


def addTarefa(tarefas):

    nova_tarefa = input("Qual será o nome dessa tarefa? ")

    tarefas[nova_tarefa] = "0"

    print("Tarefa adicionada!\n")

    rep = int(input("Deseja continuar adicionando (1 para continuar)? "))

    if rep == 1:

        addTarefa(tarefas)

    else:

        return tarefas

def alterarValor(tarefas, concluida):

    """
    concluido indicará se a tarefa dever ser marcada como concluida ou não
    se 0 = pendência, se 1 = concluído
    """

    tarefa_selecionada = input("Que tarefa você deseja alterar? ")

    tarefas[tarefa_selecionada] = concluida

    print("Tarefa alterada!\n")

    rep = int(input("Deseja continuar alterando (1 para continuar)? "))

    if rep == 1:

        alterarValor(tarefas, concluida)

    else:

        return tarefas

def alterarTodas(tarefas, concluida):

    for i in tarefas:

        tarefas[i] = concluida

    print("Tarefas alteradas!\n")

    return tarefas


def delTarefa(tarefas):

    excluir_tarefa = input("Qual tarefa você deseja deletar? ")

    del tarefas[excluir_tarefa]

    print("Tarefa deletada!\n")

    rep = int(input("Deseja continuar deletando (1 para continuar)? "))

    if rep == 1:

        delTarefa(tarefas)

    else:

        return tarefas


def deletarTodas(tarefas):

    print("Tarefas deletadas!")

    return tarefas.clear()


def convTxt(tarefas):

    with open("tarefas.txt", "w") as arquivo:

        for i in tarefas:

            if int(tarefas[i]):

                arquivo.write(f"{i}: Concluído\n")

            else:

                arquivo.write(f"{i}: Pendente\n")


def printTarefas(tarefas):

    for i in tarefas:

        if int(tarefas[i]):

            print(f"{i}: Concluído")

        else:

            print(f"{i}: Pendente")


menu()
