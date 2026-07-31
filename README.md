# Caderno Temático — Como se tornar o profissional que a Michael Page contrata (e o gap que você pode preencher)

Projeto do desafio **"Caderno Temático no NotebookLM"** (DIO), usando IA como ferramenta
de aprendizagem ativa. Tema escolhido: **os critérios reais de contratação da Michael
Page para vagas de tecnologia** — extraídos diretamente de recrutadores da empresa — e,
a partir disso, **um projeto de IA que gera impacto real para a Michael Page**, cobrindo
uma lacuna que a própria empresa expõe em seu material público.

---

## 1. Contexto e Objetivos

### Por que esse tema

A Michael Page fez uma parceria com a DIO para lançar o bootcamp gratuito *"Criando seu
primeiro agente de IA"*, com três mentorias conduzidas por recrutadores reais da empresa
(Camilo e Júlia, ambos da divisão de tecnologia) mais uma live de lançamento com o time
de marketing (Manuela). Nesses quatro encontros, os recrutadores descrevem, com
exemplos concretos de processos seletivos reais, exatamente o que diferencia um
candidato aprovado de um reprovado. Isso é uma fonte rara: não é opinião de mercado
genérica, é o critério de avaliação de quem toma a decisão de contratar, dito na
primeira pessoa.

Ao mesmo tempo, o site da Michael Page (`michaelpage.com.br`) foi analisado para checar
se existe, hoje, alguma estrutura própria que ajude o candidato a *aplicar* esses
critérios antes de uma entrevista real. A resposta, confirmada por scraping direto das
páginas (ver `fontes/05` e `fontes/06`), é **não**: o site tem vagas, Guia Salarial,
artigos de "Advice" (blog) e a ferramenta interativa Talent Trends — todo conteúdo é
informativo/passivo. Não há simulador de entrevista, não há ferramenta de
diagnóstico de currículo/portfólio, não há prática guiada. É exatamente esse gap que
motiva a segunda metade deste projeto.

### Objetivos de estudo

1. Extrair e organizar, a partir das quatro mentorias, os critérios reais que fazem um
   candidato avançar em processo seletivo na Michael Page.
2. Estruturar esse conhecimento em um miniguia aplicável, por estágio de carreira
   (júnior → pleno → sênior), com passos concretos de preparação.
3. Usar o NotebookLM como ferramenta de curadoria e verificação dessas fontes,
   documentando o processo de engenharia de prompt (o que funcionou, o que não
   funcionou, como corrigi).
4. Identificar, com base cruzada entre o site e as falas dos próprios recrutadores, uma
   lacuna real de produto/serviço da Michael Page e propor — e prototipar — uma solução
   de IA para fechá-la.

---

## 2. Curadoria de Fontes

Lista completa, com links e descrição do papel de cada fonte, em
[`fontes/fontes.md`](fontes/fontes.md). Resumo:

- 4 transcrições de mentorias/live do bootcamp Michael Page × DIO (YouTube, extraídas
  via `youtube-transcript-api`, script em `scripts/extract_transcripts.py`)
- 2 páginas do site institucional da Michael Page (home e Talent Trends), extraídas via
  Firecrawl

Todos os arquivos `.txt`/`.md` da pasta `fontes/` são o material a ser carregado como
fonte no NotebookLM.

---

## 3. Engenharia de Prompts e "Cicatrizes"

> **Nota de honestidade metodológica:** este projeto foi construído com apoio de IA
> (Claude Code) para pesquisa, extração e organização — mas eu não tenho acesso
> operacional ao NotebookLM a partir daqui. Por isso, esta seção é entregue como um
> **kit pronto para execução**: perguntas estratégicas desenhadas, variações de prompt
> já pensadas para antecipar problemas comuns do NotebookLM, e uma tabela de registro
> com campos em aberto. **Eu, como aluno, preciso rodar cada prompt no meu caderno real
> e preencher os campos `[PREENCHER]`** com a resposta obtida, as fontes que o
> NotebookLM citou e a dificuldade que encontrei. Isso é o que a DIO pede — pensamento
> crítico e raciocínio documentado, não um resultado fabricado.

### Perguntas estratégicas (roteiro sugerido, em ordem de aplicação)

| # | Pergunta | Por que essa pergunta | O que eu esperava vs. o que preciso checar |
|---|----------|------------------------|----------------------------------------------|
| 1 | "Segundo as fontes, quais são os 5 sinais que geram confiança em uma entrevista na Michael Page? Cite a fonte exata de cada um." | Testa se o NotebookLM ancora a resposta na fala do Camilo (mentoria 2) e não mistura com conhecimento genérico de internet. | Esperado: clareza, profundidade, raciocínio, contexto, capacidade de explicar decisões — todos citando `02-mentoria-mercado-tec-esfriou.txt`. |
| 2 | "Compare o que a Júlia diz sobre 'diferencial que não é usar IA, mas como e por que usar' com o que a Manuela diz sobre 'barreira de acesso ao conhecimento'. Existe uma tensão ou eles se complementam?" | Pergunta de síntese cruzada entre duas fontes — testa se o NotebookLM realmente lê múltiplos documentos em conjunto, não só o mais recente carregado. | Risco de "cicatriz": o modelo pode responder só com uma fonte e ignorar a outra. |
| 3 | "Monte uma tabela com o que muda entre um candidato júnior, pleno e sênior segundo a Júlia na mentoria 3, com as perguntas típicas que cada nível faz." | Extrai o framework júnior/pleno/sênior (que uso no miniguia da seção 4) de forma estruturada. | Verificar se a tabela bate com a leitura manual da transcrição — números/citações de IA erram fácil. |
| 4 | "O site da Michael Page (fontes 05 e 06) oferece algum curso, simulador ou ferramenta de prática para candidatos? Liste tudo que existe hoje." | Valida objetivamente o gap central do projeto usando só as fontes, sem opinião externa. | Esperado: Guia Salarial, Talent Trends (dados), vagas, blog "Advice" — nenhuma ferramenta prática. |
| 5 | "Quais expectativas os recrutadores da Michael Page dizem ter dos candidatos que **não** são atendidas por nenhuma ferramenta hoje disponível no site da própria empresa?" | Pergunta-síntese final: cruza os critérios (fontes 1-4) com a ausência estrutural (fontes 5-6) para chegar à tese do projeto de impacto. | Esta é a pergunta mais exigente para o NotebookLM — provável que precise de 2-3 variações de prompt até a resposta ficar bem fundamentada. |

### Variações de prompt testadas (para cada pergunta acima)

- **Variação direta**: pergunta como está na tabela.
- **Variação com restrição de citação**: adicionar `"responda apenas com base nas fontes carregadas e cite o nome do arquivo-fonte de cada afirmação"` — útil quando a resposta parecer genérica demais.
- **Variação decomposta**: se a resposta vier rasa, quebrar a pergunta em 2-3 perguntas menores e sequenciais (ex.: primeiro pedir a lista dos sinais, depois pedir exemplos de cada um).

### Registro de execução (preencher após rodar no NotebookLM)

| Prompt (#) | Resposta obtida | Fontes citadas pelo NotebookLM | Dificuldade encontrada | Como resolvi |
|---|---|---|---|---|
| 1 | `Os **5 sinais que chamam a atenção e geram confiança** em uma entrevista, também referidos como os cinco pilares, são:

1. **Clareza**: A capacidade de apresentar o que você faz de forma compreensível e direta.
2. **Profundidade**: Demonstrar detalhes profundos sobre como você construiu um projeto ou solução, seja na parte técnica ou comportamental.
3. **Raciocínio**: Apresentar a lógica de pensamento que você utilizou ao longo do desenvolvimento do seu trabalho.
4. **Contexto**: Explicar qual era o objetivo real por trás da criação daquela solução e até onde você pretendia chegar.
5. **Capacidade de explicar decisões**: Conseguir justificar de maneira clara e embasada o porquê de ter escolhido um determinado caminho técnico ou estratégico em vez de outro.

---

💡 Se você quiser, podemos analisar o que as fontes dizem sobre como esses sinais se aplicam na prática para diferenciar os candidatos na hora de responder às perguntas dos gestores.` | `**Fonte exata:**
Todos esses sinais são apontados pelo recrutador sênior Camilo no vídeo **"Talent Trends 2026: o que mudou no mercado tech?"**.` | `Estruturar o prompt` | `Usei o Claude Code via CLI para otimizar minha ideia e gerar em seguida o prompt` |
| 2 | `[PREENCHER]` | `[PREENCHER]` | `Estruturar o prompt` | `Usei o Claude Code via CLI para otimizar minha ideia e gerar em seguida o prompt` |
| 3 | `[PREENCHER]` | `[PREENCHER]` | `Estruturar o prompt` | `Usei o Claude Code via CLI para otimizar minha ideia e gerar em seguida o prompt` |
| 4 | `[PREENCHER]` | `[PREENCHER]` | `Estruturar o prompt` | `Usei o Claude Code via CLI para otimizar minha ideia e gerar em seguida o prompt` |
| 5 | `[PREENCHER]` | `[PREENCHER]` | `Estruturar o prompt` | `Usei o Claude Code via CLI para otimizar minha ideia e gerar em seguida o prompt` |

Dificuldades comuns esperadas com NotebookLM (para orientar o preenchimento acima):
respostas que misturam fontes em português e trechos mal transcritos (as legendas do
YouTube têm erros de transcrição automática, ex. "Di" em vez de "DIO", "sonoridade" em
vez de "senioridade" — vale registrar se isso confundiu alguma resposta); tendência do
modelo a resumir demais e perder o exemplo concreto (caso do "candidato A vs. candidato
B"); necessidade de reformular quando a resposta ficar genérica em vez de ancorada nas
fontes.

---

## 4. Miniguia de Estudo — Entrega Final

### 4.1 Resumo estruturado: os 5 sinais que geram confiança em entrevista

*(fonte: Camilo, `fontes/02-mentoria-mercado-tec-esfriou.txt`)*

O mercado não "esfriou" — ficou mais seletivo e maduro. Antes, contratava-se por
urgência; hoje, por valor gerado. Nesse cenário, currículos e respostas de entrevista
ficaram parecidos porque todo mundo usa IA para otimizar os dois. O que separa quem
avança é a presença simultânea de:

1. **Clareza** — explicar o que fez sem enrolação.
2. **Profundidade** — não parar na resposta certa e genérica; explicar o "como".
3. **Raciocínio** — mostrar a lógica por trás de uma escolha, não só o resultado.
4. **Contexto** — qual era o problema, por que aquele projeto existia.
5. **Capacidade de explicar decisões** — por que esse caminho e não outro.

**Caso prático usado na mentoria:** dois candidatos tecnicamente equivalentes. O
candidato A responde corretamente, mas de forma superficial e genérica. O candidato B
usou IA para se preparar, mas contextualiza a experiência, explica as decisões e
demonstra pensamento crítico. B avança — não porque sabe mais, mas porque **demonstra
como pensa**.

### 4.2 Resumo estruturado: o diferencial não é usar IA, é como e por quê

*(fonte: Júlia, `fontes/03-mentoria-diferencial-com-ia.txt`)*

Dados citados na mentoria: 64% das pessoas usam IA no dia a dia, 71% dos candidatos
usam IA para otimizar candidaturas, 62% dos empregadores usam IA nos processos
seletivos. Conclusão da Júlia: a pergunta relevante deixou de ser "você usa IA?" e
passou a ser "como você usa, e o que isso revela sobre o seu julgamento?".

- **Armadilha a evitar:** achar que dominar uma ferramenta de IA é vantagem permanente.
  Toda ferramenta se populariza (aconteceu com Excel, Power BI, cloud — vai acontecer
  com IA). Vantagem durável é a interpretação, não a ferramenta.
- **Quatro coisas que a IA não substitui:** julgamento, contexto, contato humano/
  influência, responsabilidade (assumir consequência de uma decisão).
- **Caso de erro real (cicatriz citada pela recrutadora):** um candidato usou IA para
  montar um plano de entrevista perfeito, decorou respostas prontas — e travou quando
  a pergunta fugiu do script ("por que você escolheu essa decisão?"). Lição: usar IA
  para se preparar é ótimo; usar IA para substituir o próprio raciocínio é o erro.

### 4.3 Resumo estruturado: o triângulo tecnologia–negócio–pessoas e a progressão de carreira

*(fonte: Camilo + Júlia, `fontes/04-mentoria-empregabilidade-crescimento.txt`)*

> "Quem entende de tecnologia resolve tarefas. Quem entende de tecnologia e negócio
> resolve problemas. Quem conecta tecnologia, negócio e pessoas gera transformação."

O que trava uma carreira, segundo os recrutadores, quase nunca é falta de competência
técnica — é resistência a mudança, baixa visibilidade, comunicação limitada e foco
exclusivamente técnico. Empregabilidade não é "conseguir emprego", é continuar
relevante.

**Progressão de senioridade por tipo de pergunta que a pessoa faz** (framework da
Júlia, `fontes/03`):

| Nível | Pergunta típica | O que isso revela |
|---|---|---|
| Júnior | "Como eu faço isso?" | Fase exploratória — ainda aprendendo o "como". |
| Pleno | "Qual solução eu uso?" | Já sabe fazer; decide entre alternativas conhecidas. |
| Sênior | "Como esse problema está sendo definido?" | Atua antes da solução — na definição correta do problema. |

Importante: senioridade não é tempo de empresa, é **repertório + contexto + capacidade
de decisão** — inclusive repertório trazido de outra área (ex.: alguém com 10 anos em
finanças migrando para dados entra com bagagem de resolução de problema complexo e
gestão de stakeholders, mesmo sendo iniciante nas ferramentas técnicas).

### 4.4 Como se preparar em cada estágio de aprendizado

**Estágio 1 — Fundação (perfil júnior / iniciante em tecnologia ou IA)**
- *Como se preparar:* construir 1 projeto aplicado, pequeno e completo, do início ao
  fim (não precisa ser complexo — vale mais um problema simples resolvido de ponta a
  ponta do que um projeto ambicioso incompleto).
- *O que fazer:* documentar o projeto no GitHub com código organizado; gravar uma demo
  curta ou vídeo; escrever, para esse projeto, a narrativa contexto → motivação →
  tecnologias usadas → decisão tomada → resultado → próximos passos (estrutura exigida
  pelo Camilo, `fontes/01`).
- *Como aplicar:* ao ser entrevistado, não recitar o que o projeto faz — explicar por
  que ele existe e por que aquelas escolhas técnicas foram feitas.

**Estágio 2 — Aplicação (perfil pleno / em transição de carreira)**
- *Como se preparar:* já sabendo executar, focar em aprender a **escolher entre
  soluções** e a comunicar isso para públicos não técnicos.
- *O que fazer:* pegar o repertório de uma área anterior (mesmo não-técnica) e conectar
  explicitamente com o novo objetivo de carreira — a Júlia é explícita: "não entre como
  Python + backend, entre como profissional de X que se especializou em tecnologia".
- *Como aplicar:* em entrevista, contextualizar a transição como continuidade de
  repertório, não como reinício do zero.

**Estágio 3 — Consolidação (perfil sênior / liderança)**
- *Como se preparar:* deslocar o foco de "sei fazer" para "sei definir o problema
  certo" e "sei influenciar sem autoridade formal".
- *O que fazer:* buscar visibilidade interna (compartilhar resultados, não só
  entregá-los), aceitar ambiguidade, treinar comunicação executiva.
- *Como aplicar:* em entrevista, é avaliado pela qualidade das decisões que tomou, não
  pela quantidade de código que escreveu.

### 4.5 Glossário

| Termo | Definição |
|---|---|
| **Hard skill** | Competência técnica (ex.: Python, cloud, LLMs). "É o convite" — abre a porta, mas não garante a permanência. |
| **Soft skill / habilidade de impacto** | Comunicação, colaboração, adaptabilidade, pensamento crítico. "É a conquista" — o que sustenta crescimento. Termo "habilidade de impacto" usado pela Júlia para evitar a ideia de que soft skill é opcional. |
| **Agente de IA** | Sistema que usa um LLM para executar tarefas de forma mais autônoma que um simples chat, geralmente orquestrando ferramentas/etapas. |
| **LLM** | Large Language Model — modelo de linguagem que gera texto a partir de um prompt. |
| **Prompt** | Instrução dada a um LLM. |
| **Business Partner (BP) de tecnologia** | Perfil técnico que também senta com áreas de negócio para traduzir dor em solução — citado como perfil crescente na Michael Page. |
| **Talent Trends** | Estudo global anual da Michael Page (~60 mil profissionais, 36 países) sobre tendências de contratação e carreira. |
| **Senioridade por repertório** | Framework em que o nível não é definido por tempo de casa, mas pela combinação de contexto, tomada de decisão e experiência transferível. |
| **Candidato A / Candidato B (caso Camilo)** | Estudo de caso da mentoria 2: dois candidatos tecnicamente equivalentes, onde vence quem contextualiza e explica decisões, não quem "sabe mais". |

### 4.6 Prompts reutilizáveis (para revisões futuras)

```
Baseado nas fontes carregadas, monte um quiz de 5 perguntas sobre os critérios de
avaliação da Michael Page em entrevistas de tecnologia, com gabarito citando a fonte.
```

```
Estou me preparando para uma entrevista de tecnologia. Aqui está a descrição do meu
projeto: [COLAR DESCRIÇÃO]. Reescreva essa descrição seguindo a estrutura
contexto → motivação → tecnologias → decisão → resultado → próximos passos, no mesmo
padrão descrito nas fontes deste caderno.
```

```
Simule uma pergunta de entrevista que teste minha profundidade e capacidade de explicar
decisões (não apenas conhecimento técnico), no estilo das entrevistas descritas nas
fontes deste caderno, sobre o seguinte projeto: [COLAR DESCRIÇÃO].
```

```
Compare meu nível de senioridade (descreva sua experiência: [COLAR]) com o framework
júnior/pleno/sênior das fontes deste caderno. Em qual estágio eu me encaixo e por quê?
```

---

## 5. Análise de Impacto — o projeto de IA para a Michael Page

### O que a Michael Page faz

Consultoria global de recrutamento especializado: recrutamento permanente e temporário
(Page Interim), executive search/assessment para C-level (Page Executive) e soluções
corporativas em escala (RPO, workforce sob demanda — Page Enterprise Solutions). Também
produz conteúdo de mercado (Guia Salarial anual, estudo Talent Trends).

### O gap real (confirmado por fonte primária e por fonte estrutural)

Cruzando as fontes 1-4 (o que os recrutadores dizem exigir) com as fontes 5-6 (o que o
site oferece), o padrão é nítido:

- Os recrutadores dizem, com todas as letras, que o que diferencia um candidato é
  **contexto, profundidade e capacidade de explicar decisões** — e que **usar IA para
  se preparar sem desenvolver pensamento crítico é um erro comum e recorrente** (caso do
  candidato que "travou").
- O site da Michael Page não tem **nenhuma** ferramenta para o candidato treinar ou
  medir isso antes de uma entrevista real. Existe conteúdo informativo (Guia Salarial,
  Talent Trends, blog "Advice") — nada interativo, nada com feedback individualizado.
- A própria Manuela nomeia o problema na live de lançamento: "existe uma barreira de
  acesso ao conhecimento" — e o bootcamp com a DIO foi a resposta da empresa para a
  camada de *conteúdo técnico*. Mas ele não resolve a camada de *prática de
  comunicação/narrativa*, que é exatamente o que os próprios recrutadores da mesma
  empresa dizem ser o fator decisório.

Essa é a lacuna: a Michael Page identificou e comunicou publicamente o critério de
avaliação, mas não oferece a ferramenta prática que ajudaria o candidato a atendê-lo.

### Roadmap de implementação

**Curto prazo (0–3 meses) — Coach de Entrevista e Portfólio**
Protótipo funcional incluído neste repositório (`main.py`): ferramenta de linha de
comando que recebe a descrição de um projeto/experiência do candidato e devolve (1) a
narrativa reestruturada no formato contexto→motivação→tecnologias→decisão→resultado→
próximos passos e (2) uma simulação de pergunta de entrevista + avaliação nos 5 sinais
(clareza, profundidade, raciocínio, contexto, capacidade de decisão) — os mesmos
critérios que o Camilo descreve usar de verdade. Custo de implementação baixo (um
script + uma API de LLM), pode nascer como ferramenta interna de apoio a candidatos do
próprio bootcamp Michael Page × DIO antes de virar produto do site.

**Médio prazo (3–12 meses) — Diagnóstico de gap de skills**
Cruzar o currículo/portfólio do candidato com os dados do Talent Trends (que a Michael
Page já coleta) e com as vagas reais abertas no portal, para apontar objetivamente:
"você está a X% do perfil que as vagas de [área] estão pedindo, e falta Y". Isso usa
dado que a empresa já possui, mas hoje só expõe de forma agregada/genérica na
ferramenta interativa do Talent Trends — não de forma personalizada por candidato.

**Longo prazo (12+ meses) — Trilha contínua integrada ao portal de vagas**
Fechar o loop entre "o que a Michael Page sabe sobre o mercado" (Talent Trends) e "o
que o candidato pratica" (Coach de entrevista): simulações de entrevista calibradas por
setor/senioridade, treinadas nos critérios reais dos recrutadores, integradas ao
cadastro de currículo do site — o candidato treina, recebe feedback, e só então
aplica, chegando mais preparado ao processo seletivo real.

### O que a Michael Page exige mas não oferece (síntese)

| Exigido (fala dos recrutadores) | Oferecido hoje no site | Gap |
|---|---|---|
| Contextualizar projetos/experiências | Nenhuma ferramenta guiada | Total |
| Explicar decisões com profundidade | Nenhum simulador de entrevista | Total |
| Usar IA com pensamento crítico, não para decorar respostas | Nenhuma orientação prática anti-genérico | Total |
| Entender em qual nível de senioridade se encaixa | Vagas listadas por nível, sem autoavaliação | Parcial |
| Se posicionar em transição de carreira | Artigos genéricos de "Advice" | Parcial (conteúdo existe, mas é passivo) |

### O que não foi percebido e precisa ser feito

O bootcamp Michael Page × DIO resolve a **entrada** (aprender IA do zero, de graça,
removendo a barreira de custo). Mas ele termina no certificado — a própria Júlia, na
live de lançamento (`fontes/01`), alerta: "não parar no certificado... transforma o
seu conhecimento num projeto, vende seu peixe mesmo".
O que falta é exatamente a ponte entre "terminei o bootcamp" e "sei me apresentar como
o candidato B, não o candidato A" — e essa ponte é o produto que este projeto propõe.

---

## 6. Protótipo — Coach de Entrevista e Portfólio (`main.py`)

Script de linha de comando, propositalmente pequeno e honesto sobre suas limitações:

- Não guarda nem envia dados para nenhum lugar além da API de IA usada.
- Requer uma chave de API própria (`ANTHROPIC_API_KEY`) — **nenhuma chave está
  hardcoded no código**; sem a variável de ambiente configurada, o script informa o
  erro claramente e não executa.
- Os critérios usados no prompt do sistema (5 sinais, estrutura narrativa) vêm
  diretamente das fontes 1-4 deste repositório — não são inventados.

### Como rodar

```bash
uv sync
export ANTHROPIC_API_KEY="sua-chave-aqui"   # no PowerShell: $env:ANTHROPIC_API_KEY = "..."
uv run python main.py
```

O script pede, interativamente, a descrição do seu projeto/experiência e devolve a
narrativa reestruturada + a simulação de entrevista com avaliação.

**Status de verificação:** o caminho de erro (ausência de `ANTHROPIC_API_KEY`) foi
testado e funciona como esperado. O caminho de sucesso (chamada real à API) não foi
executado nesta sessão por não haver uma chave configurada no ambiente — o modelo
usado (`claude-sonnet-5`) é um ID de API válido e confirmado, então a chamada deve
funcionar assim que uma chave for fornecida, mas recomendo rodar um teste manual antes
de considerar o protótipo validado ponta a ponta.

---

## Estrutura do repositório

```
README.md                 este arquivo
main.py                   protótipo — Coach de Entrevista e Portfólio
pyproject.toml            dependências (uv)
fontes/
  fontes.md               tabela de fontes com links
  01-04-*.txt             transcrições das 4 mentorias
  05-06-*.md              páginas do site Michael Page
scripts/
  extract_transcripts.py  script usado para extrair as transcrições do YouTube
```
