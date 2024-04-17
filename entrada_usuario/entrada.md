# Entrada do Usuário

No Bash, assim como em muitas outras linguagens de programação, é possível receber entrada do usuário durante a execução de um script ou interação com o shell. Isso permite que seus scripts sejam mais interativos e flexíveis, permitindo que os usuários forneçam dados ou façam escolhas durante a execução do programa. Vamos explorar como isso pode ser feito no Bash:

## Utilizando o Comando read
O comando read é usado para ler uma linha de entrada do usuário e atribuí-la a uma variável. Aqui está a sintaxe básica:

```bash
read -p "Prompt: " variavel
```

-p "Prompt: ": Isso exibe um prompt ao usuário, solicitando a entrada. O texto dentro das aspas é o prompt que será exibido.
variavel: É a variável que receberá a entrada do usuário.
Exemplo de Uso
```bash
#!/bin/bash

# Solicita ao usuário que insira seu nome
read -p "Por favor, digite seu nome: " nome

# Exibe uma mensagem de boas-vindas usando o nome fornecido pelo usuário
echo "Olá, $nome! Bem-vindo ao nosso script."
```

Neste exemplo, o script solicita ao usuário que insira seu nome e, em seguida, exibe uma mensagem de boas-vindas usando o nome fornecido.

Opções Adicionais do Comando read
Além do -p para exibir um prompt personalizado, o comando read possui várias opções que podem ser úteis:

-r: Impede que o read interprete sequências de escape de barra invertida no texto de entrada, garantindo que a entrada seja lida literalmente.

-s: Torna a entrada do usuário silenciosa, útil para senhas ou outras informações confidenciais.

-n n: Define o número mínimo de caracteres que o usuário deve digitar antes de read retornar.


## Considerações de Segurança
Quando você solicita entrada do usuário, é importante considerar questões de segurança, especialmente quando se trata de informações sensíveis, como senhas. Evite exibir senhas na tela e use opções como -s para tornar a entrada silenciosa. Além disso, sempre valide e sanitize a entrada do usuário para evitar vulnerabilidades de segurança, como injeção de código.

[Voltar para Visão Geral](../README.md)