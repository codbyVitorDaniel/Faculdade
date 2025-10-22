# 1) Soma de ingressos dos quiosques (lista de números)
# Enunciado: Some recursivamente o total de ingressos vendidos pelos quiosques da
# orla de Itaipuaçu, dados em uma lista de inteiros.
# Ex.: [12, 7, 5] → 24
# Assinatura sugerida: soma(lista)

def soma(lista):
    if not lista:
        return 0
    return lista[0] + soma(lista[1:])
ingressos = [12, 7, 5]
print(soma(ingressos))  

# 2) Quantas vezes “Maricá” aparece? (string)
# Enunciado: Dada uma string, conte recursivamente quantas vezes a palavra
# "Maricá" aparece.
# Ex.: "Maricá é linda. Maricá tem lagoas." → 2
# Assinatura: conta_marica(texto)
# Dica: teste se o prefixo começa com "Maricá" e avance 1 caractere a cada
# chamada.

def conta(texto):
    if len(texto) < len("Maricá"):
        return 0
    if texto.startswith("Maricá"):
        return 1 + conta(texto[1:])
    else:
        return conta(texto[1:])


frase = "Maricá é linda. Maricá tem lagoas."
print(conta(frase))


# 3) Reverter nome de bairro (string)
# Enunciado: Inverta recursivamente o nome de um bairro.
# Ex.: "Itaipuaçu" → "uçaupIat"
# Assinatura: reverter(s)
# Dica: último caractere + reverter(restante sem último).

def reverter(s):
    if len(s) == 0:
        return s
    return s[-1] + reverter(s[:-1])
bairro = "Itaipuaçu"
print(reverter(bairro))  


# 4) Fatorial de moradores (n!)
# Enunciado: Calcule recursivamente o fatorial de n (número fictício de combinações
# de equipes em um evento na praça).
# Ex.: 5 → 120
# Assinatura: fatorial(n)
# Dica: caso base: n <= 1 → 1; senão: n * fatorial(n-1).

def fator(n):
    if n <= 1:
        return 1
    return n * fator(n - 1)
print(fator(5))  


# 5) Maior nota de evento (lista)
# Enunciado: Encontre recursivamente o maior valor em uma lista de notas de um
# evento cultural em Ponta Negra.
# Ex.: [7.5, 8.2, 9.0, 8.8] → 9.0
# Assinatura: maximo(lista)
# Dica: compare o primeiro com o máximo do resto.

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    resto = maximo(lista[1:])
    if lista[0] > resto:
        return lista[0]
    else:
        return resto
notas = [7.5, 8.2, 9.0, 8.8]
print(maximo(notas))

# 6) Desconto em série (aplicado item a item)
# Enunciado: Dada uma lista de preços da feira de Araçatiba, aplique recursivamente
# um desconto d% em todos os itens, retornando nova lista.
# Ex.: ([10, 20], 10) → [9.0, 18.0]
# Assinatura: aplica_desconto(lista, d)
# Dica: novo_primeiro = primeiro*(1-d/100) + aplica_desconto(resto, d).

def aplica(lista, d):
    if not lista:
        return []
    novo = lista[0] * (1 - d / 100)
    return [novo] + aplica(lista[1:], d)
precos = [10, 20]
print(aplica(precos, 10)) 


# 7) Contar pares na lista (números)
# Enunciado: Conte recursivamente quantos números pares há em uma lista de
# medições simples de um posto de monitoramento.
# Ex.: [2, 3, 4, 7, 8] → 3
# Assinatura: conta_pares(lista)
# Dica: se primeiro é par, 1 + conta(resto); senão, conta(resto).

def contar(lista):
    if not lista:
        return 0
    if lista[0] % 2 == 0:
        return 1 + contar(lista[1:])
    else:
        return contar(lista[1:])

medicoes = [2, 3, 4, 7, 8]
print(contar(medicoes))  


# 8) Potência de 2 (sem loops)
# Enunciado: Calcule recursivamente 2^n, interpretando como dobrar a capacidade
# de atendimento a cada passo.
# Ex.: n=5 → 32
# Assinatura: pot2(n)
# Dica: caso base: n <= 0 → 1; senão 2 * pot2(n-1).


def pot2(n):
    if n <= 0:
        return 1
    return 2 * pot2(n - 1)
print(pot2(5))  
