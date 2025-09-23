#Implementaçao de uma pilha
'''
Push - inclui elementos no inicio da lista 
pop - remove um item do topo da pilha e retorna o valor desse item
size - retorna o tamanho da pilha
'''
#Criaçao da Classe
class Stack:
    #Criaçao da Classe 
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def peek(self):
        #return the top element
        if self.size() == 0:
            return self.items[0]
    def pop (self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()
# Fim da Classe