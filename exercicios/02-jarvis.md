# Sequência 2 — Crie o seu Jarvis (INTELECTO)

**Objetivo:** ter um assistente pessoal seu, que fala pelo Telegram, lembra das conversas e tem a personalidade que você definir.
**Base:** INTELECTO (https://inematds.github.io/intelecto/), curso (https://inematds.github.io/intelecto-curso/) e área https://eventos.inema.pro/jarvis/
**Pré-requisito:** a Sequência 1 feita (terminal, pastas, `.env`).

---

## E1. Desenhe o seu Jarvis antes de instalar (15 min)

Num arquivo `meu-jarvis.md`, responda:

- Nome do assistente e como ele fala (formal, direto, bem-humorado).
- Três coisas que ele **deve** fazer por você toda semana.
- Três coisas que ele **nunca** deve fazer.
- O que ele precisa lembrar de você (profissão, rotina, preferências).

**Pronto quando:** o arquivo cabe numa tela e outra pessoa entenderia quem é o seu assistente.

## E2. O bot no Telegram (10 min)

No Telegram, abra o `@BotFather`, mande `/newbot`, escolha nome e @usuário. Guarde o token **só** no `.env` (regra da Sequência 1).

**Pronto quando:** você tem o token e ele não aparece em nenhum arquivo além do `.env`.

## E3. Construir (30 min)

O INTELECTO não tem instalador: você entrega um briefing ao agente e ele constrói o assistente, com testes. Primeiro veja o caminho funcionando no exemplo do repositório (9 testes, sem chave e sem internet):

```bash
git clone https://github.com/inematds/intelecto.git
cd intelecto/exemplo-jarvis
python3 -m unittest discover -s . -p 'test_*.py' -v
python3 smoke.py
```

1. Abra a página de comparação do INTELECTO (https://inematds.github.io/intelecto/), marque os ingredientes e exporte o briefing.
2. Peça ao Claude Code ou ao Codex: "Construa o meu assistente a partir deste briefing e do doc/intelecto.md, com testes."
3. Use o seu `meu-jarvis.md` para o nome, o jeito de falar e a personalidade. O token do Telegram fica só no `.env`.

**Pronto quando:** você manda "oi" no Telegram e ele responde com o nome e o jeito que você definiu.

## E4. Teste de memória (2 dias)

1. Dia 1: conte a ele três fatos seus (ex.: "toda segunda eu fecho o relatório de vendas").
2. Dia 2, numa conversa nova: pergunte "o que eu faço toda segunda?".

**Pronto quando:** ele lembra sem você repetir. Se não lembrar, veja no curso como a memória é guardada e ajuste.

## E5. Nuvem ou local (20 min)

Rode a mesma pergunta duas vezes: uma com um modelo na nuvem (OpenRouter) e outra com um modelo local (Ollama), se o seu computador aguentar. Anote numa tabela: tempo de resposta, qualidade e custo.

**Pronto quando:** você sabe dizer qual modelo usar para quê, com os seus números.

## E6. Uma rotina de verdade (20 min)

Escolha uma das três tarefas do E1 e transforme em pedido fixo (ex.: "toda manhã, quando eu mandar 'dia', liste as minhas três prioridades a partir do que eu te contei ontem"). Use por uma semana.

**Pronto quando:** você usou 5 dias seguidos e anotou o que melhorar.

---

### Desafio extra
Escreva no `meu-jarvis.md` a lista de tarefas que você gostaria de mandar e ir dormir. Essa lista é a entrada da Sequência 3.
