# Funções em Shell Scripting

As funções em shell scripting, especialmente em Bash, são blocos de código reutilizáveis que você pode definir uma vez e chamar em várias partes do seu script. Elas são semelhantes às funções em outras linguagens de programação e servem para modularizar e organizar o código, tornando os scripts mais limpos, mais eficientes e mais fáceis de manter. Aqui está uma visão geral sobre como criar, usar e tirar proveito das funções em shell scripts.

## Definição de Função
Uma função em Bash é definida com a seguinte sintaxe:

```bash
nome_da_funcao() {
    # comandos
}
```
Você pode também definir funções usando a palavra-chave function, embora isso não seja necessário no Bash moderno:

```bash
function nome_da_funcao {
    # comandos
}
```

## Características das Funções
### Escopo de Variáveis: 
Por padrão, as variáveis em Bash são globais. No entanto, você pode declarar variáveis locais dentro de funções usando a palavra-chave local. Isso é útil para evitar conflitos de nomes de variáveis e manter a independência de cada função.

### Passagem de Argumentos: 
As funções podem aceitar argumentos. Dentro da função, você pode acessar esses argumentos através das variáveis $1, $2, $3, etc., que representam o primeiro, segundo, terceiro argumento, e assim por diante.

### Retorno de Valores: 
As funções em Bash usam o comando return para terminar sua execução e opcionalmente retornar um código de saída numérico (geralmente usado para indicar sucesso ou falha). Para retornar strings ou outros valores, você geralmente usa eco (echo) e captura essa saída onde a função foi chamada.

### Exemplo Prático
Aqui está um exemplo de uma função simples em Bash:

```bash
function saudacao {
    nome=$1
    echo "Olá, $nome!"
}
```

Lembrando que $1 é o primeiro argumento passado à função, $2 é o segundo, etc. 

Você pode chamar essa função com um argumento assim:

```bash
saudacao "Maria"
```

Isso imprimirá:

```
Olá, Maria!
```

## Ver Mais

### Verifique [entrada de usuário](entrada_usuario\entrada.md)

[Voltar para Visão Geral](../visao_geral.md)