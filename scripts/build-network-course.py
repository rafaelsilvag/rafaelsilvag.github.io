"""Generate the topic index and missing material pages; preserve existing presentations."""
from pathlib import Path
from html import escape as esc
import json
from localize_site import localize_file
ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT/'teaching/2027/1/network-services'
data=json.loads((COURSE/'programa.json').read_text());meta=data['metadata']
def page(title,body):
 return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#0b1220"><meta name="description" content="{esc(title)} - Serviços de Redes para Internet, Sistemas de Informação, 2027/1."><title>{esc(title)} | Serviços de Redes para Internet</title><link rel="icon" href="../../../../assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../../../../assets/style.css"><link rel="stylesheet" href="disciplina.css"></head><body><a class="skip-link" href="#main">Pular para o conteúdo</a><header class="site-header"><div class="container header-inner"><a class="brand" href="../../../../index.html" aria-label="Rafael Silva Guimarães — início">rsg<span>.</span></a><nav aria-label="Navegação principal"><a href="../../../../index.html">Sobre</a><a href="../../../../publications.html">Publicações</a><a href="../../../../classes.html" aria-current="page">Aulas</a></nav></div></header><main id="main" class="container course-main" lang="pt-BR"><nav class="breadcrumbs" aria-label="Navegação estrutural"><a href="../../../../classes.html">Aulas</a><span aria-hidden="true">/</span><a href="index.html">Serviços de Redes para Internet</a><span aria-hidden="true">/</span><span>2027/1</span></nav>{body}</main><footer class="site-footer container"><p>Rafael Silva Guimarães<span class="footer-dot">·</span> Ifes, Brasil</p><a href="../../../../classes.html">Todas as disciplinas <span aria-hidden="true">↑</span></a></footer></body></html>\n'''
def save(name,body,preserve=False,title=None):
 path=COURSE/name
 if preserve and path.exists():return
 path.write_text(page(title or meta['title'],body));localize_file(path)
def rubric(a):
 return '<h2>Critérios de avaliação</h2><p>Distribuição de pontos proposta para esta avaliação.</p><ul>'+''.join(f'<li>{esc(label)}: {points} pontos.</li>' for label,points in a['criteria'])+f'</ul><p><strong>Total: {a["points"]} pontos.</strong> A participação individual será verificada na demonstração ou apresentação.</p>'
def aliases(start,end):return ''.join(f'<span id="aula-{i:02}" class="anchor-alias" aria-hidden="true"></span>' for i in range(start,end+1))
assessments=''.join(f'<tr><th scope="row">{a["code"]}</th><td>{esc(a["title"])}<small>{esc(a["kind"])}</small></td><td>{a["lessons"]}</td><td>{a["points"]}</td></tr>' for a in data['assessments'])
topics=''
for t in data['topics']:
 n=t['number'];subtopics=''.join(f'<li>{esc(s)}</li>' for s in t['subtopics'])
 topics+=f'''<li class="topic-card" id="topico-{n:02}" value="{n}">{aliases(t['start'],t['end'])}<div class="unit-heading"><h3>{esc(t['title'])}</h3><p>Aulas {t['start']}–{t['end']} · {t['theory']+t['practice']} h · {t['theory']} T / {t['practice']} P</p></div><ul class="topic-subtopics">{subtopics}</ul><div class="topic-actions"><a class="text-link" href="{t['presentation']}">Apresentação <span class="resource-note">Em preparação</span></a><a class="text-link secondary-action" href="{t['activity']}">Atividades do tópico</a></div></li>'''
rows=''.join(f'<tr><td>{u["start"]}–{u["end"]}</td><td>{esc(u["title"])}</td><td>{u["theory"]+u["practice"]} h</td></tr>' for u in data['units'])
refs=''.join(f'<li><a href="{r["url"]}" target="_blank" rel="noopener noreferrer">{esc(r["title"])} ↗</a></li>' for r in data['references'])
body=f'''<section class="course-hero"><p class="eyebrow">2027/1 · SISTEMAS DE INFORMAÇÃO</p><h1>Serviços de Redes para Internet<span class="accent">.</span></h1><p class="course-instructor">Professor: Rafael Silva Guimarães</p><p class="course-summary">Da conectividade IP à entrega de software: construção, integração e operação de serviços com Docker, Docker Compose e CI/CD.</p><div class="course-stats"><span><strong>10</strong> tópicos</span><span><strong>60</strong> aulas</span><span><strong>72 h</strong> carga horária total</span><span><strong>26 h / 46 h</strong> teóricas / práticas</span></div><p class="schedule-note">{esc(meta['durationNote'])}</p><div class="course-actions"><a class="text-link" href="plano-de-ensino.pdf">Plano de ensino (PDF)</a><a class="text-link secondary-action" href="plano-de-ensino.xlsx">Plano editável (XLSX)</a><a class="text-link secondary-action" href="#cronograma">Ver os tópicos ↓</a></div></section>
<section class="course-section"><h2>Um projeto, três etapas</h2><p>O projeto evolui em três entregas: containers e endereçamento (T1), serviços integrados com Compose (T2) e pipeline de CI/CD com monitoramento e recuperação (T3).</p></section>
<section class="course-section" id="cronograma"><p class="eyebrow">PERCURSO DE APRENDIZAGEM</p><h2>Tópicos da disciplina</h2><p>Cada tópico reúne até três subtópicos e possui sua própria apresentação e atividade. Os slides HTML serão publicados gradualmente.</p><ol class="topic-list">{topics}</ol></section>
<section class="course-section" id="avaliacoes">{aliases(29,30)}{aliases(57,58)}<h2>Avaliações</h2><p>{esc(meta['evaluationNote'])}</p><div class="table-scroll"><table><caption>Proposta de avaliações: 100 pontos</caption><thead><tr><th scope="col">Avaliação</th><th scope="col">Escopo</th><th scope="col">Aulas</th><th scope="col">Pontos</th></tr></thead><tbody>{assessments}</tbody></table></div><p class="schedule-note">Cada prova ocupa duas aulas e constitui uma única avaliação. As aulas 59 e 60 são duas sessões do mesmo T3. Datas a definir conforme o calendário acadêmico.</p><div class="course-actions"><a class="text-link secondary-action" href="atividade-29.html">Orientações da Prova 1</a><a class="text-link secondary-action" href="atividade-57.html">Orientações da Prova 2</a></div></section>
<section class="course-section"><h2>Distribuição das 60 aulas</h2><div class="table-scroll"><table><thead><tr><th scope="col">Aulas</th><th scope="col">Tópico ou avaliação</th><th scope="col">Carga horária</th></tr></thead><tbody>{rows}</tbody></table></div></section><section class="course-section course-references"><h2>Referências técnicas</h2><ul>{refs}</ul></section>'''
save('index.html',body)
for t in data['topics']:
 n=t['number'];title=f'Tópico {n:02} — {t["title"]}';subs=''.join(f'<li>{esc(s)}</li>' for s in t['subtopics'])
 common=f'<p class="eyebrow">TÓPICO {n:02} · AULAS {t["start"]}–{t["end"]} · {t["theory"]+t["practice"]} H</p><h1>{esc(t["title"])}<span class="accent">.</span></h1>'
 presentation=common+f'<section class="lesson-content"><h2>Apresentação em preparação</h2><p>Os slides HTML deste tópico serão disponibilizados nesta página.</p><ul>{subs}</ul></section><a class="text-link" href="{t["activity"]}">Atividades do tópico</a><nav class="lesson-pagination" aria-label="Navegação entre tópicos"><a href="index.html#topico-{n:02}">← Tópicos da disciplina</a></nav>'
 save(t['presentation'],presentation,preserve=True,title=title)
 tasks=''.join(f'<li>{esc(s)}</li>' for s in t['tasks'])
 activity=common+f'<section class="lesson-content"><h2>Atividades propostas</h2><ol>{tasks}</ol><h2>Entrega esperada</h2><p>{esc(t["deliverable"])}</p>'
 code={3:'T1',6:'T2',10:'T3'}.get(n)
 if code:activity+=rubric(next(a for a in data['assessments'] if a['code']==code))
 activity+=f'</section><a class="text-link" href="{t["presentation"]}">Voltar à apresentação</a><nav class="lesson-pagination" aria-label="Navegação entre tópicos"><a href="index.html#topico-{n:02}">← Tópicos da disciplina</a></nav>'
 save(t['activity'],activity,preserve=True,title=f'Atividades — {title}')
# Replace only the two explicitly removed introductory items in legacy URLs.
for l in data['lessons'][:2]:
 common=f'<p class="eyebrow">AULA {l["number"]:02}</p><h1>{esc(l["title"])}</h1><p>{esc(l["objective"])}</p>'
 save(l['presentation'],common+'<section class="lesson-content"><h2>Apresentação em preparação</h2><p>Este conteúdo integra o tópico de revisão TCP/IP.</p></section><a class="text-link" href="topico-01.html">Apresentação do tópico</a>',title=l['title'])
 save(l['activity'],common+'<section class="lesson-content"><h2>Atividades propostas</h2><ol>'+''.join(f'<li>{esc(s)}</li>' for s in l['tasks'])+'</ol><p>'+esc(l['deliverable'])+'</p></section><a class="text-link" href="atividade-topico-01.html">Atividades do tópico</a>',title=f'Atividades — {l["title"]}')
print('Course index organized in 10 topics with 20 presentation/activity links.')
