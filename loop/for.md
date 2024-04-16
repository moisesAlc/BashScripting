# For
O loop for no Bash é uma estrutura de controle que permite repetir um bloco de comandos múltiplas vezes. Essa funcionalidade é essencial para automação e manipulação de tarefas repetitivas em shell scripting. O for pode ser usado para iterar sobre uma lista de valores, executar comandos para cada elemento de uma lista de arquivos, ou simplesmente repetir um bloco de comandos um número definido de vezes.

## Sintaxe Básica
O loop for no Bash pode ser escrito de várias maneiras, dependendo do contexto e do que precisa ser iterado. Aqui estão as formas mais comuns de usar o loop for:

### Iterando sobre uma lista de valores
```bash
for var in item1 item2 item3 ... itemN
do
    # Comandos a serem executados para cada item
    echo "$var"
done
```

Neste exemplo, var assume o valor de cada item na lista (item1, item2, etc.), e o bloco de comandos dentro do do...done é executado para cada um desses itens.

### Iterando sobre uma sequência de números

```bash
for i in {1..10}
do
    echo "Número $i"
done
```

Aqui, i iterará de 1 a 10. A sintaxe {1..10} é uma expansão de chaves que gera uma sequência de números de 1 a 10.

### Iterando sobre os resultados de um comando

```bash
for file in $(ls)
do
    echo "Arquivo encontrado: $file"
done
```

Neste exemplo, file irá conter o nome de cada arquivo no diretório atual, um de cada vez, como resultado do comando ls.

### Exemplos de Uso Prático

#### Processamento de arquivos
Um uso comum do loop for é processar uma série de arquivos em um diretório:

```bash
for img in *.jpg
do
    convert "$img" "${img%.jpg}.png"
done
```

Este script converterá todos os arquivos .jpg em um diretório para o formato .png usando o comando convert do ImageMagick.

#### Gerando relatórios

```bash
for user in $(cut -d: -f1 /etc/passwd)
do
    echo "Relatório para usuário: $user"
    # Comandos para gerar relatório
done
```

Este exemplo gera um relatório para cada usuário listado no arquivo /etc/passwd.

## Boas Práticas

### Citação de variáveis: 
Sempre coloque as variáveis entre aspas duplas para evitar problemas com nomes de arquivos ou valores que contêm espaços.

### Verifique o conteúdo das listas: 
Certifique-se de que a lista que você está iterando contém os valores esperados para evitar a execução de comandos em elementos indesejados ou mal formatados.

### Evite subshells desnecessários: 
Embora seja útil iterar sobre a saída de um comando, isso pode ser ineficiente se a saída for grande. Considere alternativas, como gerar a lista de itens em um arquivo temporário e iterar sobre ele.

[Voltar para Visão Geral](../visao_geral.md)