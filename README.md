# Shell Scripting com Bash

Material de estudo e prática em **Shell Scripting** (Bash): notas conceituais, exemplos curtos e atividades guiadas. O foco é automação no terminal, fluxo de dados (pipes e redirecionamento), controle de execução e boas práticas básicas.

Leia primeiro [O que é um shell?](shell/shell.md) (conceito, histórico, empilhamento, compatibilidade e uso no Windows/macOS).

## Objetivos

- Dominar sintaxe e idiomas comuns do Bash para scripts reutilizáveis.
- Entender **condicionais**, **loops**, **funções**, **arrays** e manipulação de texto.
- Usar **pipes**, **redirecionamento** e variáveis como `IFS` de forma consciente.
- Trabalhar com **entrada do usuário**, **cálculos** e ferramentas auxiliares (por exemplo `tmux` para sessões persistentes no terminal).

## Pré-requisitos

- Linux ou ambiente compatível com **Bash** (versão 4+ recomendada para alguns recursos de arrays). No Windows ou macOS, veja [shell/shell.md](shell/shell.md).
- Permissão de execução nos scripts (`chmod +x script.sh`) ou invocação explícita: `bash script.sh`.

## Estrutura do repositório

| Caminho | Conteúdo |
|---------|------------|
| `shell/` | Conceito de shell, histórico (`sh`, Bash, Zsh), empilhamento e ambientes Windows/macOS. |
| `arrays/` | Arrays em Bash. |
| `atividades/01.calculadora/` | Implementação de referência da calculadora em menu. |
| `atividades/02.integradora/` | Script que gera linhas de log a partir de texto; base para exercícios de validação e logs. |
| `calculos/` | Operações e aritmética no shell. |
| `case/` | Estrutura `case` e exemplo em `script.sh`. |
| `condicional/` | `if`, `test`, operadores lógicos; exemplo em `teste_then.sh`. |
| `entrada_usuario/` | `read` e leitura interativa. |
| `fluxos/` | `IFS`, redirecionamento e arquivos de exemplo (`erro.log`). |
| `funcoes/` | Definição e uso de funções. |
| `loop/` | Loops `for` e `while`. |
| `pipe/` | Pipelines entre comandos; scripts de exemplo. |
| `tmux/` | Uso do multiplexer `tmux` no dia a dia. |
| `trap/` | Sinais e limpeza com `trap`. |

## Índice dos tópicos (notas)

Cada link aponta para um arquivo Markdown na pasta indicada.

1. [O que é um shell — conceito, histórico, compatibilidade](shell/shell.md)
2. [TMUX — sessões e janelas no terminal](tmux/tmux.md)
3. [Funções](funcoes/funcoes.md)
4. [Condicionais — `test`, `then`, operadores lógicos](condicional/condicional.md)
5. [Leitura de entrada do usuário](entrada_usuario/entrada.md)
6. [Cálculos numéricos](calculos/calculos.md)
7. [Estrutura `case`](case/case.md)
8. [Loop `for`](loop/for.md)
9. [Loop `while`](loop/while.md)
10. [IFS — separador de campos interno](fluxos/IFS.md)
11. [`trap` — sinais e encerramento](trap/trap.md)
12. [Pipes entre comandos](pipe/pipe.md)
13. [Redirecionamento (`stdin` / `stdout` / `stderr`)](fluxos/redirecionamento.md)
14. [Arrays](arrays/arrays.md)

Sugerimos seguir a ordem acima se estiver começando; depois pode alternar entre `pipe/`, `fluxos/` e `trap/` conforme seus scripts ficarem mais complexos.

## Atividades práticas

### 1. Calculadora interativa

Implemente (ou compare com a solução em [`atividades/01.calculadora/calculadora.sh`](atividades/01.calculadora/calculadora.sh)) uma calculadora que:

- recebe dois operandos e um operador (soma, subtração, multiplicação e divisão);
- apresenta o resultado correto;
- opcionalmente expõe um **menu** para escolher a operação ou sair.

Para executar a referência:

```bash
bash atividades/01.calculadora/calculadora.sh
```

*(O script pode tentar instalar `bc` via `apt` se não estiver disponível — ajuste conforme sua distribuição.)*

### 2. Geração e tratamento de logs

1. Leia e compreenda [`atividades/02.integradora/script.sh`](atividades/02.integradora/script.sh) (entrada `lorem_ipsum.txt`, saída em `log_output.txt`).
2. Melhore o script conforme os requisitos abaixo.

| Requisito | Detalhe |
|-----------|---------|
| **Arquivo de log de saída** | Se o arquivo de log não existir ou não for gravável, escreva uma mensagem de erro em **stderr** em vez de falhar em silêncio. |
| **Arquivo de entrada** | Se o arquivo de entrada não existir, mensagem de erro em **stderr** e registro do problema em `input_error_log.txt`. |
| **Log só de erros** | Linhas cuja tag seja erro (por exemplo contendo `ERROR` / `ERRO`) devem ser duplicadas ou filtradas para `error_log.txt`, conforme a convenção que definir no enunciado do seu script. |
| **Cenários extra** | Adicione casos mais realistas (rotação de arquivos, múltiplas fontes, filtros com `grep`/`awk`, etc.) usando o que aprendeu nas pastas de notas. |

Execução típica (a partir da pasta da atividade):

```bash
cd atividades/02.integradora
bash script.sh
```

## Convenções rápidas

- Preferir `#!/usr/bin/env bash` no shebang para portabilidade entre sistemas onde o Bash não está em `/bin/bash`.
- Citar variáveis e parâmetros: `"$var"` e `"$1"` para evitar quebras com espaços ou globbing acidental.
- Testar scripts com `bash -n script.sh` (sintaxe) antes de executar em produção.

## Licença e uso

Utilize e adapte o material para estudo pessoal ou formação. Se forkar o repositório, mantenha créditos coerentes com a licença do projeto (se existir arquivo `LICENSE` na raiz, siga-o).
