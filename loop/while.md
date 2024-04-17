# While

O loop while no Bash é uma estrutura de controle fundamental que permite repetir um conjunto de comandos enquanto uma condição especificada é verdadeira. É muito usado em scripts de shell para automatizar e gerenciar tarefas repetitivas que precisam continuar até que uma determinada condição seja alterada, como esperar por uma mudança em um arquivo, processar dados até que acabem, ou executar uma tarefa de manutenção recorrente.

## Sintaxe Básica do Loop while
A sintaxe do loop while é simples e direta:

```bash
while [ condição ]
do
    # Comandos a serem executados enquanto a condição for verdadeira
done
```

### condição: 
uma expressão que é avaliada antes de cada passagem pelo loop. Se a condição for verdadeira (ou seja, se a expressão retornar zero, que é considerado sucesso em Bash), o bloco de comandos dentro do loop será executado.
### do...done: 
delimita os comandos que são executados repetidamente enquanto a condição for verdadeira.

## Exemplos Práticos de Uso

### Esperando por um Arquivo
Um uso comum do while é esperar até que um arquivo específico seja criado:

```bash
while [ ! -f "/tmp/arquivo_pronto.txt" ]
do
    echo "Aguardando o arquivo ser criado..."
    sleep 1
done
echo "Arquivo criado, procedendo com o script..."
```

Este script verifica a existência de um arquivo a cada segundo, e prossegue com a execução do restante do script assim que o arquivo é detectado.

### Lendo Linhas de um Arquivo
O loop while também é útil para ler linhas de um arquivo, uma a uma:

```bash
while IFS= read -r linha
do
    echo "Processando: $linha"
done < "arquivo.txt"
```

#### Para entender melhor o uso do [IFS](fluxos\IFS.md)

Neste exemplo, cada linha do arquivo arquivo.txt é lida e processada sequencialmente até que o fim do arquivo seja alcançado.

## Boas Práticas com o Loop while

## Evite loops infinitos: 
Garanta que a condição do loop while possa eventualmente se tornar falsa. Caso contrário, o loop continuará indefinidamente, o que pode resultar em uso excessivo de recursos ou comportamentos não desejados.
## Use sleeps para reduzir carga: 
Em loops while que envolvem esperar por eventos (como a criação de um arquivo ou mudanças de status), é uma boa prática usar sleep para evitar que o loop consome excessivamente a CPU.
## Tratamento de sinais: 
Em scripts mais complexos que podem ser interrompidos, considerar o tratamento de sinais para sair de loops while de maneira limpa é crucial, usando por exemplo [trap](..\trap\trap.md) para capturar sinais e limpar recursos antes de sair.

[Voltar para Visão Geral](../README.md)