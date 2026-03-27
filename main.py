import sys
from lerArquivo import lerArquivo
from AnalisadorLexico import parseExpressao
from ExecutarExpressao import executarExpressao
from gerarAssembly import gerarAssembly
from ExibirResultados import exibirResultados

def main():
    if len(sys.argv) != 2:
        print("Número incorreto de parametros, é necessário informar apenas o arquivo .txt")
        sys.exit(1)
    nomeArquivo = sys.argv[1]

    try:
        arquivo = lerArquivo(nomeArquivo)
        resultados = []
        expressoes = []
        for linha in arquivo:
            expressao = parseExpressao(linha)
            resultado = executarExpressao(expressao)
            expressoes.extend(expressao)
            resultados.append(resultado)
        
        assembly = gerarAssembly(expressoes)
        saida = "assembly.s"

        with open(saida, "w", encoding="utf-8") as arquivo:
            arquivo.write(assembly)
        exibirResultados(resultados)
    except FileNotFoundError:
        print("arquivo não encontrado!")


if __name__ == "__main__":
    main()