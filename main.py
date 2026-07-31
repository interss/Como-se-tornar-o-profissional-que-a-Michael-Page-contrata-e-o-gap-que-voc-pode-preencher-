"""Coach de Entrevista e Portfolio -- Michael Page.

Prototipo do projeto de impacto descrito no README (secao 6). Recebe a descricao
de um projeto/experiencia do candidato e devolve:

1. Uma narrativa reestruturada no formato contexto -> motivacao -> tecnologias ->
   decisao -> resultado -> proximos passos (estrutura descrita pelo recrutador
   Camilo em fontes/01-live-lancamento-bootcamp.txt).
2. Uma simulacao de pergunta de entrevista + avaliacao nos "5 sinais" que geram
   confianca em processo seletivo, segundo fontes/02-mentoria-mercado-tec-esfriou.txt:
   clareza, profundidade, raciocinio, contexto, capacidade de explicar decisoes.

Requer a variavel de ambiente ANTHROPIC_API_KEY. Nenhuma chave fica no codigo.
"""

import os
import sys

import anthropic

MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = """Voce e um recrutador senior de tecnologia da Michael Page, no mesmo \
estilo descrito nas mentorias do bootcamp Michael Page x DIO. Sua avaliacao segue \
estritamente os "5 sinais" citados pelos recrutadores da empresa: clareza, \
profundidade, raciocinio, contexto e capacidade de explicar decisoes. Voce despreza \
respostas genericas ou decoradas e valoriza candidatos que demonstram COMO pensam, \
nao apenas O QUE fizeram.

Dado um relato de projeto ou experiencia profissional de um candidato, produza:

1. NARRATIVA REESTRUTURADA -- reescreva o relato no formato:
   Contexto (qual problema existia) / Motivacao (por que esse projeto) /
   Tecnologias usadas / Decisao (por que esse caminho e nao outro) /
   Resultado (impacto gerado) / Proximos passos (o que evoluiria).

2. PERGUNTA DE ENTREVISTA -- uma pergunta dificil e especifica que um recrutador \
faria sobre esse relato para testar profundidade real (nao generica).

3. AVALIACAO NOS 5 SINAIS -- para cada sinal (clareza, profundidade, raciocinio, \
contexto, capacidade de explicar decisoes), dê uma nota de 1 a 5 e uma frase \
justificando, com base SOMENTE no que o candidato relatou.

Seja direto e honesto -- se o relato for raso, diga isso claramente e explique o que \
falta, no mesmo tom construtivo mas sem rodeios usado nas mentorias."""


def get_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(
            "Erro: variavel de ambiente ANTHROPIC_API_KEY nao encontrada.\n"
            "Defina sua propria chave antes de rodar, por exemplo:\n"
            "  export ANTHROPIC_API_KEY='sua-chave-aqui'   (bash)\n"
            "  $env:ANTHROPIC_API_KEY = 'sua-chave-aqui'   (PowerShell)",
            file=sys.stderr,
        )
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


def coach(client: anthropic.Anthropic, relato: str) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": relato}],
    )
    return "".join(block.text for block in response.content if block.type == "text")


def main() -> None:
    client = get_client()
    print("=== Coach de Entrevista e Portfolio -- Michael Page ===")
    print("Descreva um projeto ou experiencia profissional sua (Ctrl+D ou linha vazia para enviar):\n")

    linhas = []
    try:
        while True:
            linha = input()
            if not linha:
                break
            linhas.append(linha)
    except EOFError:
        pass

    relato = "\n".join(linhas).strip()
    if not relato:
        print("Nenhum relato informado. Encerrando.", file=sys.stderr)
        sys.exit(1)

    print("\nAnalisando com base nos criterios reais de recrutadores da Michael Page...\n")
    print(coach(client, relato))


if __name__ == "__main__":
    main()
