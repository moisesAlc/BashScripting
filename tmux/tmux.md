# Manual Básico do Tmux

O `tmux` é um multiplexador de terminal poderoso para sistemas Unix-like. Ele permite que você controle vários terminais a partir de uma única tela, podendo alternar entre eles, dividir a tela em painéis e até desconectar e reconectar a sessões sem perder o estado. Este manual básico cobrirá como instalar, usar e aproveitar alguns dos recursos essenciais do `tmux`.

## Instalação

O `tmux` pode ser instalado na maioria das distribuições Linux usando o gerenciador de pacotes da distribuição.

## Iniciando com o Tmux
Para começar uma sessão tmux, simplesmente abra um terminal e digite:

  ```bash
  tmux
  ```

Você será colocado em uma nova sessão tmux com um único painel. A linha de status na parte inferior da tela mostra informações sobre a sessão, incluindo o número do painel e o nome da sessão.

Comandos Básicos
Criar uma nova janela:

  ```bash
  Ctrl-b c
  ```

Este comando cria uma nova janela dentro da sessão tmux.

Alternar entre janelas:

  ```bash
  Ctrl-b n
  ```

Este comando move você para a próxima janela na sessão.

Dividir o painel horizontalmente:

  ```bash
  Ctrl-b "
  ```

Isso divide o painel atual horizontalmente em dois.

Dividir o painel verticalmente:

  ```bash
  Ctrl-b %
  ```

Isso divide o painel atual verticalmente em dois.

Navegar entre painéis:

  ```bash
  Ctrl-b seta_direcional
  ```

Use as teclas de seta para mover entre os painéis divididos.

Fechar um painel:

  ```bash
  exit
  ```

Digite exit no painel que você deseja fechar.

Desanexar de uma sessão:

  ```bash
  Ctrl-b d
  ```

Isso desanexa você da sessão tmux atual, permitindo que você deixe a sessão rodando em background.

Listar sessões existentes:

  ```bash
  tmux ls
  ```

Mostra todas as suas sessões tmux ativas.

Reanexar a uma sessão:

  ```bash
  tmux attach -t session_name
  ```

Substitua session_name pelo nome da sessão a qual você deseja se reconectar.

## Personalização

O tmux é altamente personalizável. As configurações podem ser alteradas criando e modificando um arquivo chamado .tmux.conf no seu diretório home. Aqui estão algumas configurações básicas:

```bash
# Define novos atalhos de teclado para dividir painéis
bind | split-window -h
bind - split-window -v

# Melhorar a resposta do tmux a comandos
set -sg escape-time 1

# Renomear a sessão mais facilmente
bind r command-prompt "rename-session %%"
```

[Voltar para Visão Geral](../visao_geral.md)