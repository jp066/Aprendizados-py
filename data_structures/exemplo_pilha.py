# pilha implementation in python


# Creating a pilha
def create_pilha():
    pilha = []
    return pilha


# Creating an vazio pilha
def check_vazio(pilha):
    return len(pilha) == 0


# Adding items into the pilha
def push_pilha(pilha, item):
    pilha.append(item)
    print("push item: " + item)


# Removing an element from the pilha
def pop_pilha(pilha):
    if (check_vazio(pilha)):
        return "pilha esta vazio"

    return pilha.pop()

def desempilhar_todas(pilha):
    while not check_vazio(pilha):
        print("item desempilhado: " + pop_pilha(pilha))
    print("pilha após desempilhar todos os elementos: " + str(pilha))

pilha = create_pilha()
push_pilha(pilha, str(1))
push_pilha(pilha, str(2))
push_pilha(pilha, str(3))
push_pilha(pilha, str(4))

desempilhar_todas(pilha)