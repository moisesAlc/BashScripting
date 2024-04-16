# Redirecionamento
O redirecionamento no Bash é uma funcionalidade poderosa que permite controlar onde a entrada, saída e saída de erro de comandos são enviadas. Isso torna possível manipular dados de maneira flexível em scripts ou na linha de comando, permitindo que os usuários e scripts capturem saídas de comandos, enviem informações para arquivos ou dispositivos, e gerenciem erros de forma eficiente.

## Tipos de Redirecionamento
No Bash, existem três fluxos principais que são comumente redirecionados:

### Saída padrão (stdout): 
Este é o fluxo de dados que um programa envia para a tela normalmente, e é identificado pelo número 1. Usando o redirecionamento, você pode enviar essa saída para um arquivo ou outro comando.
### Entrada padrão (stdin): 
Este é o fluxo pelo qual um programa recebe dados, normalmente do teclado, e é identificado pelo número 0. Com o redirecionamento, você pode fazer com que um programa receba dados de um arquivo ou de outro comando.
### Erro padrão (stderr): 
Este é o fluxo usado para enviar mensagens de erro, identificado pelo número 2. Pode ser redirecionado para um arquivo para log de erros, ou ser combinado com a saída padrão.

## Comandos de Redirecionamento
### Redirecionamento de Saída
```>``` : Redireciona a saída padrão para um arquivo, sobrescrevendo o arquivo.

```bash
ls > arquivo.txt
```
---
```>>``` : Redireciona a saída padrão para um arquivo, anexando ao arquivo existente.

```bash;
echo "nova linha" >> arquivo.txt
```

### Redirecionamento de Entrada

```<``` : Direciona o conteúdo de um arquivo para a entrada padrão de um comando.

```bash
sort < desordenado.txt > ordenado.txt
```
---

```<<``` : O redirecionamento usando ```<<```, conhecido como ```here document``` ou simplesmente ```heredoc```, é uma funcionalidade no Bash e outros shells Unix-like que permite redirecionar a entrada a partir de um bloco de texto literal dentro de um script ou da linha de comando. Esse método é extremamente útil para executar um comando que requer múltiplas linhas de entrada ou para incorporar um bloco de texto diretamente em um script **sem a necessidade de criar arquivos externos**.

#### Como Funciona o Here Document
O redirecionamento ```<<``` é seguido por um ```delimitador``` que você escolhe. Após esse ```delimitador```, você pode inserir as ```linhas de texto``` que deseja passar para o comando. O ```here document``` termina quando uma linha contendo apenas o ```delimitador``` é encontrada.

##### Sintaxe Básica
```bash
comando <<DELIMITADOR
linha 1
linha 2
linha 3
DELIMITADOR
```

- ```comando```: o comando que receberá o texto como entrada.

- ```DELIMITADOR```: um identificador que você define para indicar o início e o fim do bloco de texto. Pode ser qualquer string que não apareça no texto.

##### Exemplo Prático
Suponhamos que você queira criar um arquivo de configuração interativamente usando ```cat```:

```bash
cat <<EOF >config.txt
# Configurações do Sistema
hostname=localhost
port=8080
EOF
```
Neste exemplo, ```EOF (End Of File)``` é um delimitador comum usado para here documents. Tudo entre a primeira EOF e a segunda EOF é considerado parte da entrada do comando cat, que então redireciona essa entrada para criar ou sobrescrever o arquivo config.txt.

##### Uso Avançado de Here Document
Passando Scripts para Shells ou Ferramentas
Here documents são especialmente úteis para passar scripts inteiros para interpretações de comandos, como Python, SQL ou um subshell:

```bash
bash <<'SCRIPT'
echo "Número de arquivos no diretório atual:"
ls | wc -l
SCRIPT
```

Neste caso, o script Bash é passado diretamente para um novo shell Bash que é invocado apenas para executar esse script.

##### Interagindo com Ferramentas Interativas
Você pode usar here documents para automatizar a entrada em programas que normalmente requerem interação do usuário, como ftp ou sql:

```bash
ftp -n <<EOF
open mirrordata.com
user anonymous senha
cd /files
get sample.zip
quit
EOF
```

Este exemplo automatiza um login FTP e a transferência de um arquivo usando um here document.

##### Considerações
- Segurança: Cuidado ao embutir senhas ou informações sensíveis em scripts que usam here documents, pois eles podem ser lidos por qualquer pessoa com acesso ao script.
- Dados Binários: Embora here documents sejam geralmente usados para texto, alguns usos especiais podem incluir dados binários, que precisam ser manipulados com cuidado para evitar problemas de codificação.


### Redirecionamento de Erro
```2>```: Redireciona a saída de erro para um arquivo.

```bash
comando 2> erro.log
```

Exemplo:

```bash
mkdir pasta
mkdir pasta 2> erro.log
```

No exemplo acima, caso você faça ```cat erro.log```, irá receber: ```mkdir: cannot create directory ‘a’: File exists```

---

```&>```: Redireciona tanto a saída padrão quanto a saída de erro para um arquivo.

```bash
comando &> tudo.log
```

#### Exemplos Práticos
##### Separando Erro de Saída Padrão
Para salvar erros em um arquivo separado enquanto mantém a saída regular na tela:

```bash
comando > saida.log 2> erro.log
```

Usando Pipe com Redirecionamento
Você pode combinar comandos com pipes e redirecionamentos para criar fluxos de trabalho complexos:

```bash
cat arquivo.log | grep "erro" > erros_encontrados.log
```

### Boas Práticas
#### Arquivos de Backup: Ao redirecionar saídas para arquivos, certifique-se de que não está sobrescrevendo arquivos importantes inadvertidamente. Considere fazer backups antes de executar scripts que modificam arquivos.