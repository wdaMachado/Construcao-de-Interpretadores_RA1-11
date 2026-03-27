from AnalisadorLexico import *

teste = "((5 2 *) (3 2 +) /)"
teste1 = "(5.3.2 2 *)"
teste2 = "(3.14 (4.234 1 *) +)"
teste3 = "((2.42 9.3 +) (2.7 4.5 %) //)"
teste4 = "(4 MEM)"
teste5 = "(1 2 +)"
testes = []
tokens = parseExpressao(teste)
tokens1 = parseExpressao(teste1)
tokens2 = parseExpressao(teste2)
tokens3 = parseExpressao(teste3)
tokens4 = parseExpressao(teste4)
tokens4 = parseExpressao(teste5)

testes.append(tokens)
testes.append(tokens1)
testes.append(tokens2)
testes.append(tokens3)
testes.append(tokens4)
with open("tokens.txt", "w") as file:
    for token in tokens3:
        file.write(token)
# print(tokens3)
for teste in testes:
    for token in teste:
        print(token , end = " ")
    print("\n")
print("\n")