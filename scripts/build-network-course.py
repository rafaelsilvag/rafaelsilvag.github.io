"""Build the class index and missing lesson scaffolds; preserve existing lesson HTMLs."""
from pathlib import Path
from html import escape as esc
import json
ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT/'teaching/2027/1/network-services'
data=json.loads((COURSE/'programa.json').read_text())
meta=data['metadata']
def page(title,body):
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#0b1220"><meta name="description" content="{esc(title)} - Serviços de Redes para Internet, Sistemas de Informação, 2027/1."><title>{esc(title)} | Serviços de Redes para Internet</title><link rel="icon" href="../../../../assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../../../../assets/style.css"><link rel="stylesheet" href="disciplina.css"></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="container header-inner"><a class="brand" href="../../../../index.html" aria-label="Rafael Silva Guimarães — home">rsg<span>.</span></a><nav aria-label="Main navigation"><a href="../../../../index.html">About</a><a href="../../../../publications.html">Publications</a><a href="../../../../classes.html" aria-current="page">Classes</a></nav></div></header>
<main id="main" class="container course-main" lang="pt-BR"><nav class="breadcrumbs" aria-label="Navegação estrutural"><a href="../../../../classes.html">Classes</a><span aria-hidden="true">/</span><a href="index.html">Serviços de Redes para Internet</a><span aria-hidden="true">/</span><span>2027/1</span></nav>{body}</main><footer class="site-footer container"><p>Rafael Silva Guimarães<span class="footer-dot">·</span> Ifes, Brazil</p><a href="../../../../classes.html">All classes <span aria-hidden="true">↑</span></a></footer></body></html>\n'''
def rubric(a):
 return '<h2>Critérios de avaliação</h2><p>Distribuição de pontos proposta para esta avaliação.</p><ul>'+''.join(f'<li>{esc(label)}: {points} pontos.</li>' for label,points in a['criteria'])+f'</ul><p><strong>Total: {a["points"]} pontos.</strong> A participação individual será verificada na demonstração ou apresentação.</p>'
assessments=''.join(f'''<tr><th scope="row">{a['code']}</th><td>{esc(a['title'])}<small>{esc(a['kind'])}</small></td><td>{a['lessons']}</td><td>{a['points']}</td></tr>''' for a in data['assessments'])
units=''
for number,u in enumerate(data['units'],1):
 lessons=''
 for l in data['lessons'][u['start']-1:u['end']]:
  lessons+=f'''<li id="aula-{l['number']:02}" value="{l['number']}"><div class="lesson-entry"><div><h3>{esc(l['title'])}</h3><p>{esc(l['objective'])}</p><span class="lesson-meta">{l['type']} · {l['hours']} h</span></div><div class="lesson-links"><a href="{l['presentation']}">Apresentação <span class="resource-note">Em preparação</span></a><a href="{l['activity']}">{'Orientações da prova' if l['number'] in [29,30,57,58] else 'Atividades'}</a></div></div></li>'''
 units+=f'''<section class="curriculum-unit" id="unidade-{number}"><div class="unit-heading"><h2>{number:02}. {esc(u['title'])}</h2><p>Aulas {u['start']}–{u['end']} · {u['theory']+u['practice']} h · {u['theory']} T / {u['practice']} P</p></div><ol start="{u['start']}" class="lesson-list">{lessons}</ol></section>'''
refs=''.join(f'<li><a href="{r["url"]}" target="_blank" rel="noopener noreferrer">{esc(r["title"])} ↗</a></li>' for r in data['references'])
body=f'''<section class="course-hero"><p class="eyebrow">2027/1 · SISTEMAS DE INFORMAÇÃO</p><h1>Serviços de Redes para Internet<span class="accent">.</span></h1><p class="course-instructor">Professor: Rafael Silva Guimarães</p><p class="course-summary">Da conectividade IP à entrega de software: construção, integração e operação de serviços com Docker, Docker Compose e CI/CD.</p><div class="course-stats"><span><strong>60</strong> aulas enumeradas</span><span><strong>72 h</strong> carga horária total</span><span><strong>26 h</strong> teóricas</span><span><strong>46 h</strong> práticas</span></div><p class="schedule-note">{esc(meta['durationNote'])}</p><div class="course-actions"><a class="text-link" href="plano-de-ensino.pdf">Plano de ensino (PDF)</a><a class="text-link secondary-action" href="plano-de-ensino.xlsx">Plano editável (XLSX)</a><a class="text-link secondary-action" href="#cronograma">Ver as 60 aulas ↓</a></div></section>
<section class="course-section" aria-labelledby="project-title"><h2 id="project-title">Um projeto, três etapas</h2><p>O mesmo projeto evolui ao longo do semestre. No T1, a equipe planeja a rede e implanta containers. No T2, integra HTTP, DNS, aplicação web e banco de dados com Compose. No T3, automatiza testes, build, publicação e entrega para homologação, com monitoramento e recuperação.</p><p>Git e testes aparecem desde o início. O bloco de CI/CD consolida essa base em um pipeline com GitHub Actions. O ambiente de implantação será um host de laboratório ou uma máquina virtual definida para a turma.</p></section>
<section class="course-section" aria-labelledby="assessment-title"><h2 id="assessment-title">Avaliações</h2><p>{esc(meta['evaluationNote'])}</p><div class="table-scroll"><table><caption>Proposta de avaliações: 100 pontos</caption><thead><tr><th scope="col">Avaliação</th><th scope="col">Escopo</th><th scope="col">Aulas</th><th scope="col">Pontos</th></tr></thead><tbody>{assessments}</tbody></table></div><p class="schedule-note">Cada prova ocupa duas aulas consecutivas e constitui uma única avaliação. As aulas 59 e 60 são duas sessões de apresentação do mesmo Trabalho 3. {meta['calendar']}</p></section>
<section class="course-section" id="cronograma" aria-labelledby="schedule-title"><p class="eyebrow">PERCURSO DE APRENDIZAGEM</p><h2 id="schedule-title">Cronograma das 60 aulas</h2><p>As páginas de apresentação estão reservadas para os futuros slides HTML. As atividades já contêm uma proposta de tarefa e entrega; as páginas de prova apresentam somente orientações de estudo.</p><nav class="unit-nav" aria-label="Unidades do cronograma">{''.join(f'<a href="#unidade-{i}">{i:02}</a>' for i in range(1,len(data['units'])+1))}</nav>{units}</section>
<section class="course-section course-references"><h2>Referências técnicas</h2><ul>{refs}</ul></section>'''
(COURSE/'index.html').write_text(page(meta['title'],body))
for l in data['lessons']:
 n=l['number'];title=f'Aula {n:02} — {l["title"]}'
 common=f'''<p class="eyebrow">AULA {n:02} · {l['type'].upper()} · {l['hours']} H</p><h1>{esc(l['title'])}<span class="accent">.</span></h1><p class="lesson-objective">{esc(l['objective'])}</p>'''
 presentation=common+f'''<section id="apresentacao" class="lesson-content"><h2>Apresentação em preparação</h2><p>Os slides HTML desta aula serão publicados nesta página. Consulte o objetivo e as atividades previstas para acompanhar o planejamento.</p></section><a class="text-link" href="{l['activity']}">Abrir atividades</a>'''
 nav=f'<nav class="lesson-pagination" aria-label="Navegação entre aulas"><a href="index.html#aula-{n:02}">← Cronograma</a>'
 if n>1:nav+=f'<a href="aula-{n-1:02}.html">Aula anterior</a>'
 if n<60:nav+=f'<a href="aula-{n+1:02}.html">Próxima aula →</a>'
 nav+='</nav>'
 path=COURSE/l['presentation']
 if not path.exists():path.write_text(page(title,presentation+nav))
 tasks=''.join(f'<li>{esc(t)}</li>' for t in l['tasks'])
 activity=common+f'''<section class="lesson-content"><h2>{'Orientações para a avaliação' if n in [29,30,57,58] else 'Atividades propostas'}</h2><ol class="task-list">{tasks}</ol><h2>{'Instrumento' if n in [29,30,57,58] else 'Entrega esperada'}</h2><p>{esc(l['deliverable'])}</p>'''
 if n in [29,30,57,58]:activity+='<p>O enunciado e as condições da prova serão fornecidos pelo professor em sala. Esta página não contém questões nem gabarito.</p>'
 a=next((a for a in data['assessments'] if a['code']=={20:'T1',42:'T2',59:'T3',60:'T3'}.get(n)),None)
 if a:activity+=rubric(a)
 activity+=f'''</section><a class="text-link" href="{l['presentation']}">Voltar à apresentação</a>'''+nav
 path=COURSE/l['activity']
 if not path.exists():path.write_text(page(f'Atividades da aula {n:02}',activity))
print('Built course index; created missing presentation and activity pages without overwriting existing lessons.')
