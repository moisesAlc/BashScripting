# 🐚 O que é um shell?

Um **shell** é o programa que lê o que você digita, interpreta comandos, inicia outros programas e devolve a saída. Ele fica entre **você** e o **sistema operacional**: você não fala diretamente com o kernel; o shell traduz suas instruções em processos, arquivos, pipes e sinais.

## 🖥️ Terminal vs shell

São camadas diferentes. No dia a dia você abre “o terminal” e já aparece um prompt — mas quem **executa** `ls` ou um script `.sh` é o **shell**, não a janela.

| | **Terminal (emulador)** | **Shell** |
|---|-------------------------|-----------|
| 📌 **O que é** | Aplicação que mostra texto e envia o que você digita | Programa que interpreta comandos e scripts |
| 💡 **Exemplos** | GNOME Terminal, Windows Terminal, iTerm2 | Bash, Zsh, `sh`, Fish, PowerShell |
| 📌 **Responsabilidade** | Fonte, abas, scroll, copiar/colar | Prompt, `cd`, pipes, loops, histórico |

Analogia: o **terminal** é a janela; o **shell** é o interpretador.

```text
Você → [ Terminal ] → [ Shell: bash/zsh/... ] → [ Comandos ] → SO
```

Entre o emulador e o shell existe um **canal de texto** (TTY/PTY). Detalhes em [Shell: TTY, PTY e sessões](../../avancado/shell/shell.md).

### 🔹 Exemplos rápidos

**Mesmo shell, terminais diferentes** — duas janelas = duas sessões; `cd` em uma não afeta a outra.

**Mesmo terminal, shells diferentes** — o emulador continua; só o interpretador muda:

```bash
echo $SHELL    # shell de login (ex.: zsh)
bash           # passa a interpretar com Bash
exit           # volta ao shell anterior
```

**O terminal não entende Bash** — ele repassa texto. Colar um `for` do Bash no PowerShell falha porque o interpretador é outro.

```bash
for i in 1 2 3; do echo $i; done   # Bash/Zsh (estilo Bourne)
```

### 🔹 Erros comuns

- 🖥️ **“Meu terminal é Bash”** — em geral o terminal é *GNOME Terminal* / *Windows Terminal*; o shell padrão é que pode ser Bash.
- 🖥️ **Fechar o terminal mata o shell** — a sessão encerra e o shell recebe SIGHUP; jobs em background podem morrer junto.
- 🖥️ **Trocar tema no terminal** — não afeta scripts; trocar de `bash` para `zsh` pode mudar sintaxe e autocompletar.

## 🐚 Shells comuns: diferenças e armadilhas

| Shell | Família / ideia | Onde aparece | Cuidados |
|-------|-----------------|--------------|----------|
| **`sh`** | Bourne / **POSIX** — sintaxe mínima e portável | `/bin/sh` em scripts de sistema (`#!/bin/sh`) | Em muitos Linux, `sh` é **dash** ou Bash em modo POSIX — **não** assuma que `sh` = Bash |
| **Bash** | Bourne + extensões (arrays, `[[ ]]`, `$(())`) | Servidores Linux, Git Bash, WSL, CI, Docker | Padrão didático deste repositório; scripts com `#!/bin/bash` precisam de Bash instalado |
| **Zsh** | Bourne-like + autocompletar e globbing ricos | **macOS** (padrão desde Catalina), Oh My Zsh | Ótimo no teclado; rode estudos com `bash script.sh`, não só com o shell padrão do Mac |
| **Fish** | Shell **interativo** moderno; **não** POSIX | Instalação opcional no desktop | Sintaxe diferente (`if`, variáveis, loops); **scripts Fish não rodam em Bash** e vice-versa |
| **PowerShell** | Outra linguagem (cmdlets, objetos .NET) | Windows nativo, `pwsh` cross-platform | Não substitui Bash para material POSIX/`grep`/`awk` deste repo |

### 🔹 Problemas que costumam aparecer

1. **Shebang errado** — `#!/bin/sh` exige POSIX; `#!/bin/bash` permite recursos do Bash. Misturar sem testar quebra em CI ou em `/bin/sh` = dash.
2. **Rodar com o shell “da vez”** — `./script.sh` usa o interpretador do shebang; `sh script.sh` força `sh`. Um `.sh` escrito para Bash deve ser `bash script.sh` se o shebang estiver ausente ou errado.
3. **macOS: Bash antigo** — o Bash do sistema pode ser 3.x; para Bash 5+, use Homebrew e `#!/usr/bin/env bash` apontando para o binário instalado.
4. **Fish como login shell** — scripts `.sh` do curso não executam no Fish; abra `bash` ou altere o comando de execução.
5. **Copiar sintaxe entre shells** — loops, testes e atribuição do Fish ou PowerShell não funcionam no Bash sem reescrever.
6. **Empilhar shells sem perceber** — `zsh` → `bash` → script: variáveis e `cd` do nível interno não voltam ao pai ao dar `exit` (comportamento esperado, mas confunde no início). Ver [empilhamento e TTY](../../avancado/shell/shell.md).

### 🔹 Por que este repositório usa Bash?

**Bash** está presente em quase todo Linux, pipelines de CI, imagens Docker e documentação de servidores. Scripts só-POSIX rodam em `sh` e muitas vezes no Zsh; scripts com `[[`, arrays associativos etc. exigem Bash explícito.

## 📝 Resumo

1. 🖥️ **Terminal** = janela; **shell** = interpretador.
2. 📖 **`sh`** = portabilidade POSIX; **Bash** = estudo e servidores; **Zsh** = interativo (Mac); **Fish** = UX, não POSIX; **PowerShell** = ecossistema Microsoft.
3. 🔀 Teste com o interpretador do shebang; não assuma que o shell padrão do usuário é Bash.
4. ➡️ Aprofundamento: [TTY/PTY, empilhamento, Windows e macOS](../../avancado/shell/shell.md).

## ➡️ Próximo passo

[Entrada do usuário](../entrada_usuario/entrada.md) — `read` e prompts.
