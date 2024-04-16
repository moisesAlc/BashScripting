#!/bin/bash

echo "Escolha uma opção:"
echo "1 - Listar arquivos"
echo "2 - Mostrar data atual"
echo "q - Sair"
read opcao

case "$opcao" in
  1)
    ls -l
    ;;
  2)
    date
    ;;
  q)
    echo "Saindo..."
    exit 0
    ;;
  *)
    echo "Opção inválida!"
    ;;
esac
