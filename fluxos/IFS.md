# IFS

O IFS, ```ou Internal Field Separator```, é uma variável crucial no shell Bash que define o delimitador que o Bash usa para dividir strings em palavras durante a leitura de entradas e o processamento de comandos. Essa variável de ambiente desempenha um papel fundamental em como o Bash interpreta os dados de entrada e como manipula a expansão de palavras.

## Função do IFS
O valor padrão do IFS inclui espaço, tabulação e nova linha, que são usados para separar campos em comandos shell. **Isso significa que, por padrão, quando o Bash lê uma linha de texto, ele considera espaços, tabs e quebras de linha como delimitadores para dividir a linha em palavras separadas.**

## Modificando o IFS
Você pode modificar o IFS para mudar o comportamento de como strings são divididas em comandos e scripts. Isso é particularmente útil em scripts que precisam processar entradas de texto formatadas de maneira específica, como dados separados por vírgulas ou outros delimitadores personalizados.

## Exemplo de Uso do IFS
Suponha que você tenha uma string de dados separados por vírgulas e queira iterar sobre cada item. Você pode ajustar o IFS para tratar a vírgula como delimitador:

```bash
string="um,dois,três,quatro"
IFS=','  # Ajustando o IFS para vírgula
for item in $string; do
    echo "Item: $item"
done
```

Neste exemplo, o loop for vai iterar sobre cada termo separado por vírgula na string. Resetar o IFS após o uso é uma boa prática para evitar comportamentos inesperados em outras partes do script:

```bash
old_IFS="$IFS"  # Salva o IFS antigo
IFS=','         # Novo IFS para vírgula
# Processamento aqui
IFS="$old_IFS"  # Restaura o IFS original
```

## Considerações ao Usar IFS
### Limitar o Escopo: 
Alterações no IFS podem afetar comandos subsequentes e comportamentos de script. É uma boa prática limitar a modificação do IFS ao escopo onde ela é necessária, ou garantir que o IFS seja restaurado ao seu valor original depois de usado.
### Dados com Espaços: 
Se o IFS inclui o espaço (como no padrão), dados que contêm espaços podem ser inesperadamente divididos. Isso deve ser levado em conta ao processar texto que pode incluir espaços significativos.
### Uso em Funções: 
Para evitar efeitos colaterais, é recomendável alterar o IFS dentro de funções usando variáveis locais para IFS, mantendo assim o resto do script inalterado.
### IFS e Leitura de Dados
Ao usar o comando read, o IFS também afeta como a entrada é lida. Por exemplo:

```bash
read -p "Digite dois nomes separados por espaço: " nome1 nome2
```
Se o IFS estiver configurado para espaço, ```nome1``` receberá a primeira palavra e ```nome2``` receberá o restante da linha.

[Voltar para Visão Geral](../visao_geral.md)