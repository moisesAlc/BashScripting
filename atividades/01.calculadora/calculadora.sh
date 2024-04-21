#!/bin/bash

if ! command -v bc &> /dev/null; then
    sudo apt update
    sudo apt install -y bc
fi

adicao() {
    clear
    echo "---------ADIÇÃO---------"
    read -p "Digite o primeiro número: " num1
    read -p "Digite o segundo número: " num2
    resultado=$((num1 + num2))
    echo "Resultado da adição: $resultado"
    echo "------------------------"
    read -p "Pressione Enter para continuar..." press
}

subtracao() {
    clear
    echo "-------SUBTRAÇÃO--------"
    read -p "Digite o primeiro número: " num1
    read -p "Digite o segundo número: " num2
    resultado=$((num1 - num2))
    echo "Resultado da subtração: $resultado"
    echo "------------------------"
    read -p "Pressione Enter para continuar..." press
}

multiplicacao() {
    clear
    echo "-----MULTIPLICAÇÃO------"
    read -p "Digite o primeiro número: " num1
    read -p "Digite o segundo número: " num2
    resultado=$((num1 * num2))
    echo "Resultado da multiplicação: $resultado"
    echo "------------------------"
    read -p "Pressione Enter para continuar..." press
}

divisao() {
    clear
    echo "--------DIVISÃO---------"
    read -p "Digite o primeiro número: " num1
    read -p "Digite o segundo número: " num2
    if [ $num2 -eq 0 ]; then
        echo "Erro: divisão por zero!"
    else
        resultado=$(echo "scale=2; $num1 / $num2" | bc)
        echo "Resultado da divisão: $resultado"
    fi
    echo "------------------------"
    read -p "Pressione Enter para continuar..." press
}

menu() {
    clear
    echo "########################"
    echo "###### CALCULADORA #####"
    echo "########################"
    echo "---------MENU-----------"
    echo "| 1- ADIÇÃO            |"
    echo "| 2- SUBTRAÇÃO         |"
    echo "| 3- MULTIPLICAÇÃO     |"
    echo "| 4- DIVISÃO           |"
    echo "| 5- SAIR              |"
    echo "------------------------"
}

opcao=0
while [ $opcao != 5 ]; do
    menu
    read -p " ESCOLHA UMA OPÇÃO : " opcao
    
    case "$opcao" in
        1) adicao ;;
        2) subtracao ;;
        3) multiplicacao ;;
        4) divisao ;;
        5) 
           clear
           echo "------------------------"
           echo " SAINDO DO PROGRAMA.... "
           echo "------------------------"
           sleep 2
           ;;
        *) 
           clear
           echo "------------------------"
           echo "|  OPÇÃO INVÁLIDA!     |"
           echo "|  TENTE NOVAMENTE!    |"
           echo "------------------------"
           sleep 2
           ;;
    esac
done
