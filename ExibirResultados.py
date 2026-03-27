def exibirResultados(resultados):
    i = 1
    for resultado in resultados:
        if (resultado == None):
            print("Resultado não encontrado")
        else:
            print(f"Resultado da expressão {i} = {resultado:.2f}")
        i += 1
        