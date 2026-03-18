def parseExpressao(linha):
    def estadoNumero(char):
        nonlocal numero
        nonlocal posicao
        if linha[posicao-1] in numeros:
            numero += char
        elif linha[posicao-1] == "(":
            numero += char
        elif linha[posicao-1] == " ":
            numero += char
        if linha[posicao+1] == " ":
            tokens.append(numero)
            numero = ""
        posicao+=1
    def estadoOperadores(char):
        nonlocal divi
        nonlocal posicao
        if linha[posicao+1] != ")":
            divi += char

        elif char == "/":
            divi += char
            tokens.append(divi)
            divi = ""
        else:
            tokens.append(char)
        posicao+=1
    def estadoComandos(char):
        nonlocal comando
        nonlocal posicao
        if char in comandos[0] or char in comandos[1] and char != "(" and char != ")":
            comando+=char
        if len(comando)>=3:
            tokens.append(comando)
            comando = ""
        if char == "(":
            #inicia
            tokens.append(char)
        elif char == ")":
            #finaliza                
            tokens.append(char)
        posicao+=1        

    operadores = ["+","-","*","%","^","/","//"]  
    numeros = ["0","1","2","3","4","5","6","7","8","9", "."]
    comandos = ["RES", "MEM", "(", ")"]
    tokens = []
    posicao = 0
    divi = "" 
    numero = ""
    comando = ""

    
    for char in linha:
        if char == " ":
            posicao+=1
            continue
        elif char in numeros:
            estadoNumero(char)
        elif char in operadores:
            estadoOperadores(char)
        elif char in comandos or char in comandos[0] or char in comandos[1]:
            estadoComandos(char)
    return tokens
