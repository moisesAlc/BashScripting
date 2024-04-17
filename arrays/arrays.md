# Arrays

Os arrays em Bash são estruturas de dados que permitem armazenar e manipular múltiplas variáveis sob um único nome. Eles são uma parte essencial da programação em shell, proporcionando uma maneira flexível de lidar com conjuntos de dados e facilitar a execução de tarefas repetitivas ou complexas.

## Tipos de Arrays em Bash
Bash suporta dois tipos principais de arrays:

- **Arrays Indexados**: São arrays nos quais os elementos são indexados numericamente, começando do índice zero. Você pode acessar os elementos usando seus índices numéricos.
- **Arrays Associativos** (ou mapas): Disponíveis a partir do Bash versão 4.0, esses arrays usam strings como chaves ao invés de índices numéricos. Para usar arrays associativos, você precisa declará-los explicitamente antes de usar.

## Declarando e Usando Arrays
### Arrays Indexados
Para declarar e manipular arrays indexados no Bash, você pode usar a seguinte sintaxe:

```bash
# Declarando um array
nomes=("Alice" "Bob" "Charlie")

# Acessando elementos do array
echo "O primeiro nome é ${nomes[0]}"  # Alice
echo "O segundo nome é ${nomes[1]}"  # Bob

# Adicionando elementos
nomes[3]="David"

# Iterando sobre os elementos do array
for nome in "${nomes[@]}"; do
    echo "Nome: $nome"
done

# Tamanho do array
echo "O array tem ${#nomes[@]} elementos."

# Acessando todos os elementos
echo "Todos os nomes: ${nomes[*]}"
```

### Arrays Associativos
Para arrays associativos, a sintaxe muda um pouco, principalmente na declaração e na maneira como você acessa os dados:

```bash

# Declarando um array associativo
declare -A usuarios

# Atribuindo valores
usuarios["alice"]="Admin"
usuarios["bob"]="User"
usuarios["charlie"]="Guest"

# Acessando elementos
echo "Alice é uma ${usuarios[alice]}"

# Iterando sobre chaves e valores
for usuario in "${!usuarios[@]}"; do
    echo "$usuario é um ${usuarios[$usuario]}"
done
```

### Operações Comuns com Arrays

**Adição de elementos**: Como visto nos exemplos, adicionar elementos em um array indexado ou associativo é direto, atribuindo valores a novas chaves ou índices.

**Exclusão de elementos**: Você pode remover elementos de um array usando a unset.

```bash
unset nomes[1]  # Remove o elemento com índice 1
```

**Tamanho do Array**: O número de elementos em um array pode ser obtido por ```${#array[@]}```.

**Listando Chaves e Valores**: Em arrays associativos, ```${!array[@]}``` lista todas as chaves do array.

## Considerações
Arrays em Bash são úteis para scripts que necessitam manipular listas de dados ou configurar múltiplos valores de configuração de forma organizada. No entanto, eles têm algumas limitações em comparação com arrays em linguagens de programação mais completas, como a falta de suporte para arrays multidimensionais nativos e limitações em operações complexas de dados.

[Voltar para Visão Geral](../README.md)