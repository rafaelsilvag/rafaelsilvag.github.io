"""Generate the topic index and missing material pages; preserve existing presentations."""
from pathlib import Path
from html import escape as esc
import json
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--refresh-materials",action="store_true",help="Regenerate the planned presentation and activity pages after a curriculum revision.")
args=parser.parse_args()
from localize_site import localize_file
ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT/'teaching/2027/1/network-services'
data=json.loads((COURSE/'programa.json').read_text());meta=data['metadata']
def page(title,body):
 return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#0b1220"><meta name="description" content="{esc(title)} - Serviços de Redes para Internet, Sistemas de Informação, 2027/1."><title>{esc(title)} | Serviços de Redes para Internet</title><link rel="icon" href="../../../../assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../../../../assets/style.css"><link rel="stylesheet" href="disciplina.css"></head><body><a class="skip-link" href="#main">Pular para o conteúdo</a><header class="site-header"><div class="container header-inner"><a class="brand" href="../../../../index.html" aria-label="Rafael Silva Guimarães — início">rsg<span>.</span></a><nav aria-label="Navegação principal"><a href="../../../../index.html">Sobre</a><a href="../../../../publications.html">Publicações</a><a href="../../../../classes.html" aria-current="page">Aulas</a></nav></div></header><main id="main" class="container course-main" lang="pt-BR"><nav class="breadcrumbs" aria-label="Navegação estrutural"><a href="../../../../classes.html">Aulas</a><span aria-hidden="true">/</span><a href="index.html">Serviços de Redes para Internet</a><span aria-hidden="true">/</span><span>2027/1</span></nav>{body}</main><footer class="site-footer container"><p>Rafael Silva Guimarães<span class="footer-dot">·</span> Ifes, Brasil</p><a href="../../../../classes.html">Todas as disciplinas <span aria-hidden="true">↑</span></a></footer></body></html>\n'''
def save(name,body,preserve=False,title=None):
 path=COURSE/name
 if preserve and path.exists() and not args.refresh_materials:return
 path.write_text(page(title or meta['title'],body));localize_file(path)
def rubric(a):
 return '<h2>Critérios de avaliação</h2><p>Distribuição de pontos proposta para esta avaliação.</p><ul>'+''.join(f'<li>{esc(label)}: {points} pontos.</li>' for label,points in a['criteria'])+f'</ul><p><strong>Total: {a["points"]} pontos.</strong> A participação individual será verificada na demonstração ou apresentação.</p>'
def aliases(start,end):return ''.join(f'<span id="aula-{i:02}" class="anchor-alias" aria-hidden="true"></span>' for i in range(start,end+1))
exam_units=[u for u in data['units'] if u['title'].startswith('Prova')]
exam_aliases=''.join(aliases(u['start'],u['end']) for u in exam_units)
assessments=''.join(f'<tr><th scope="row">{a["code"]}</th><td>{esc(a["title"])}<small>{esc(a["kind"])}</small></td><td>{a["lessons"]}</td><td>{a["points"]}</td></tr>' for a in data['assessments'])
topics=''
for t in data['topics']:
 n=t['number'];subtopics=''.join(f'<li>{esc(s)}</li>' for s in t['subtopics'])
 topics+=f'''<li class="topic-card" id="topico-{n:02}" value="{n}">{aliases(t['start'],t['end'])}<div class="unit-heading"><h3>{esc(t['title'])}</h3><p>Aulas {t['start']}–{t['end']} · {t['theory']+t['practice']} h · {t['theory']} T / {t['practice']} P</p></div><ul class="topic-subtopics">{subtopics}</ul><div class="topic-actions"><a class="text-link" href="{t['presentation']}">Apresentação <span class="resource-note">Em preparação</span></a><a class="text-link secondary-action" href="{t['activity']}">Atividades do tópico</a></div></li>'''
rows=''.join(f'<tr><td>{u["start"]}–{u["end"]}</td><td>{esc(u["title"])}</td><td>{u["theory"]+u["practice"]} h</td></tr>' for u in data['units'])
refs=''.join(f'<li><a href="{r["url"]}" target="_blank" rel="noopener noreferrer">{esc(r["title"])} ↗</a></li>' for r in data['references'])
body=f'''<section class="course-hero"><p class="eyebrow">2027/1 · SISTEMAS DE INFORMAÇÃO</p><h1>Serviços de Redes para Internet<span class="accent">.</span></h1><p class="course-instructor">Professor: Rafael Silva Guimarães</p><p class="course-summary">Da conectividade IP à entrega de software: construção, integração e operação de serviços com Docker, Docker Compose e CI/CD.</p><div class="course-stats"><span><strong>{len(data['topics'])}</strong> tópicos</span><span><strong>60</strong> aulas</span><span><strong>72 h</strong> carga horária total</span><span><strong>26 h / 46 h</strong> teóricas / práticas</span></div><p class="schedule-note">{esc(meta['durationNote'])}</p><div class="course-actions"><a class="text-link" href="plano-de-ensino.pdf">Plano de ensino (PDF)</a><a class="text-link secondary-action" href="plano-de-ensino.xlsx">Plano editável (XLSX)</a><a class="text-link secondary-action" href="#cronograma">Ver os tópicos ↓</a></div></section>
<section class="course-section"><h2>Um projeto, três etapas</h2><p>{esc(meta['projectDescription'])}</p><p>O mesmo projeto evolui em três marcos: T1 após Docker (aula 16), T2 após integrar os serviços (aula 38) e T3 no encerramento (aula 60), com CI/CD, monitoramento e documentação.</p></section>
<section class="course-section" id="cronograma"><p class="eyebrow">PERCURSO DE APRENDIZAGEM</p><h2>Tópicos da disciplina</h2><p>Cada tópico reúne até três subtópicos e possui sua própria apresentação e atividade. Os slides HTML serão publicados gradualmente.</p><ol class="topic-list">{topics}</ol></section>
<section class="course-section" id="avaliacoes">{exam_aliases}<h2>Avaliações</h2><p>{esc(meta['evaluationNote'])}</p><div class="table-scroll"><table><caption>Proposta de avaliações: 100 pontos</caption><thead><tr><th scope="col">Avaliação</th><th scope="col">Escopo</th><th scope="col">Aulas</th><th scope="col">Pontos</th></tr></thead><tbody>{assessments}</tbody></table></div><p class="schedule-note">Cada prova ocupa duas aulas e constitui uma única avaliação. {esc(meta['finalProjectNote'])} Datas a definir conforme o calendário acadêmico.</p><div class="course-actions"><a class="text-link secondary-action" href="atividade-25.html">Orientações da Prova 1</a><a class="text-link secondary-action" href="atividade-55.html">Orientações da Prova 2</a></div></section>
<section class="course-section"><h2>Distribuição das 60 aulas</h2><div class="table-scroll"><table><thead><tr><th scope="col">Aulas</th><th scope="col">Tópico ou avaliação</th><th scope="col">Carga horária</th></tr></thead><tbody>{rows}</tbody></table></div></section><section class="course-section course-references"><h2>Referências técnicas</h2><ul>{refs}</ul></section>'''
save('index.html',body)
for t in data['topics']:
 n=t['number'];title=f'Tópico {n:02} — {t["title"]}';subs=''.join(f'<li>{esc(s)}</li>' for s in t['subtopics'])
 common=f'<p class="eyebrow">TÓPICO {n:02} · AULAS {t["start"]}–{t["end"]} · {t["theory"]+t["practice"]} H</p><h1>{esc(t["title"])}<span class="accent">.</span></h1>'
 presentation=common+f'<section class="lesson-content"><h2>Apresentação em preparação</h2><p>Os slides HTML deste tópico serão disponibilizados nesta página.</p><ul>{subs}</ul></section><a class="text-link" href="{t["activity"]}">Atividades do tópico</a><nav class="lesson-pagination" aria-label="Navegação entre tópicos"><a href="index.html#topico-{n:02}">← Tópicos da disciplina</a></nav>'
 save(t['presentation'],presentation,preserve=True,title=title)
 tasks=''.join(f'<li>{esc(s)}</li>' for s in t['tasks'])
 activity=common+f'<section class="lesson-content"><h2>Atividades propostas</h2><ol>{tasks}</ol><h2>Entrega esperada</h2><p>{esc(t["deliverable"])}</p>'
 code={2:'T1',5:'T2',8:'T3'}.get(n)
 if code:activity+=rubric(next(a for a in data['assessments'] if a['code']==code))
 activity+=f'</section><a class="text-link" href="{t["presentation"]}">Voltar à apresentação</a><nav class="lesson-pagination" aria-label="Navegação entre tópicos"><a href="index.html#topico-{n:02}">← Tópicos da disciplina</a></nav>'
 save(t['activity'],activity,preserve=True,title=f'Atividades — {title}')
# Keep individually numbered lesson URLs consistent with the revised curriculum.
for l in data['lessons']:
 n=l['number'];topic=next((t for t in data['topics'] if t['start']<=n<=t['end']),None)
 common=f'<p class="eyebrow">AULA {n:02} · {l["type"].upper()} · {l["hours"]} H</p><h1>{esc(l["title"])}</h1><p class="lesson-objective">{esc(l["objective"])}</p>'
 back=f'<nav class="lesson-pagination" aria-label="Navegação entre aulas"><a href="index.html#aula-{n:02}">← Planejamento da disciplina</a>'
 if topic:back+=f'<a href="{topic["presentation"]}">Apresentação do tópico</a><a href="{topic["activity"]}">Atividades do tópico</a>'
 back+='</nav>'
 presentation=common+'<section class="lesson-content"><h2>Apresentação em preparação</h2><p>O conteúdo desta aula integra o roteiro do tópico correspondente. Os slides HTML serão publicados na apresentação do tópico.</p></section>'+f'<a class="text-link" href="{l["activity"]}">Abrir atividades</a>'+back
 save(l['presentation'],presentation,preserve=True,title=f'Aula {n:02} — {l["title"]}')
 exam=topic is None
 tasks=''.join(f'<li>{esc(task)}</li>' for task in l['tasks'])
 activity=common+f'<section class="lesson-content"><h2>{"Orientações para a avaliação" if exam else "Atividades propostas"}</h2><ol>{tasks}</ol><h2>{"Instrumento" if exam else "Entrega esperada"}</h2><p>{esc(l["deliverable"])}</p>'
 if exam:activity+='<p>O enunciado e as condições da prova serão fornecidos pelo professor em sala. As duas aulas indicadas pertencem à mesma avaliação.</p>'
 code='T1' if n==16 else 'T2' if n==38 else 'T3' if 57<=n<=60 else None
 if code:activity+=rubric(next(a for a in data['assessments'] if a['code']==code))
 if code=='T3':activity+=f'<p>{esc(meta["finalProjectNote"])}</p>'
 activity+='</section>'+back
 save(l['activity'],activity,preserve=True,title=f'Atividades da aula {n:02} — {l["title"]}')
# Retain previously published topic URLs without presenting obsolete schedules.
for old,new in [(9,7),(10,8)]:
 topic=data['topics'][new-1]
 for activity in [False,True]:
  target=topic['activity'] if activity else topic['presentation']
  old_name=f'atividade-topico-{old:02}.html' if activity else f'topico-{old:02}.html'
  save(old_name,f'<h1>{esc(topic["title"])}</h1><p>Este material está organizado no tópico {new} do planejamento atualizado.</p><a class="text-link" href="{target}">Acessar o material atualizado</a>',title=topic['title'])
print(f'Course index organized in {len(data["topics"])} topics; lesson URLs and assessment scopes synchronized.')
