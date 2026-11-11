# Serviços de Redes para Internet — 2027/1

A página `index.html` organiza 60 aulas em 11 unidades, somando 72 horas (26 teóricas e 46 práticas). Cada item tem 1 ou 2 horas de planejamento; datas e agrupamento em encontros dependem do calendário acadêmico.

## Materiais da disciplina

Todos os arquivos ficam diretamente neste diretório:

- `aula-01.html` a `aula-60.html`: páginas reservadas para futuras apresentações HTML. Ainda não são slides concluídos.
- `atividade-01.html` a `atividade-60.html`: propostas de atividades, objetivos e entregas; nas provas, somente orientações de estudo.
- `plano-de-ensino.pdf`: plano institucional atualizado, em quatro páginas.
- `plano-de-ensino.xlsx`: cópia editável do modelo fornecido, com identificação de 2027/1, conteúdo, horas e avaliações atualizados. O arquivo original em Downloads foi preservado.
- `programa.json`: organização das aulas, objetivos, tarefas e avaliações.
- `disciplina.css`: estilos específicos da disciplina.

Ao produzir uma apresentação, edite o `aula-NN.html` correspondente e retire o aviso “Apresentação em preparação”. No `index.html`, remova também o rótulo “Em preparação” do link daquela aula. Use nomes relativos para PDFs e outros arquivos colocados neste diretório.

O comando `python3 scripts/build-network-course.py`, executado na raiz do repositório, reconstrói o índice a partir de `programa.json` e cria somente páginas de aulas/atividades que ainda não existam. Páginas existentes são preservadas para não sobrescrever apresentações editadas. O gerador não atualiza automaticamente o plano em PDF/XLSX. Caso o cronograma seja alterado, confira esses documentos e as atividades existentes.

## Avaliações propostas

| Avaliação | Aulas | Pontos |
| --- | --- | --- |
| T1 — Ambiente de rede com containers | 20 | 15 |
| P1 — Redes, Docker e Compose | 29 e 30 | 20 |
| T2 — Ambiente integrado com Compose | 42 | 20 |
| P2 — Integração de serviços, CI/CD e operação | 57 e 58 | 20 |
| T3 — Projeto final com CI/CD e monitoramento | 59 e 60 | 25 |

Cada prova é uma única avaliação dividida em duas aulas. As duas sessões finais pertencem ao mesmo T3. Os trabalhos são incrementais; reaproveitam e aprimoram o ambiente produzido anteriormente. Regras de aprovação, recuperação e segunda chamada seguem definição institucional. Datas e horário de atendimento permanecem a preencher.
