# 📜 Integradora de logs

Gera linhas de log a partir de `lorem_ipsum.txt` e grava em `log_output.txt`. Estude [`script.sh`](script.sh) antes de estender o script.

## ▶️ ▶️ Executar

```bash
cd niveis/avancado/pratica/integradora
bash script.sh
```

## 📁 Melhorias solicitadas

| 📁 Requisito | Detalhe |
|-----------|---------|
| 📜 **Arquivo de log de saída** | Se o log não existir ou não for gravável, mensagem em **stderr** (não falhar em silêncio). |
| ⌨️ **Arquivo de entrada** | Se a entrada não existir, erro em **stderr** e registro em `input_error_log.txt`. |
| 📜 **Log só de erros** | Linhas com tag de erro (ex.: `ERROR` / `ERRO`) em `error_log.txt`. |
| 📌 **Cenários extra** | Rotação de arquivos, múltiplas fontes, filtros com `grep`/`awk`, etc. |

## 📁 Arquivos

- ⌨️ `lorem_ipsum.txt` — entrada
- 📜 `log_output.txt` — saída gerada (exemplo)
- 📌 `script.sh` — script base
