# Serviços de Redes para Internet — 2027/1

A disciplina acompanha a evolução da infraestrutura de uma aplicação web simples, que será fornecida pelo professor. A linguagem e o repositório da aplicação-base serão definidos para a turma. O foco é a comunicação entre serviços, sua composição com Docker/Compose, a entrega por CI/CD e a operação do ambiente.

## Organização

HTTP e DNS são apresentados primeiro no host ou em uma VM do laboratório. Os mesmos serviços são depois executados em containers e integrados com Compose. O T1 é entregue após Docker, na aula 24.

Oito tópicos, com até três subtópicos cada, distribuem 56 aulas de conteúdo e projeto. As duas provas ocupam outras quatro aulas. Total: 60 aulas planejadas, correspondentes a 72 horas (26 teóricas e 46 práticas). Datas e agrupamento em encontros dependem do calendário acadêmico.

| Tópico ou avaliação | Aulas | Quantidade de aulas | Teoria (h) | Prática (h) | Total (h) |
| --- | --- | ---: | ---: | ---: | ---: |
| 1. Fundamentos de redes para aplicações | 1–8 | 8 | 6 | 4 | 10 |
| 2. Serviços HTTP e DNS | 9–16 | 8 | 4 | 6 | 10 |
| 3. Docker e execução de serviços | 17–24 | 8 | 4 | 6 | 10 |
| Prova 1 | 25–26 | 2 | 2 | 0 | 2 |
| 4. Docker Compose e integração de serviços | 27–32 | 6 | 2 | 5 | 7 |
| 5. Banco de dados e ambiente integrado | 33–38 | 6 | 2 | 5 | 7 |
| 6. CI/CD de aplicações com containers | 39–50 | 12 | 4 | 11 | 15 |
| 7. Monitoramento e diagnóstico | 51–54 | 4 | 0 | 5 | 5 |
| Prova 2 | 55–56 | 2 | 2 | 0 | 2 |
| 8. Projeto final e apresentação | 57–60 | 4 | 0 | 4 | 4 |
| **Total** | | **60** | **26** | **46** | **72** |

## Materiais por tópico

Todos os arquivos ficam diretamente neste diretório:

- `topico-01.html` a `topico-08.html`: páginas reservadas para futuras apresentações HTML.
- `atividade-topico-01.html` a `atividade-topico-08.html`: roteiros de atividades e entregas por tópico.
- `aula-01.html` a `aula-60.html` e `atividade-01.html` a `atividade-60.html`: detalhamento individual sincronizado com a distribuição atual.
- `plano-de-ensino.pdf`: exportação da planilha institucional.
- `programa.json`: fonte da organização de tópicos, aulas, atividades e avaliações.
- `disciplina.css`: estilos específicos da disciplina.

Ao produzir slides, edite o `topico-NN.html` correspondente, retire o aviso de preparação e atualize o rótulo do link no índice. Use links relativos para os arquivos da disciplina. Os URLs antigos dos tópicos 9 e 10 levam ao material atualizado de monitoramento e projeto final.

Execute `python3 scripts/build-network-course.py` na raiz para reconstruir o índice e criar materiais ausentes. Páginas existentes são preservadas. Para aplicar uma revisão curricular aos roteiros e apresentações ainda planejados, use `--refresh-materials`; essa opção reescreve os HTMLs de materiais e deve ser usada somente quando essa substituição for intencional.

Somente o PDF é publicado no site. A versão editável fica em `.local/planos/network-services/plano-de-ensino.xlsx`, fora do versionamento; ela deve ser mantida no ambiente de autoria. O plano é preparado por `scripts/prepare-teaching-plan.py`, recebendo o caminho do modelo XLSX e usando essa cópia editável local, e exportado para PDF no LibreOffice. O modelo original é preservado. A interface tem opção de inglês; os materiais pedagógicos permanecem em português.

## Avaliações propostas

| Avaliação | Marco | Aulas | Pontos |
| --- | --- | --- | ---: |
| T1 | Aplicação em containers: rede, imagem e persistência | 24 | 15 |
| P1 | Fundamentos de redes, HTTP/DNS e Docker | 25 e 26 | 20 |
| T2 | Ambiente integrado com HTTP, DNS, aplicação e banco | 38 | 20 |
| P2 | Compose, integração, CI/CD e monitoramento | 55 e 56 | 20 |
| T3 | Projeto final com CI/CD, monitoramento e recuperação | 57–60, entrega na aula 60 | 25 |

Os trabalhos evoluem o mesmo ambiente. Cada prova é uma única avaliação dividida em duas aulas. O T3 tem preparação e validação nas aulas 57 e 58 e apresentações nas aulas 59 e 60. Datas e horário de atendimento permanecem a preencher; aprovação, recuperação e segunda chamada seguem as normas institucionais.

## Vídeos e código em sala

Os vídeos originais ficam em `videos/`, na raiz do site. O campo `videos` de cada tópico em `programa.json` associa os arquivos a seus títulos e descrições. Os players ficam na página de apresentação do tópico, com links no índice e nas atividades. O carregamento começa quando solicitado pelo aluno.

- Tópico 1: `enderecoip.mp4` e `firewall.mp4` (apoio à revisão de IP, portas e regras de acesso).
- Tópico 2: `proxyreverso.mp4`.
- Tópico 3: `dockerkubernets.mp4` (Kubernetes é complementar, sem nova unidade obrigatória).

O link **Códigos das aulas** aponta para https://github.com/rafaelsilvag/servicos-de-redes-2027-1, também configurado em `metadata.codeRepository`.

Para conferir o currículo, os links e os materiais, execute `python3 scripts/check-network-course.py` na raiz.
