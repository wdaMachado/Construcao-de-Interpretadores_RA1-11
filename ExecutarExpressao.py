
def executarExpressao(tokens):

    def memoria(a):
        return 0

    def resposta(a):
        return 0
    
    def tipagem(val):

        if val in ["MEM","RES"]:
            return str(val)
        else:
            return float(val)
            
    def resolver_expressao(exp_tokens):

        operador = exp_tokens[-1]
        a = tipagem(exp_tokens[0])
        b = tipagem(exp_tokens[1])

        operadores = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "//": lambda a, b: a // b,
            "%": lambda a, b: a % b,
            "^": lambda a, b: a ** b,
            "MEM": lambda a,b: memoria(a),
            "RES": lambda a,b: resposta(a)
        }

        resultado = operadores[operador](a,b)
        print(exp_tokens)
        print(resultado)
        return resultado

    tokens = list(tokens)
    pilha_aberturas = []
    index = 0

    while index < len(tokens):
        token = tokens[index]

        if token == "(":
            pilha_aberturas.append(index)
            index += 1
            continue

        if token == ")":
            
            abertura = pilha_aberturas.pop()
            exp_interna = tokens[abertura + 1:index]
            resultado = resolver_expressao(exp_interna)

            tokens[abertura:index + 1] = [float(resultado)]
            index = abertura
            continue

        index += 1

    if len(tokens) == 1:
        return tokens[0]
