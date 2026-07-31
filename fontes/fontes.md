# Fontes utilizadas neste Caderno Temático

Todas as fontes abaixo são abertas (site público + vídeos públicos do YouTube) e foram
convertidas para texto/markdown para upload no NotebookLM. Os arquivos `.txt` e `.md`
desta pasta são exatamente o material que deve ser carregado como fonte no caderno.

| # | Fonte | Tipo | Link original | Arquivo local |
|---|-------|------|----------------|----------------|
| 1 | Live de lançamento — Bootcamp "Criando seu primeiro agente de IA" (Michael Page × DIO) | Transcrição de vídeo | https://www.youtube.com/watch?v=pv0J-DHsu-g | `01-live-lancamento-bootcamp.txt` |
| 2 | Mentoria 1 — "O mercado de tech esfriou?" (Camilo, Michael Page) | Transcrição de vídeo | https://www.youtube.com/watch?v=O26VX_SRtdk | `02-mentoria-mercado-tec-esfriou.txt` |
| 3 | Mentoria 2 — "Como se diferenciar quando todo mundo usa IA" (Júlia, Michael Page) | Transcrição de vídeo | https://www.youtube.com/watch?v=MNR468ZegVI | `03-mentoria-diferencial-com-ia.txt` |
| 4 | Mentoria 3 — "O que sustenta crescimento e empregabilidade em tech" (Camilo + Júlia, Michael Page) | Transcrição de vídeo | https://www.youtube.com/watch?v=aiemUUl5dhY | `04-mentoria-empregabilidade-crescimento.txt` |
| 5 | Site institucional Michael Page Brasil (home) | Página web | https://www.michaelpage.com.br/ | `05-site-michaelpage-home.md` |
| 6 | Página Talent Trends 2026 | Página web | https://www.michaelpage.com.br/talent-trends | `06-site-michaelpage-talent-trends.md` |

O desafio pede de 3 a 5 fontes; optei por 6 porque as quatro transcrições de vídeo e as
duas páginas do site cumprem papéis diferentes e complementares: os vídeos trazem os
critérios de avaliação usados por recrutadores reais (qualitativo), enquanto o site
confirma — ou não — a existência de estrutura de apoio ao candidato (estrutural).

## Como as transcrições foram obtidas

Extração automática das legendas públicas do YouTube via biblioteca
`youtube-transcript-api`, script em `scripts/extract_transcripts.py`. Não houve edição
de conteúdo — apenas concatenação do texto das legendas em um único arquivo por vídeo.
