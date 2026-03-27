def executarExpressao(tokens):

    def memoria(a):
        return 0.0 

    def resposta(a):
        return 0.0 
    
    def tipagem(val):
        if val in ["MEM", "RES"]:
            return str(val)
        try:
            return float(val)
        except ValueError:
            return 0.0
            
    def resolver_expressao(exp_tokens):
        if not exp_tokens:
            return 0.0
            
        operador = exp_tokens[-1]

        if len(exp_tokens) == 1:
            return memoria(operador)

        if len(exp_tokens) == 2:
            a = tipagem(exp_tokens[0])
            if operador == "MEM":
                return memoria(a)
            elif operador == "RES":
                return resposta(a)
            return a

        if len(exp_tokens) >= 3:
            a = tipagem(exp_tokens[0])
            b = tipagem(exp_tokens[1])

            operadores = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b,
                "//": lambda a, b: a // b,
                "%": lambda a, b: a % b,
                "^": lambda a, b: a ** b
            }
            
            if operador in operadores:
                return operadores[operador](a, b)
            
        return 0.0

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
            if pilha_aberturas:
                abertura = pilha_aberturas.pop()
                exp_interna = tokens[abertura + 1:index]
                resultado = resolver_expressao(exp_interna)

                tokens[abertura:index + 1] = [float(resultado)]
                index = abertura + 1
                continue
            else:
                index += 1
                continue

        index += 1

    return tokens[0] if tokens else 0.0