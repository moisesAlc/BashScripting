# Atividade *Opcional* de Shell Scripting IT Talent 2024

## Utilização do TMUX: [tmux](tmux/tmux.md)

## Funções: [funções](funcoes/funcoes.md)

## Condicionais: [condicional, test,  operadores lógicos...](condicional/condicional.md)

## Leitura de Entrada do Usuário: [entrada do usuário](entrada_usuario/entrada.md)

## Cálculos numéricos: [cálculos](calculos/calculos.md)

## Estrutura Case: [case](case/case.md)

## Loop For: [loop](loop/for.md)

## Loop While: [loop](loop/while.md)

## IFS: [IFS](fluxos/IFS.md)

## Trap: [trap](trap/trap.md)

## Pipe: [pipe](pipe/pipe.md)

## Redirecionamento: [redirecionamento](fluxos/redirecionamento.md)

## Arrays: [arrays](arrays/arrays.md)

---

## 1ª Atividade Proposta: Calculadora

- Crie uma calculadora que recebe dois operandos e um operador (soma, subtração, multiplicação e divisão) e entrega o resultado do cálculo. Você pode mostrar um menu de opções onde o usuário poderá escolher qual função executar, inclusive sair do programa

## 2ª Atividade Proposta: Análise de Logs

Verifique o [script de geração de logs](atividades/02.integradora/script.sh) e entenda o seu funcionamento. Depois, verifique:

- **Checagem de Arquivo de Log**: O script assume que o arquivo de log pode ser escrito sem verificar se ele já existe ou se é acessível. Adicione uma mensagem de erro para ```stderr``` caso o arquivo não exista. 

- **Checagem de Arquivo de Entrada**: Adicione uma mensagem de erro para ```stderr``` caso o arquivo não exista e redirecione para o arquivo ```input_error_log.txt```

- **Crição de Log específico de Erros**: Crie um arquivo específico para logs de erros (contém a tag ERRO) em ```error_log.txt```

- **Crie cenários**: crie cenários mais complexos utilizando o que aprendeu.
