"""Apply Portuguese defaults and a persistent English language switch to site pages."""
from pathlib import Path
from bs4 import BeautifulSoup,Comment,NavigableString
import json
ROOT=Path(__file__).resolve().parents[1]
# Each pair is Portuguese / English. Teaching materials retain their instructional language.
PAIRS={
'about':('Sobre','About'),'publications':('Publicações','Publications'),'classes':('Aulas','Classes'),
'skip':('Pular para o conteúdo','Skip to content'),'navigation':('Navegação principal','Main navigation'),'home':('Rafael Silva Guimarães — início','Rafael Silva Guimarães — home'),
'profiles':('Perfis profissionais','Professional profiles'),'researchInterests':('Interesses de pesquisa','Research interests'),'breadcrumb':('Navegação estrutural','Breadcrumb'),
'heroEyebrow':('PESQUISA · ENSINO · REDES','RESEARCH · TEACHING · NETWORKS'),'role':('Professor e pesquisador','Professor & researcher'),
'bio':('Atuo na interseção entre redes de computadores, pesquisa e educação. Meus interesses incluem redes definidas por software, Internet do futuro, Internet das Coisas e redes de data centers.','I work at the intersection of computer networks, research, and education. My interests include software-defined networking, the Internet of the future, IoT, and data center networks.'),
'location':('Cachoeiro de Itapemirim, Brasil','Cachoeiro de Itapemirim, Brazil'),'footerLocation':('Ifes, Brasil','Ifes, Brazil'),
'researchLabel':('INTERESSES DE PESQUISA','RESEARCH INTERESTS'),'sdn':('Redes definidas por software','Software-defined networking'),'futureInternet':('Internet do futuro','Internet of the future'),'iot':('Internet das Coisas','Internet of Things'),'dataCenters':('Redes de data centers','Data center networks'),
'backTop':('Voltar ao topo','Back to top'),'backHome':('Voltar ao início','Back to home'),'allClasses':('Todas as disciplinas','All classes'),
'research':('PESQUISA','RESEARCH'),'selectedPublications':('Publicações selecionadas','Selected publications'),'allPublications':('Todas as publicações','All publications'),
'publicationNote':('Para consultar a lista completa de publicações e as citações, acesse','For the complete publication list and citation information, visit'),
'classroom':('EM SALA DE AULA','IN THE CLASSROOM'),'learningMaterials':('Disciplinas e materiais de estudo','Courses & learning materials'),'academicYear':('ANO LETIVO','ACADEMIC YEAR'),'semester':('1º semestre','Semester 1'),
'integrated':('ENSINO TÉCNICO INTEGRADO','INTEGRATED TECHNICAL EDUCATION'),'undergraduate':('GRADUAÇÃO','UNDERGRADUATE'),
'internetProgram':('Informática para Internet · Curso Técnico Integrado','Internet Informatics · Integrated Technical Program'),
'informationSystems':('Bacharelado em Sistemas de Informação','Bachelor’s Degree in Information Systems'),
'fullInternetProgram':('Curso Técnico em Informática para Internet Integrado ao Ensino Médio','Integrated Technical Program in Internet Informatics'),
'materialsSoon':('Materiais em preparação','Materials coming soon'),'courseStatus':('8 tópicos · 60 aulas · 72 horas · Plano e atividades','8 topics · 60 classes · 72 hours · Course plan & activities'),
'courseResources':('MATERIAIS DA DISCIPLINA','COURSE RESOURCES'),'learningTitle':('Aprender, explorar e praticar.','A place to learn, explore & practice.'),
'resourcesDescription':('As apresentações, atividades e demais materiais serão publicados aqui conforme forem disponibilizados.','Lecture notes, activities, and course resources will be published here as they become available.'),
'instructor':('Professor: Rafael Silva Guimarães','Instructor: Rafael Silva Guimarães'),
'photo':('Foto de Rafael Silva Guimarães em seu perfil do GitHub','Portrait of Rafael Silva Guimarães from his GitHub profile'),
'aboutTitle':('Sobre | Rafael Silva Guimarães','About | Rafael Silva Guimarães'),
'publicationsTitle':('Publicações | Rafael Silva Guimarães','Publications | Rafael Silva Guimarães'),
'classesTitle':('Aulas | Rafael Silva Guimarães','Classes | Rafael Silva Guimarães'),
'aboutDescription':('Sobre Rafael Silva Guimarães, professor e pesquisador do Ifes: redes de computadores, educação e perfis profissionais.','About Rafael Silva Guimarães at Ifes: computer networks research, education, and professional profiles.'),
'publicationsDescription':('Publicações selecionadas de Rafael Silva Guimarães e acesso à lista completa no Google Scholar.','Selected publications by Rafael Silva Guimarães and links to the complete publication list on Google Scholar.'),
'classesDescription':('Disciplinas de Rafael Silva Guimarães organizadas por ano e semestre, com materiais de estudo.','Classes taught by Rafael Silva Guimarães, organized by academic year and semester, with links to course materials.'),
'computerNetworksDescription':('Redes de Computadores II, 1º semestre de 2027. Curso Técnico Integrado em Informática para Internet. Informações e materiais da disciplina.','Redes de Computadores II, semester 1 of 2027. Integrated Technical Program in Internet Informatics. Course information and learning materials.'),
'materialsLanguage':('Os nomes das disciplinas e os materiais didáticos são apresentados em português.','Course names and teaching materials are provided in Portuguese.'),
}
ALIASES={text:key for key,pair in PAIRS.items() for text in pair}
ALIASES['60 classes · 72 hours · Course plan & activities']='courseStatus'
def localize_file(path):
 path=Path(path);s=BeautifulSoup(path.read_text(),'html.parser')
 s.html['lang']='pt-BR'
 # Visible text nodes are wrapped separately so icons, links and proper publication titles survive switching.
 for node in list(s.find_all(string=True)):
  if isinstance(node,Comment) or node.parent.name in ['script','style','title']:continue
  if node.parent.find_parent(attrs={'data-i18n':True}) or node.parent.has_attr('data-i18n'):continue
  stripped=str(node).strip();key=ALIASES.get(stripped)
  if not key:continue
  span=s.new_tag('span',attrs={'data-i18n':key});span.string=PAIRS[key][0]
  leading=str(node)[:len(str(node))-len(str(node).lstrip())];trailing=str(node)[len(str(node).rstrip()):]
  node.replace_with(span)
  if leading:span.insert_before(leading)
  if trailing:span.insert_after(trailing)
 for tag in s.find_all(True):
  for attr in ['aria-label','alt']:
   if tag.has_attr(attr) and tag[attr] in ALIASES:
    key=ALIASES[tag[attr]];tag['data-i18n-'+attr]=key;tag[attr]=PAIRS[key][0]
 css=next(tag for tag in s.select('link[rel="stylesheet"]') if tag['href'].endswith('assets/style.css'))
 base=css['href'].removesuffix('style.css')
 if path.parent==ROOT:
  key={'index.html':'about','publications.html':'publications','classes.html':'classes'}.get(path.name)
  if key:
   s.title['data-i18n']=key+'Title';s.title.string=PAIRS[key+'Title'][0]
   description=s.select_one('meta[name="description"]');description['data-i18n-content']=key+'Description';description['content']=PAIRS[key+'Description'][0]
 elif path.parent.name=='computer-networks-ii':
  desc=s.select_one('meta[name="description"]');desc['data-i18n-content']='computerNetworksDescription';desc['content']=PAIRS['computerNetworksDescription'][0]
 if path.parent!=ROOT:
  main=s.select_one('main');main['lang']='pt-BR'
  if not s.select_one('.materials-language-note'):
   note=s.new_tag('p',attrs={'class':'materials-language-note','data-i18n':'materialsLanguage','lang':'en','hidden':True})
   note.string=PAIRS['materialsLanguage'][0]
   breadcrumbs=s.select_one('.breadcrumbs')
   if breadcrumbs:breadcrumbs.insert_after(note)
 if not s.select_one('.language-switch'):
  switch=s.new_tag('div',attrs={'class':'language-switch','role':'group','aria-label':'Idioma / Language'})
  for lang,label in [('pt-BR','Português'),('en','English')]:
   button=s.new_tag('button',attrs={'type':'button','data-language':lang,'lang':lang,'aria-pressed':'true' if lang=='pt-BR' else 'false'})
   button.string=label;switch.append(button)
  s.select_one('.header-inner').append(switch)
 if not s.select_one('script[data-site-i18n]'):
  script=s.new_tag('script',src=base+'i18n.js',attrs={'defer':True,'data-site-i18n':True});s.head.append(script)
 for article in s.select('.publication h3,.publication .venue'):article['lang']='en'
 for tag in s.select('[data-i18n]'):
  if tag['data-i18n'] in PAIRS:tag.string=PAIRS[tag['data-i18n']][0]
 path.write_text(str(s).rstrip()+'\n')
def build_runtime():
 catalogs={lang:{key:pair[i] for key,pair in PAIRS.items()} for i,lang in enumerate(['pt-BR','en'])}
 runtime='''
(() => {
  const supported = ['pt-BR', 'en'];
  const normalize = value => value === 'pt' ? 'pt-BR' : value;
  function applyLanguage(language) {
    const strings = translations[language];
    document.documentElement.lang = language;
    document.querySelectorAll('[data-i18n]').forEach(element => {
      const value = strings[element.dataset.i18n];
      if (value !== undefined) element.textContent = value;
    });
    ['aria-label', 'alt', 'content'].forEach(attribute => {
      document.querySelectorAll(`[data-i18n-${attribute}]`).forEach(element => {
        const value = strings[element.getAttribute(`data-i18n-${attribute}`)];
        if (value !== undefined) element.setAttribute(attribute, value);
      });
    });
    document.querySelectorAll('[data-language]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.language === language));
    });
    document.querySelectorAll('.materials-language-note').forEach(note => {
      note.hidden = language !== 'en';
    });
  }
  let saved = null;
  try { saved = localStorage.getItem('site-language'); } catch (_) {}
  const requested = normalize(new URL(location.href).searchParams.get('lang'));
  const language = supported.includes(requested) ? requested : supported.includes(saved) ? saved : 'pt-BR';
  applyLanguage(language);
  // Carry an explicit language through internal navigation even when storage is blocked.
  function updateLinks(language) {
    document.querySelectorAll('a[href]').forEach(link => {
      const raw = link.getAttribute('href');
      if (!raw || raw.startsWith('#')) return;
      const url = new URL(raw, location.href);
      if (url.origin !== location.origin || !(/\\.html$/.test(url.pathname) || url.pathname.endsWith('/'))) return;
      url.searchParams.set('lang', language);
      link.href = url.href;
    });
  }
  updateLinks(language);
  document.querySelectorAll('[data-language]').forEach(button => {
    button.addEventListener('click', () => {
      const selected = button.dataset.language;
      if (!supported.includes(selected)) return;
      applyLanguage(selected);
      updateLinks(selected);
      try { localStorage.setItem('site-language', selected); } catch (_) {}
      const url = new URL(location.href);
      url.searchParams.set('lang', selected);
      try { history.replaceState(null, '', url); } catch (_) {}
    });
  });
})();
'''
 (ROOT/'assets/i18n.js').write_text('// Generated by scripts/localize_site.py.\nconst translations = '+json.dumps(catalogs,ensure_ascii=False,indent=2)+';\n'+runtime)
if __name__=='__main__':
 build_runtime()
 for path in ROOT.rglob('*.html'):localize_file(path)
 print('Portuguese defaults and Portuguese/English switch applied to all HTML pages.')
