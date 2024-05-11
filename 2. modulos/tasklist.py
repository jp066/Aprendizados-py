import datetime
import pickle
import os

# Classe para representar uma tarefa
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

# Função para adicionar uma nova tarefa
def add_task(task_list):
    description = input("Descrição da tarefa: ")
    due_date_str = input("Data de vencimento (formato: AAAA-MM-DD HH:MM): ")
    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")
    task = Task(description, due_date)
    task_list.append(task)
    print("Tarefa adicionada com sucesso.")

# Função para exibir todas as tarefas
def display_tasks(task_list):
    if not task_list:
        print("Nenhuma tarefa encontrada.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task.description} - Data de vencimento: {task.due_date}")

# Função principal
def main():
    # Verifica se o arquivo de tasklist já existe
    if os.path.exists("tasklist.pkl"):
        with open("tasklist.pkl", "rb") as file:
            task_list = pickle.load(file)
    else:
        task_list = []

    while True:
        print("\n=== Task List ===")
        print("1. Adicionar Tarefa")
        print("2. Exibir Tarefas")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            display_tasks(task_list)
        elif choice == "3":
            # Salva a lista de tarefas em um arquivo antes de sair
            with open("tasklist.pkl", "wb") as file:
                pickle.dump(task_list, file)
            print("Tasklist salva. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
