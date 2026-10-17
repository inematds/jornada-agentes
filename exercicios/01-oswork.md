# Sequência 1 — Do chat para o terminal (OSWork)

**Objetivo:** sair do chat e colocar um agente para trabalhar dentro de uma pasta sua.
**Base:** curso OSWork (https://inematds.github.io/oswork-quick/) e área https://eventos.inema.pro/oswork/
**Você vai precisar de:** um computador, o terminal (cmd no Windows; Terminal no Mac e no Linux) e o Claude Code ou o Codex instalados.

Faça na ordem. Cada exercício tem um **pronto quando**: só passe para o próximo quando ele for verdade.

---

## E1. Sua primeira pasta pelo terminal (10 min)

1. Abra o terminal.
2. Crie a pasta `projetos` e, dentro dela, `meu-primeiro-agente`.
3. Entre nela e liste o conteúdo (vai estar vazia).
4. Abra a mesma pasta pelo Explorador de Arquivos (ou Finder) e compare.

**Pronto quando:** você chega até a pasta só pelo terminal, sem o mouse, e sabe dizer em que pasta está.

## E2. O manual do funcionário: AGENTS.md (15 min)

Crie, dentro da pasta, um arquivo `AGENTS.md` com:

```markdown
# Quem sou
<seu nome, sua profissão, para quem você trabalha>

# Regras deste projeto
- Escreva em português, frases curtas.
- Não apague arquivos sem perguntar.
- Antes de terminar, diga o que mudou e como eu confiro.

# O que tem aqui
- index.html: minha página
```

**Pronto quando:** o arquivo existe e tem pelo menos três regras suas, escritas por você.

## E3. A primeira tarefa (15 min)

Dentro da pasta, chame o agente (`claude` ou `codex`) e peça:

> Leia o AGENTS.md. Crie um index.html com uma página simples sobre mim, usando o que está lá.

Abra a página no navegador. Peça uma mudança (cor, texto, uma seção nova) e confira de novo.

**Pronto quando:** a página abre no navegador e você pediu pelo menos **uma correção** ao agente. Dar a tarefa, conferir e decidir: isso é gestão.

## E4. A rede de segurança: Git (20 min)

1. Na pasta: `git init`, depois `git add .` e `git commit -m "primeira versão"`.
2. Peça ao agente uma mudança grande na página.
3. Não gostou? Volte: `git restore index.html` (ou `git checkout -- index.html`).

**Pronto quando:** você desfez uma mudança do agente com um comando, sem pânico.

## E5. Segredo não entra no texto (10 min)

1. Crie um arquivo `.env` com uma linha falsa: `MINHA_CHAVE=teste123`.
2. Crie um `.gitignore` com a linha `.env`.
3. Rode `git status`: o `.env` **não** pode aparecer.
4. Acrescente ao AGENTS.md: "Nunca escreva chaves ou senhas em arquivo de texto; elas ficam no .env".

**Pronto quando:** `git status` não mostra o `.env`.

## E6. O agente lê os seus arquivos (20 min)

Coloque na pasta três arquivos de texto seus (anotações, uma ata, um e-mail longo). Peça:

> Leia os arquivos .txt desta pasta e escreva resumo.md com 5 decisões e 5 pendências, citando de qual arquivo veio cada uma.

Confira duas citações no arquivo original.

**Pronto quando:** você achou no original pelo menos duas das frases citadas. Se alguma não existir, anote no AGENTS.md a regra que faltou.

---

### Desafio extra
Repita o E3 com o **outro** agente (se usou o Claude Code, use o Codex). Os dois leem o mesmo AGENTS.md. O que mudou no resultado?
