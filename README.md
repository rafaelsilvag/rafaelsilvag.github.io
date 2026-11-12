# Rafael Silva Guimarães — site pessoal

Site estático em português, com opção de interface em inglês. Compatível com GitHub Pages e sem dependências para publicação.

## Páginas e idiomas

- `index.html`: perfil, pesquisa e links profissionais.
- `publications.html`: publicações selecionadas e acesso ao Google Scholar.
- `classes.html`: disciplinas organizadas por ano e semestre.
- `assets/style.css`: tema escuro e estilos compartilhados.
- `assets/i18n.js`: alternância de idioma, gerada por `scripts/localize_site.py`.

Os botões **Português** e **English** alternam o perfil e a interface. A escolha é lembrada no navegador e transmitida nos links internos. O parâmetro `?lang=en` abre diretamente a interface em inglês; `?lang=pt-BR` abre em português. Sem JavaScript, o conteúdo padrão permanece em português. Títulos oficiais de publicações preservam o idioma original. Nomes das disciplinas e materiais didáticos permanecem em português, com aviso na interface em inglês.

Para ajustar traduções, edite o catálogo `PAIRS` em `scripts/localize_site.py` e execute `python3 scripts/localize_site.py`. Esse script exige BeautifulSoup e atua sobre os textos da interface, preservando a estrutura dos links e os materiais de ensino.

## Disciplinas

Cada disciplina tem seu próprio diretório, com um `index.html` independente. Apresentações HTML, PDFs e demais arquivos podem ser colocados diretamente nele e vinculados por caminhos relativos.

- `teaching/2027/1/computer-networks-ii/`: Redes de Computadores II — Técnico Integrado em Informática para Internet.
- `teaching/2027/1/network-services/`: Serviços de Redes para Internet — Sistemas de Informação.

Serviços de Redes para Internet está organizada em 8 tópicos com até três subtópicos cada. O planejamento distribui 60 aulas em 72 horas (26 teóricas e 46 práticas), incluindo duas provas e três trabalhos. Fundamentos e IPv4 formam um único tópico; CI/CD reúne testes, build, publicação e entrega. O projeto final ocupa quatro aulas. Cada tópico tem uma apresentação HTML e uma página de atividades. Consulte o README da disciplina para edição dos materiais.

O plano em PDF é exportado da própria planilha institucional, com as tabelas, os campos e os cabeçalhos do modelo. O script `scripts/prepare-teaching-plan.py` recebe o caminho do modelo XLSX e prepara a planilha atualizada e uma cópia temporária para impressão. O arquivo original é preservado. A exportação PDF usa LibreOffice; a cópia de impressão inclui o plano preenchido e omite os anexos sem carga horária e a aba auxiliar.

## Prévia e publicação

Execute `python3 -m http.server 8000` na raiz e abra http://localhost:8000. No GitHub Pages, publique a branch `main` a partir da raiz do repositório.

A foto atual é o avatar público do GitHub, em 460 × 460 pixels. As publicações selecionadas foram obtidas do perfil público do Google Scholar e a lista completa continua vinculada ao perfil original.
