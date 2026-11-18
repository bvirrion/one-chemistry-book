import re,sys,glob
known=set()
files=sorted(glob.glob('../one-physics-book/sources/GLOSSARY_BOOK_*_ZH.md'))+[f'sources/GLOSSARY_BOOK_{b}_ZH.md' for b in sys.argv[1].split(',') if b]
for f in files:
    for l in open(f):
        m=re.match(r'\d\d \| (.*?) \| ',l)
        if m: known|={x.strip().lower() for x in m.group(1).split(' / ')}
tot=0
for y in sys.argv[2:]:
    out=[]
    for l in open(f'draft/zh/terms-{y}.txt'):
        ch,t=l.rstrip('\n').split(' | ',1)
        if t.lower() not in known and len(t)>2: out.append(t); known.add(t.lower())
    tot+=len(out); print(f'## {y} ({len(out)}): '+'; '.join(out))
print('total',tot)
