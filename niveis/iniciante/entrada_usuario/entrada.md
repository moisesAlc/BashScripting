# ⌨️ Entrada do Usuário

No Bash, assim como em muitas outras linguagens de programação, é possível receber entrada do usuário durante a execução de um script ou interação com o shell. Isso permite que seus scripts sejam mais interativos e flexíveis, permitindo que os usuários forneçam dados ou façam escolhas durante a execução do programa. Vamos explorar como isso pode ser feito no Bash:

## ⌨️ Utilizando o Comando read
O comando read é usado para ler uma linha de entrada do usuário e atribuí-la a uma variável. Aqui está a sintaxe básica:

```bash
read -p "Prompt: " variavel
```

- 📌 `-p "Prompt: "`: exibe um prompt ao usuário; o texto entre aspas é o que aparece na tela.
- 📌 `variavel`: nome da variável que receberá a entrada.

## 💡 Exemplo de uso
```bash
#!/bin/bash

# Solicita ao usuário que insira seu nome
read -p "Por favor, digite seu nome: " nome

# Exibe uma mensagem de boas-vindas usando o nome fornecido pelo usuário
echo "Olá, $nome! Bem-vindo ao nosso script."
```

Neste exemplo, o script solicita ao usuário que insira seu nome e, em seguida, exibe uma mensagem de boas-vindas usando o nome fornecido.

## ⚙️ Opções adicionais do `read`

Além do `-p`, o comando `read` oferece:

- 🔤 **`-r`**: não interpreta escapes com `\`; lê a entrada literalmente.
- 🔒 **`-s`**: entrada silenciosa (senhas).
- 🔢 **`-n n`**: lê no máximo `n` caracteres antes de continuar.


## 🔒 Considerações de Segurança
Quando você solicita entrada do usuário, é importante considerar questões de segurança, especialmente quando se trata de informações sensíveis, como senhas. Evite exibir senhas na tela e use opções como -s para tornar a entrada silenciosa. Além disso, sempre valide e sanitize a entrada do usuário para evitar vulnerabilidades de segurança, como injeção de código.

🔙 [Voltar para trilha iniciante](../README.md)