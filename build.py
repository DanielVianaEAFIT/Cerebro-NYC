"""Build offline metadata and a public-data dashboard from first-delivery workbook. Python standard library only."""
import zipfile,xml.etree.ElementTree as ET,json,pathlib,sys,datetime
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'Diccionario.xlsx');out=pathlib.Path(__file__).parent
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(p) as z:
 ss=[''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
 def rows(sheet):
  root=ET.fromstring(z.read(f'xl/worksheets/sheet{sheet}.xml'))
  for r in root.findall('.//m:sheetData/m:row',ns):
   d={}
   for c in r.findall('m:c',ns):
    col=''.join(k for k in c.attrib['r'] if k.isalpha());v=c.find('m:v',ns)
    if v is not None:d[col]=ss[int(v.text)] if c.attrib.get('t')=='s' else v.text
   yield d
 source=list(rows(2)); headers=source[2]; data=[]
 for r in source[4:]:
  if r.get('A','').startswith('F'):
   data.append({headers.get(k,k):v for k,v in r.items()})
 (out/'fuentes.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
 print('Fuentes registradas:',len(data));print('Integradas:',sum('Integrada' in x.get('Estado','') for x in data))
