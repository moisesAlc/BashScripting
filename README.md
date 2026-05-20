# 🖥️ Shell Scripting com Bash

Material de estudo e prática em **Shell Scripting** (Bash), organizado em trilhas por nível.

## 🗺️ Trilhas

| 🗺️ Nível | Descrição |
|-------|-----------|
| [**Iniciante**](niveis/iniciante/README.md) | Shell, entrada do usuário, pipes |
| [**Intermediário**](niveis/intermediario/README.md) | Condicionais, loops, funções, fluxos, arrays, calculadora |
| [**Avançado**](niveis/avancado/README.md) | shell (TTY/PTY), trap, integradora de logs, robustez (em expansão) |

📚 Visão geral: [niveis/README.md](niveis/README.md).

🚀 Comece por [O que é um shell?](niveis/iniciante/shell/shell.md).

## 🎯 Objetivos

- 📖 Dominar sintaxe e idiomas comuns do Bash para scripts reutilizáveis.
- 🔁 Entender **condicionais**, **loops**, **funções**, **arrays** e manipulação de texto.
- 🔗 Usar **pipes**, **redirecionamento** e variáveis como `IFS` de forma consciente.
- ⌨️ Trabalhar com **entrada do usuário**, **cálculos** e ferramentas auxiliares (por exemplo `tmux`).

## ✅ Pré-requisitos

- 📚 Linux ou ambiente compatível com **Bash** (versão 4+ recomendada para arrays).
- 🖥️ No Windows ou macOS: [shell iniciante](niveis/iniciante/shell/shell.md) (visão geral) e [shell avançado](niveis/avancado/shell/shell.md) (Git Bash, WSL, macOS).

## 🎯 Estrutura

| 📌 Caminho | Conteúdo |
|---------|------------|
| [`niveis/iniciante/`](niveis/iniciante/README.md) | `shell`, `entrada_usuario`, `pipe` |
| [`niveis/intermediario/`](niveis/intermediario/README.md) | Tópicos de sintaxe e estrutura + `pratica/calculadora/` |
| [`niveis/avancado/`](niveis/avancado/README.md) | `shell`, `trap` + `pratica/integradora/` |

📂 Todo o material fica em **`niveis/`**. 🔄 Links antigos da raiz: [CAMINHOS-ANTIGOS.md](CAMINHOS-ANTIGOS.md).

## 💡 Projetos práticos

**🧮 Calculadora** (intermediário):

```bash
bash niveis/intermediario/pratica/calculadora/calculadora.sh
```

**📜 Integradora de logs** (avançado) — [enunciado](niveis/avancado/pratica/integradora/README.md):

```bash
cd niveis/avancado/pratica/integradora
bash script.sh
```

## 📌 Convenções rápidas

- 📖 Preferir `#!/usr/bin/env bash` no shebang.
- 📌 Citar variáveis: `"$var"` e `"$1"`.
- 🔀 Testar sintaxe: `bash -n script.sh`.

## 📌 Licença e uso

Material para estudo e formação. Se existir `LICENSE` na raiz, siga-o ao forkar.
