# Case

A estrutura case em shell scripting é uma poderosa ferramenta de controle de fluxo que permite a execução de blocos de comandos baseados no valor de uma variável ou expressão. É semelhante à instrução switch encontrada em outras linguagens de programação como C, Java ou Python. A sintaxe do case facilita a leitura e a manutenção de scripts, especialmente quando você precisa lidar com múltiplas condições que direcionam para diferentes blocos de código.

## Sintaxe Básica
A estrutura case em Bash tem a seguinte forma:

```bash
case "valor" in
  padrão1)
    # Comandos para o padrão1
    ;;
  padrão2)
    # Comandos para o padrão2
    ;;
  *)
    # Comandos padrão (opcional)
    ;;
esac
```

- **case "valor"**: Inicia a declaração do case. Aqui, "valor" é a variável ou expressão que será comparada com os padrões especificados nos case labels.
- **padrão)**: Cada caso dentro de uma estrutura case começa com um padrão seguido de um parêntese. Este padrão é uma expressão que, se correspondida com o valor após o case, executará os comandos associados até encontrar um ;;.
- **;;**: Delimitador que encerra um bloco de comandos dentro de um caso específico.
- ***)**: Um caso especial que funciona como um catch-all, que será executado se nenhum outro padrão for correspondido.
- **esac**: Marca o fim de uma declaração case.

## Exemplos de Uso

### Exemplo 1: Script de Menu Simples
```bash
#!/bin/bash

echo "Escolha uma opção:"
echo "1 - Listar arquivos"
echo "2 - Mostrar data atual"
echo "q - Sair"
read opcao

case "$opcao" in
  1)
    ls -l
    ;;
  2)
    date
    ;;
  q)
    echo "Saindo..."
    exit 0
    ;;
  *)
    echo "Opção inválida!"
    ;;
esac
```

Neste exemplo, o script apresenta um menu simples ao usuário e executa diferentes comandos com base na escolha do usuário.

### Exemplo 2: Manipulação de Strings
```bash
#!/bin/bash

read -p "Digite uma palavra: " palavra

case "$palavra" in
  a*|A*)
    echo "Sua palavra começa com A."
    ;;
  z*|Z*)
    echo "Sua palavra começa com Z."
    ;;
  *)
    echo "Sua palavra não começa com A nem com Z."
    ;;
esac
```

Aqui, o script verifica se uma palavra começa com 'A' ou 'Z', demonstrando o uso de padrões com globbing (curingas como *).

## Vantagens do Uso do Case
- Legibilidade: case torna scripts mais legíveis e fáceis de entender, especialmente ao lidar com várias condições.
- Manutenção: É mais fácil adicionar novos casos em uma estrutura case do que modificar uma longa série de if-elif-else.
- Eficiência: Em alguns contextos, case pode ser mais eficiente do que múltiplos if-elif statements, especialmente quando lidando com padrões de texto.

[Voltar para Visão Geral](../README.md)