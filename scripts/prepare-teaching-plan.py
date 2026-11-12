"""Preserve the institutional XLSX template and prepare its print layout for PDF export.

Usage: python3 scripts/prepare-teaching-plan.py /absolute/path/to/template.xlsx
The public XLSX retains the reference tabs and annexes. The temporary PDF copy
prints only the completed plan (A1:K73), omitting unused annexes and the status tab.
"""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import json,sys,copy
ROOT=Path(__file__).resolve().parents[1];COURSE=ROOT/'teaching/2027/1/network-services'
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main';ns={'s':NS}
source=Path(sys.argv[1]);target=COURSE/'plano-de-ensino.xlsx';data=json.loads((COURSE/'programa.json').read_text())
def read(path):
 with ZipFile(path) as z:parts={name:z.read(name) for name in z.namelist()}
 tree=E.fromstring(parts['xl/worksheets/sheet1.xml'])
 strings=[''.join(e.itertext()) for e in E.fromstring(parts['xl/sharedStrings.xml']).findall('s:si',ns)] if 'xl/sharedStrings.xml' in parts else []
 def value(addr):
  c=tree.find(f'.//s:c[@r="{addr}"]',ns)
  if c is None:return ''
  if c.get('t')=='inlineStr':return ''.join(c.find('s:is',ns).itertext())
  v=c.find('s:v',ns)
  if v is None:return ''
  return strings[int(v.text)] if c.get('t')=='s' else v.text
 return parts,tree,value
_,_,old=read(target)
updates={a:old(a) for a in ['B7','B12','B14','B15','A19','A21','A47','A57','A59']}
updates['B13']=2027
updates['A47']=data['metadata']['methodology']
parts,tree,value=read(source);sheetdata=tree.find('s:sheetData',ns)
def setcell(addr,value,formula=None):
 r=int(''.join(ch for ch in addr if ch.isdigit()));row=sheetdata.find(f's:row[@r="{r}"]',ns)
 if row is None:row=E.SubElement(sheetdata,f'{{{NS}}}row',r=str(r))
 c=row.find(f's:c[@r="{addr}"]',ns)
 if c is None:c=E.SubElement(row,f'{{{NS}}}c',r=addr)
 for ch in list(c):c.remove(ch)
 if isinstance(value,(int,float)):
  c.attrib.pop('t',None)
  if formula:E.SubElement(c,f'{{{NS}}}f').text=formula
  E.SubElement(c,f'{{{NS}}}v').text=str(value)
 else:
  c.set('t','inlineStr');E.SubElement(E.SubElement(c,f'{{{NS}}}is'),f'{{{NS}}}t').text=str(value)
 return c
def height(r,h):
 row=sheetdata.find(f's:row[@r="{r}"]',ns)
 if row is not None:row.set('ht',str(h));row.set('customHeight','1')
for addr,v in updates.items():setcell(addr,v)
# A:G describes one program item, H:I and J:K contain theory/practice hours.
for r in range(24,43):
 for col in ['A','H','J']:setcell(f'{col}{r}','')
 height(r,2)
for r,u in enumerate(data['units'],24):
 setcell(f'A{r}',f"Aulas {u['start']:02}-{u['end']:02}: {u['title']}")
 setcell(f'H{r}',u['theory']);setcell(f'J{r}',u['practice']);height(r,22)
note_row=24+len(data['units'])
setcell(f'A{note_row}','8 tópicos e 60 aulas, totalizando 72 horas. Datas e agrupamento dos encontros conforme o calendário.');height(note_row,28)
for rownum in range(note_row+1,43):sheetdata.find(f's:row[@r="{rownum}"]',ns).set('hidden','1')
setcell('H43',26,'SUM(H24:H42)');setcell('J43',46,'SUM(J24:J42)')
for r,code in enumerate(['P1','P2','T1','T2','T3'],50):
 a=next(a for a in data['assessments'] if a['code']==code)
 setcell(f'A{r}',f'{code} - {a["kind"]}');setcell(f'B{r}',a['title']);setcell(f'F{r}',a['points']);setcell(f'H{r}',f'Aulas {a["lessons"]}; data a definir');height(r,42 if code=='T3' else 34)
setcell('A55','TOTAL (proposta: 100 pontos)');setcell('B55','2 provas e 3 trabalhos');setcell('F55',100,'SUM(F50:F54)');setcell('H55','Datas a definir')
for r,h in [(15,18),(17,46),(19,38),(21,78),(44,18),(45,20),(46,18),(47,78),(48,18),(49,24),(55,28),(56,30),(57,36),(58,18),(59,36),(62,20),(63,28),(64,28),(65,40),(67,20),(68,22),(69,28),(70,28),(71,28),(72,28)]:height(r,h)
# Apply wrapping to the affected text cells, retaining each original font and borders.
styles=E.fromstring(parts['xl/styles.xml']);xfs=styles.find('s:cellXfs',ns)
clones={}
for addr in ['B15','A19','A21',f'A{note_row}','A47','A57','A59']+[f'{col}{r}' for col in ['A','B','H'] for r in range(50,56)]+[f'{col}{r}' for col in ['A','B','G'] for r in [63,64,65,68,69,70,71,72]]:
 c=tree.find(f'.//s:c[@r="{addr}"]',ns)
 if c is None:continue
 original_style=int(c.get('s','0'))
 # Filled narrative sections match the black text of the methodology section.
 if addr in ['A57','A59']:original_style=int(tree.find('.//s:c[@r="A47"]',ns).get('s','0'))
 if original_style not in clones:
  xf=copy.deepcopy(xfs[original_style]);align=xf.find('s:alignment',ns)
  if align is None:align=E.SubElement(xf,f'{{{NS}}}alignment')
  align.set('wrapText','1');align.set('vertical','center');xf.set('applyAlignment','1');clones[original_style]=len(xfs);xfs.append(xf)
 c.set('s',str(clones[original_style]))
xfs.set('count',str(len(xfs)));parts['xl/styles.xml']=E.tostring(styles,xml_declaration=True,encoding='UTF-8',standalone=True)
pr=tree.find('s:sheetPr',ns)
if pr is None:pr=E.Element(f'{{{NS}}}sheetPr');tree.insert(0,pr)
setup=pr.find('s:pageSetUpPr',ns)
if setup is None:setup=E.SubElement(pr,f'{{{NS}}}pageSetUpPr')
setup.set('fitToPage','1')
page=tree.find('s:pageSetup',ns);page.set('paperSize','9');page.set('orientation','landscape');page.set('fitToWidth','1');page.set('fitToHeight','0');page.attrib.pop('scale',None)
margins=tree.find('s:pageMargins',ns)
for key in ['left','right','top','bottom']:margins.set(key,'0.75')
# Manual page breaks keep each major section together.
existing=tree.find('s:rowBreaks',ns)
if existing is not None:tree.remove(existing)
breaks=E.Element(f'{{{NS}}}rowBreaks',count='3',manualBreakCount='3')
for row in [21,45,55]:E.SubElement(breaks,f'{{{NS}}}brk',id=str(row),min='0',max='16383',man='1')
# rowBreaks precede drawing elements in SpreadsheetML.
insert_at=next((i for i,e in enumerate(tree) if E.QName(e).localname in ['colBreaks','customProperties','cellWatches','ignoredErrors','smartTags','drawing','legacyDrawing','legacyDrawingHF','picture','oleObjects','controls','webPublishItems','tableParts','extLst']),len(tree))
tree.insert(insert_at,breaks)
workbook=E.fromstring(parts['xl/workbook.xml']);names=workbook.find('s:definedNames',ns)
if names is None:names=E.SubElement(workbook,f'{{{NS}}}definedNames')
for e in list(names):
 if e.get('name')=='_xlnm.Print_Area' and e.get('localSheetId')=='0':names.remove(e)
name=workbook.find('s:sheets/s:sheet',ns).get('name')
E.SubElement(names,f'{{{NS}}}definedName',name='_xlnm.Print_Area',localSheetId='0').text=f"'{name}'!$A$1:$K$73"
calc=workbook.find('s:calcPr',ns)
if calc is not None:calc.set('fullCalcOnLoad','1')
parts['xl/worksheets/sheet1.xml']=E.tostring(tree,xml_declaration=True,encoding='UTF-8',standalone=True)
parts['xl/workbook.xml']=E.tostring(workbook,xml_declaration=True,encoding='UTF-8',standalone=True)
def save(path,parts):
 with ZipFile(path,'w',ZIP_DEFLATED) as z:
  for name,content in parts.items():z.writestr(name,content)
save(target,parts)
for sheet in workbook.findall('s:sheets/s:sheet',ns)[1:]:sheet.set('state','hidden')
parts['xl/workbook.xml']=E.tostring(workbook,xml_declaration=True,encoding='UTF-8',standalone=True)
tmp=Path('/tmp/site-pt-plan');tmp.mkdir(exist_ok=True);save(tmp/'plano-de-ensino.xlsx',parts)
print('Prepared public template workbook and temporary print copy for native PDF conversion.')
