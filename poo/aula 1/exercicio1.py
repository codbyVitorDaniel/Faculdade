class Cubo:
    
    def __init__(self,valor):
        self.x = valor
        print('metodo Criado')
    def calcularCubo(self):
        cubo = self.x * self.x * self.x
        return f'Cubo Calculado:{cubo}'

calculoCubo = Cubo(10)
calculo = calculoCubo.calcularCubo()
print(calculo)
