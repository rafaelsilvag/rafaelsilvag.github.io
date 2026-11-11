# Serviços de Redes para Internet — 2027/1

A página `index.html` apresenta 10 tópicos, cada um com dois ou três subtópicos e links próprios para apresentação e atividades. O planejamento distribui 60 aulas em 72 horas (26 teóricas e 46 práticas), incluindo as avaliações. Datas e agrupamento em encontros dependem do calendário acadêmico.

## Materiais por tópico

Todos os arquivos ficam diretamente neste diretório:

- `topico-01.html` a `topico-10.html`: páginas reservadas para futuras apresentações HTML.
- `atividade-topico-01.html` a `atividade-topico-10.html`: tarefas e entregas propostas para cada tópico.
- `plano-de-ensino.pdf`: exportação da própria planilha institucional, em quatro páginas.
- `plano-de-ensino.xlsx`: plano editável no formato do modelo fornecido, com conteúdo, horas e avaliações atualizados.
- `programa.json`: tópicos, subtópicos, atividades e distribuição das 60 aulas.
- `disciplina.css`: estilos específicos da disciplina.

Ao produzir slides, edite o `topico-NN.html` correspondente e retire o aviso “Apresentação em preparação”. Remova também o rótulo “Em preparação” do link no índice. Use links relativos para arquivos colocados neste diretório.

O comando `python3 scripts/build-network-course.py`, na raiz do repositório, reconstrói o índice a partir de `programa.json` e cria somente páginas de tópicos/atividades que ainda não existam. Apresentações existentes são preservadas. Os dois itens introdutórios removidos têm suas páginas antigas atualizadas para conteúdo de TCP/IP; os demais URLs de aulas anteriores continuam acessíveis por compatibilidade.

Os textos da interface ficam em português por padrão, com seletor para inglês. O conteúdo pedagógico permanece em português. Ao alterar os tópicos, atualize também o plano de ensino; os slides existentes não são reescritos automaticamente.

## Avaliações propostas

| Avaliação | Aulas | Pontos |
| --- | --- | --- |
| T1 — Ambiente de rede com containers | 20 | 15 |
| P1 — Redes, Docker e Compose | 29 e 30 | 20 |
| T2 — Ambiente integrado com Compose | 42 | 20 |
| P2 — Integração de serviços, CI/CD e operação | 57 e 58 | 20 |
| T3 — Projeto final com CI/CD e monitoramento | 59 e 60 | 25 |

Cada prova é uma única avaliação dividida em duas aulas. As duas sessões finais pertencem ao mesmo T3. Os trabalhos são incrementais. Datas e horário de atendimento permanecem a preencher; aprovação, recuperação e segunda chamada seguem as normas institucionais.
