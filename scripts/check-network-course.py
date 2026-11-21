"""Check curriculum totals, generated material links and the current teaching plan."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
from bs4 import BeautifulSoup
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / 'teaching/2027/1/network-services'
data = json.loads((COURSE / 'programa.json').read_text())
assert len(data['topics']) == 8 and len(data['lessons']) == 60
assert sum(l['hours'] for l in data['lessons']) == 72
assert sum(l['hours'] for l in data['lessons'] if l['type'] == 'Teórica') == 26
assert sum(l['hours'] for l in data['lessons'] if l['type'] == 'Prática') == 46
assert [t['title'] for t in data['topics'][1:4]] == [
    'Serviços HTTP e DNS', 'Docker e execução de serviços', 'Docker Compose e integração de serviços']
assert sorted(n for u in data['units'] for n in range(u['start'], u['end'] + 1)) == list(range(1, 61))
assessments = {a['code']: a for a in data['assessments']}
assert assessments['T1']['lessons'] == '24'
assert assessments['P1']['lessons'] == '25 e 26' and 'Compose' not in assessments['P1']['title']
assert sum(a['points'] for a in data['assessments']) == 100
assert all(sum(points for _, points in a['criteria']) == a['points'] for a in data['assessments'])
video_count = 0
for topic in data['topics']:
    assert len(topic['subtopics']) <= 3
    for filename in [topic['presentation'], topic['activity']]:
        page = BeautifulSoup((COURSE / filename).read_text(), 'html.parser')
        assert topic['title'] in page.h1.get_text(), filename
    presentation = BeautifulSoup((COURSE / topic['presentation']).read_text(), 'html.parser')
    assert len(presentation.select('video')) == len(topic.get('videos', []))
    for video in topic.get('videos', []):
        assert (ROOT / 'videos' / video['file']).is_file()
        player = presentation.find('source', src='../../../../videos/' + video['file']).parent
        assert player.has_attr('controls') and player.get('preload') == 'none'
        video_count += 1
assert video_count == 4
for lesson in data['lessons']:
    for filename in [lesson['presentation'], lesson['activity']]:
        assert lesson['title'] in BeautifulSoup((COURSE / filename).read_text(), 'html.parser').h1.get_text()
for filename in ['index.html', 'atividade-topico-01.html', 'atividade-60.html']:
    page = BeautifulSoup((COURSE / filename).read_text(), 'html.parser')
    assert page.find('a', href=data['metadata']['codeRepository']), filename
references = 0
for filename in ROOT.rglob('*.html'):
    page = BeautifulSoup(filename.read_text(), 'html.parser')
    ids = [e['id'] for e in page.select('[id]')]
    assert len(ids) == len(set(ids)), filename
    for element in page.select('a[href],link[href],img[src],script[src],source[src]'):
        url = urlsplit(element.get('href', element.get('src')))
        assert 'plano-de-ensino.xlsx' not in url.path, (filename, url.path)
        if url.scheme or url.netloc:
            continue
        target = (filename.parent / unquote(url.path)).resolve() if url.path else filename
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), (filename, target)
        if url.fragment:
            assert BeautifulSoup(target.read_text(), 'html.parser').find(id=url.fragment), (filename, url.fragment)
        references += 1
assert not (COURSE / 'plano-de-ensino.xlsx').exists(), 'Somente o PDF deve ser publicado.'
pdf = PdfReader(COURSE / 'plano-de-ensino.pdf')
assert len(pdf.pages) == 4
text = ' '.join(' '.join(p.extract_text().split()) for p in pdf.pages)
assert text.index('Serviços HTTP e DNS') < text.index('Docker e execução de serviços')
assert 'Aulas 24' in text and 'TOTAL' in text
print(f'OK: 8 tópicos, 60 aulas, 72 horas, 4 vídeos, código em sala e {references} referências locais.')
