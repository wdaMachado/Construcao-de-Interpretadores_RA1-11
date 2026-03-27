# Construcao-de-Interpretadores_RA1-11

Pedro Bittencourt<br>
Pedro Bueno<br>
Pedro Lyra<br>
William

## 1. Gerar o Assembly 

No terminal, execute o comando passando o seu arquivo de texto:
```
python main.py seu_arquivo.txt
```

Isso criará o arquivo assembly.s na pasta do projeto.

##  2. Executar no Hardware (CPULator)
1. Acesse o CPULator (ARMv7 DE1-SoC).

2. Limpe o editor, cole o conteúdo de assembly.s e clique em Compile and Load.

3. Pressione F3 (Continue) para processar todas as expressões.

## 3. Validar e Salvar Resultados (Memória)
Para visualizar e exportar os dados calculados pelo processador:

- No painel Memory, procure a caixa Go to address, digite RES_ARRAY e mude o formato para Double.


- Para salvar o arquivo de texto com os dados:

1. Clique no botão Settings (ou ícone de engrenagem) no painel de memória.

2. Selecione Download Memory Content.

3. Configure os campos:
Start address: (Endereço do RES_ARRAY).
Size: (Suficiente para cobrir as linhas de teste).

4. Clique em Download para baixar o arquivo com os resultados brutos.
