import re,glob,collections,sys
ys=sys.argv[1].split(','); n=int(sys.argv[2])
def cnt(files):
    c=collections.Counter(); w=collections.defaultdict(collections.Counter)
    for f in files:
        for m in re.finditer(r'\\omterm\{([^}]*)\}\{([^{}]*)\}', open(f).read()): c[m.group(1)]+=1; w[m.group(1)][m.group(2)]+=1
    return c,w
zc,zw=cnt([f for y in ys for f in glob.glob(f'parts/{y}/zh/*.tex')+glob.glob(f'parts/{y}/solutions/zh/*.tex')])
ec,ew=cnt([f for y in ys for f in glob.glob(f'parts/{y}/*.tex')+glob.glob(f'parts/{y}/solutions/*.tex')])
print('zh',sum(zc.values()),len(zc),'en',sum(ec.values()),len(ec))
for k in sorted(zc, key=lambda k: -(zc[k]-ec.get(k,0)))[:n]:
    print(f"{zc[k]-ec.get(k,0):5d} {zc[k]:4d}/{ec.get(k,0):<4d} {k[:40]:40s} zh:{dict(zw[k].most_common(3))}  en:{dict(ew[k].most_common(2))}"[:190])
print('-- missing:', ', '.join(f'{k.split(":",2)[2]} {ec[k]}' for k in sorted(ec, key=lambda k:-ec[k]) if k not in zc)[:700])
