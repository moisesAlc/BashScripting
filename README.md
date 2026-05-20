# Shell Scripting com Bash

Material de estudo e prática em **Shell Scripting** (Bash): notas conceituais, exemplos curtos e atividades guiadas. Organizado em trilhas por nível de dificuldade.

## Trilhas

| Nível | Descrição |
|-------|-----------|
| [**Iniciante**](niveis/iniciante/README.md) | Shell, entrada do usuário, pipes |
| [**Intermediário**](niveis/intermediario/README.md) | Condicionais, loops, funções, fluxos, arrays |
| [**Avançado**](niveis/avancado/README.md) | trap, logs, robustez (em expansão) |

Visão geral: [niveis/README.md](niveis/README.md).

Comece por [O que é um shell?](niveis/iniciante/shell/shell.md).

## Objetivos

- Dominar sintaxe e idiomas comuns do Bash para scripts reutilizáveis.
- Entender **condicionais**, **loops**, **funções**, **arrays** e manipulação de texto.
- Usar **pipes**, **redirecionamento** e variáveis como `IFS` de forma consciente.
- Trabalhar com **entrada do usuário**, **cálculos** e ferramentas auxiliares (por exemplo `tmux` para sessões persistentes no terminal).

## Pré-requisitos

- Linux ou ambiente compatível com **Bash** (versão 4+ recomendada para alguns recursos de arrays). No Windows ou macOS, veja [shell/shell.md](niveis/iniciante/shell/shell.md).
- Permissão de execução nos scripts (`chmod +x script.sh`) ou invocação explícita: `bash script.sh`.

## Estrutura do repositório

| Caminho | Conteúdo |
|---------|------------|
| `niveis/` | Trilhas iniciante, intermediário e avançado |
| `niveis/iniciante/` | `shell`, `entrada_usuario`, `pipe`, `pratica/` |
| `condicional/`, `calculos/`, `case/`, `loop/` | Intermediário *(na raiz até migração)* |
| `funcoes/`, `fluxos/`, `arrays/`, `tmux/` | Intermediário *(na raiz)* |
| `trap/` | Avançado *(na raiz)* |
| `atividades/` | Projetos de referência *(serão movidos para `niveis/*/pratica/`)* |

## Atividades práticas

### Calculadora (intermediário)

[`atividades/01.calculadora/calculadora.sh`](atividades/01.calculadora/calculadora.sh) — menu, operações e entrada do usuário.

```bash
bash atividades/01.calculadora/calculadora.sh
```

### Integradora de logs (avançado)

[`atividades/02.integradora/`](atividades/02.integradora/) — geração e melhoria de logs (stderr, arquivos de erro, filtros).

```bash
cd atividades/02.integradora
bash script.sh
```

Requisitos detalhados no enunciado em [niveis/avancado/README.md](niveis/avancado/README.md).

## Convenções rápidas

- Preferir `#!/usr/bin/env bash` no shebang para portabilidade entre sistemas onde o Bash não está em `/bin/bash`.
- Citar variáveis e parâmetros: `"$var"` e `"$1"` para evitar quebras com espaços ou globbing acidental.
- Testar scripts com `bash -n script.sh` (sintaxe) antes de executar em produção.

## Licença e uso

Utilize e adapte o material para estudo pessoal ou formação. Se forkar o repositório, mantenha créditos coerentes com a licença do projeto (se existir arquivo `LICENSE` na raiz, siga-o).
