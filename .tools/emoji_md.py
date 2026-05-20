#!/usr/bin/env python3
"""Adiciona emojis a títulos e listas em arquivos Markdown (fora de blocos de código)."""
import re
import sys
from pathlib import Path

# Já tem emoji no início do título?
HAS_EMOJI = re.compile(
    r"^[\s#]*(?:[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U00002300-\U000023FF"
    r"\U00002194-\U00002199\U00002714\U00002716\U00002705\U0000274C\U00002753"
    r"\U0001F680-\U0001F6FF\U000026A0-\U000026FF])"
)

KEYWORD_EMOJI = [
    (r"shell|terminal|tty|pty", "🖥️"),
    (r"pipe|pipeline|tubula", "🔗"),
    (r"entrada|usuário|read|prompt", "⌨️"),
    (r"condicional|if\b|then|test", "🔀"),
    (r"cálculo|calculo|expr|bc\b|aritm", "🔢"),
    (r"case\b|menu", "📋"),
    (r"loop|for\b|while", "🔁"),
    (r"função|funcoes|function", "📦"),
    (r"redirecion|stdin|stdout|stderr|heredoc", "↔️"),
    (r"\bifs\b|campo", "✂️"),
    (r"array", "📚"),
    (r"tmux|sessão|painel", "🪟"),
    (r"trap|sinal|sig", "⚡"),
    (r"log|integradora|erro", "📜"),
    (r"calculadora", "🧮"),
    (r"prática|pratica|exerc", "🛠️"),
    (r"pré-requisito|prerequisito", "✅"),
    (r"próximo|proximo", "➡️"),
    (r"ordem|trilha|nível|nivel", "🗺️"),
    (r"objetivo|estrutura", "🎯"),
    (r"histórico|historico|bourne|bash|zsh", "📖"),
    (r"compatib|windows|macos|git bash|wsl", "🌐"),
    (r"segurança|seguranca", "🔒"),
    (r"exemplo|prático|pratico", "💡"),
    (r"vantagem|benef", "✨"),
    (r"considera|boas práticas|cuidado|erro comum", "⚠️"),
    (r"resumo", "📝"),
    (r"instala", "📥"),
    (r"execut", "▶️"),
    (r"arquivo|requisito|melhoria", "📁"),
    (r"convenção|licença|licenca", "📌"),
    (r"caminho antigo|bookmark|migr", "🔄"),
    (r"extensão|planejado|futuro", "🚀"),
    (r"empilh", "📚"),
    (r"ssh|remoto", "🔐"),
    (r"http|curl", "🌐"),
    (r"config|ambiente|variável", "⚙️"),
    (r"modular|eficiên|flexib|performance", "⚡"),
    (r"ver mais|voltar", "🔙"),
    (r"visão geral", "👀"),
    (r"operador|compara", "⚖️"),
    (r"demonstra", "🎬"),
    (r"personaliza", "🎨"),
    (r"tipos de", "🏷️"),
    (r"declar|iter", "🔧"),
    (r"monitor", "👁️"),
    (r"filtr", "🔍"),
]

DEFAULT_BY_LEVEL = {1: "📘", 2: "📌", 3: "🔹", 4: "▫️", 5: "•", 6: "·"}


def pick_emoji(text: str) -> str:
    t = text.lower()
    for pattern, em in KEYWORD_EMOJI:
        if re.search(pattern, t, re.I):
            return em
    return "📌"


def heading_level(line: str) -> int:
    m = re.match(r"^(#{1,6})\s", line)
    return len(m.group(1)) if m else 0


def enrich_heading(line: str) -> str:
    lvl = heading_level(line)
    if not lvl or HAS_EMOJI.search(line):
        return line
    hashes = "#" * lvl
    title = line[lvl:].strip()
    em = pick_emoji(title) if lvl <= 2 else (DEFAULT_BY_LEVEL.get(lvl, "▫️"))
    if lvl == 1 and title.lower().startswith("o que é"):
        em = "🐚"
    return f"{hashes} {em} {title}"


def enrich_bullet(line: str) -> str:
    m = re.match(r"^(\s*[-*]\s+)(.+)$", line)
    if not m or HAS_EMOJI.search(m.group(2)):
        return line
    return f"{m.group(1)}{pick_emoji(m.group(2))} {m.group(2)}"


def enrich_numbered(line: str) -> str:
    m = re.match(r"^(\s*\d+\.\s+)(.+)$", line)
    if not m or HAS_EMOJI.search(m.group(2)):
        return line
    return f"{m.group(1)}{pick_emoji(m.group(2))} {m.group(2)}"


def enrich_table_row(line: str) -> str:
    if not line.strip().startswith("|") or line.strip().startswith("|--"):
        return line
    parts = line.split("|")
    if len(parts) < 3:
        return line
    cell = parts[1].strip()
    if not cell or HAS_EMOJI.search(cell) or cell.startswith("["):
        return line
    parts[1] = f" {pick_emoji(cell)} {cell} "
    return "|".join(parts)


def process(content: str) -> str:
    lines = content.splitlines(keepends=True)
    out = []
    in_code = False
    for line in lines:
        bare = line.rstrip("\n")
        if bare.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        lvl = heading_level(bare)
        if lvl:
            new = enrich_heading(bare) + ("\n" if line.endswith("\n") else "")
            out.append(new)
        elif re.match(r"^\s*[-*]\s+", bare):
            out.append(enrich_bullet(bare) + ("\n" if line.endswith("\n") else ""))
        elif re.match(r"^\s*\d+\.\s+", bare):
            out.append(enrich_numbered(bare) + ("\n" if line.endswith("\n") else ""))
        elif bare.strip().startswith("|"):
            out.append(enrich_table_row(bare) + ("\n" if line.endswith("\n") else ""))
        else:
            out.append(line)
    return "".join(out)


def main():
    root = Path(__file__).resolve().parents[1]
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts or ".tools" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new = process(text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            print(path.relative_to(root))


if __name__ == "__main__":
    main()
