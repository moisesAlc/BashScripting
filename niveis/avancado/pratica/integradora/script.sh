#!/bin/bash

# Defina o caminho para o arquivo de texto Lorem Ipsum
arquivo_entrada="lorem_ipsum.txt"

# Caminho para o arquivo de log onde os parágrafos serão gravados
arquivo_log="log_output.txt"

# Cria um array com tags que serão inseridas de forma aleatória
nomes=("INFO" "WARNING" "ERROR")

# Tempo de sleep
tempo_sleep=1

# Verifica se o arquivo de entrada existe
if [ ! -f "$arquivo_entrada" ]; then
    echo "Arquivo de texto não encontrado."
    exit 1
fi

# Lê o arquivo linha por linha
while IFS= read -r line
do
    # Verifica se a linha é um parágrafo (não vazio)
    if [[ ! -z "$line" ]]; then
        # Pega o timestamp atual
        timestamp=$(date +"%Y-%m-%d %H:%M:%S")

        # Gera aleatoriamente um número aleatório dentro dos limites de índices do array  nomes
        indice_aleatorio=$(($RANDOM % ${#nomes[@]}))

        # Pega o índice aleatório e joga o valor do array em tag_log
        tag_log=${nomes[$indice_aleatorio]}

        # Escreve o timestamp e o parágrafo no arquivo de log
        echo "$timestamp - $tag_log - $line" >> "$arquivo_log"

        # Espera x segundos antes de processar o próximo parágrafo
        sleep $tempo_sleep
    fi
done < "$arquivo_entrada"

echo "Processamento concluído."
