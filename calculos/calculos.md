# Cálculos

Realizar cálculos em Bash é um aspecto fundamental para muitos scripts que lidam com lógica numérica, automação de tarefas e manipulação de dados. Bash fornece várias maneiras de executar operações matemáticas básicas e avançadas. Embora não seja tão robusto quanto as linguagens de programação projetadas especificamente para matemática pesada, Bash é bastante capaz de lidar com a maioria das necessidades de cálculo em scripts de shell.

## Utilizando o Comando `expr`
O comando expr é uma das ferramentas mais antigas disponíveis em shell scripts para avaliar expressões. Ele é usado principalmente para operações aritméticas inteiras básicas, como adição, subtração, multiplicação e divisão.

## Exemplo Básico
```bash
#!/bin/bash

# Adição
resultado=$(expr 5 + 3)
echo "Resultado da adição: $resultado"

# Subtração
resultado=$(expr 10 - 4)
echo "Resultado da subtração: $resultado"

# Multiplicação (note o uso de escape para o asterisco)
resultado=$(expr 6 \* 2)
echo "Resultado da multiplicação: $resultado"

# Divisão
resultado=$(expr 10 / 2)
echo "Resultado da divisão: $resultado"
```

Uma limitação do `expr` é que ele só lida com números inteiros e requer que operadores como * (multiplicação) sejam escapados para evitar que sejam interpretados como caracteres especiais pelo shell.

## Aritmética Bash com ```((...))```

Para uma maneira mais integrada e flexível de fazer cálculos em Bash, você pode usar a expansão aritmética com ```((...))```. Essa abordagem suporta uma gama mais ampla de operadores matemáticos e não exige o uso de um subshell externo ou comandos adicionais como expr.

## Exemplo com ((...))
```bash
#!/bin/bash

# Adição
resultado=$((5 + 3))
echo "Resultado da adição: $resultado"

# Subtração
resultado=$((10 - 4))
echo "Resultado da subtração: $resultado"

# Multiplicação
resultado=$((6 * 2))
echo "Resultado da multiplicação: $resultado"

# Divisão
resultado=$((10 / 2))
echo "Resultado da divisão: $resultado"
```

A sintaxe ```((...))``` é mais limpa e mais fácil de usar para cálculos diretos em scripts. Além disso, ela permite incrementos, decrementos e uma variedade de operações bit a bit.

Usando bc para Cálculos de Ponto Flutuante
Para cálculos mais complexos, especialmente aqueles que envolvem ponto flutuante, Bash pode utilizar o comando bc (Basic Calculator), uma calculadora de precisão arbitrária que pode executar uma grande variedade de operações matemáticas.

## Exemplo com ```bc```
```bash
#!/bin/bash

# Cálculo com ponto flutuante
resultado=$(echo "scale=2; 10 / 3" | bc)
echo "Resultado da divisão com ponto flutuante: $resultado"
```

Neste exemplo, ```scale=2``` define o número de dígitos decimais no resultado. O comando ```bc``` é poderoso e pode lidar com expressões matemáticas complexas, variáveis, funções matemáticas padrão e até mesmo script diretamente dentro de suas operações.

[Voltar para Visão Geral](../visao_geral.md)