# Trap

No contexto do shell scripting no Bash, o comando trap é uma ferramenta poderosa que permite a programadores definir ações ou manipuladores que serão executados em resposta a sinais ou outros eventos específicos. Isso é extremamente útil para lidar com interrupções inesperadas, como terminações de programas, sinais de interrupção do usuário (como ```Ctrl+C```), ou para executar a limpeza do script quando ele termina naturalmente ou por erro.

## Funcionalidade Básica do Trap
O comando trap intercepta sinais enviados para o script e executa um comando ou uma série de comandos em resposta. Sinais são notificações enviadas a processos para indicar que um evento específico ocorreu. Alguns dos sinais mais comuns incluem:

```SIGINT```: O sinal de interrupção, geralmente enviado ao programa quando você pressiona Ctrl+C.

```SIGTERM```: Sinal de terminação padrão, usado para solicitar o encerramento do programa.

```EXIT```: Não é exatamente um sinal, mas pode ser capturado por trap para executar comandos quando o script termina.

```SIGHUP```: Sinal enviado para terminar processos após o fechamento de um terminal.


## Sintaxe do Trap
A sintaxe básica do comando trap é:

```bash
trap 'comandos' SINAL
```

```'comandos'```: Comandos a serem executados quando o sinal especificado é recebido. Os comandos devem ser fornecidos como uma string.

```SINAL```: O nome do sinal que, quando recebido pelo script, acionará a execução dos comandos.

## Exemplos de Uso do Trap

### Capturando o Ctrl+C
Para capturar um ```Ctrl+C (SIGINT)``` e executar uma função de limpeza:

```bash
trap 'echo "Ctrl+C foi pressionado. Saindo..."; exit' SIGINT
```

## Limpeza ao Sair
Para executar comandos de limpeza independentemente de como o script termina (normalmente ou por um sinal):

```bash
trap 'rm -f /tmp/arquivo_temporario' EXIT
```

Neste exemplo, um arquivo temporário é removido quando o script é finalizado.

## Ignorando um Sinal
Você também pode configurar um script para ignorar completamente sinais, o que pode ser útil para garantir que um script não seja interrompido prematuramente:

```bash
trap '' SIGINT
```

## Boas Práticas
### Use Trap para Limpeza: 
trap é ideal para limpar arquivos temporários, restaurar configurações ou qualquer outra tarefa de limpeza necessária para deixar tudo em um estado consistente após o término do script.
### Evite Comandos Complexos no Trap: 
Embora você possa tecnicamente colocar qualquer comando no trap, é melhor manter os comandos simples e não depender de funções ou comandos externos que possam falhar.
### Teste os Traps com Diferentes Sinais:
Diferentes sistemas e terminais podem comportar-se de maneira ligeiramente diferente, então é uma boa prática testar como os sinais são manipulados em seu ambiente específico.

[Voltar para Visão Geral](../README.md)