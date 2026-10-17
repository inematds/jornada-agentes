#!/usr/bin/env bash
# fila-caseira.sh — fila de tarefas mínima, para entender a ideia antes do inemaccbot.
# Cada arquivo em <pasta>/entrada/ é um pedido; a resposta vai para <pasta>/feito/,
# a tarefa que der erro vai para <pasta>/falhou/. Rodar de novo só pega o que sobrou.
#
# Uso: ./fila-caseira.sh <pasta> [motor]
#   motor: claude (padrão) ou codex — os dois pela sua assinatura.
set -u
PASTA="${1:?uso: fila-caseira.sh <pasta> [claude|codex]}"
MOTOR="${2:-claude}"
mkdir -p "$PASTA/entrada" "$PASTA/rodando" "$PASTA/feito" "$PASTA/falhou"

# retomada: o que ficou em "rodando" (queda, Ctrl+C) volta para a entrada
for f in "$PASTA"/rodando/*.md; do [ -e "$f" ] && mv "$f" "$PASTA/entrada/"; done

for f in "$PASTA"/entrada/*.md; do
  [ -e "$f" ] || { echo "fila vazia"; break; }
  nome=$(basename "$f")
  mv "$f" "$PASTA/rodando/$nome"                      # pega a tarefa (só uma por vez)
  echo "→ $nome"
  case "$MOTOR" in
    claude) saida=$(claude -p "$(cat "$PASTA/rodando/$nome")" < /dev/null 2>&1); rc=$? ;;
    codex)  saida=$(codex exec --skip-git-repo-check - < "$PASTA/rodando/$nome" 2>&1); rc=$? ;;
    *) echo "motor desconhecido: $MOTOR"; exit 2 ;;
  esac
  if [ $rc -eq 0 ] && [ -n "$saida" ]; then
    { cat "$PASTA/rodando/$nome"; printf '\n---\n\n%s\n' "$saida"; } > "$PASTA/feito/$nome"
    rm "$PASTA/rodando/$nome"; echo "  feito"
  else
    { cat "$PASTA/rodando/$nome"; printf '\n---\nERRO (rc=%s)\n%s\n' "$rc" "$saida"; } > "$PASTA/falhou/$nome"
    rm "$PASTA/rodando/$nome"; echo "  falhou (rc=$rc)"
  fi
done
echo "entrada: $(ls "$PASTA"/entrada | wc -l) · feito: $(ls "$PASTA"/feito | wc -l) · falhou: $(ls "$PASTA"/falhou | wc -l)"
