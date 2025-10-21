# #Implementaçao de uma pilha
# '''
# Push - inclui elementos no inicio da lista 
# pop - remove um item do topo da pilha e retorna o valor desse item
# size - retorna o tamanho da pilha
# '''
# #Criaçao da Classe
# class Stack:
#     #Criaçao da Classe 
#     def __init__(self):
#         self.items = []
#     def push(self, item):
#         self.items.append(item)
        
#     def size(self):
#         return len(self.items)
    
#     def peek(self):
#         #return the top element
#         if self.size() == 0:
#             return self.items[0]
#     def pop (self):
#         if self.size() == 0:
#             return None
#         else:
#             return self.items.pop()
# # Fim da Classe

class Fila:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue (self):
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    
    
fila_atendimento = Fila()
fila_atendimento.enqueue("Marcio")
fila_atendimento.enqueue("Alexandre")
fila_atendimento.enqueue("Dias")
fila_atendimento.enqueue("Garrido")

while not fila_atendimento.is_empty():
    cliente_atual = fila_atendimento.dequeue()
    print(f"Atendendo o cliente {cliente_atual}")