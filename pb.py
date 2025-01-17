import sys
try:
 with open(sys.argv[1]) as f:
  c=f.read();o=[];i=0;s='    '
  for line in c.splitlines():
   l=line.strip();p=[];t=''
   for b in l:
    if b in "{}":
     if t:p.append(t);t=''
     p.append(b)
    else:t+=b
   if t: p.append(t)
   for a in p:
    a=a.strip().replace(';','\n'+s*i)
    if a=='}':i-=1;continue
    if a=='{':o[-1]+=':';i+=1;continue
    if a:o.append(f'{s * i}{a}')
  with open(sys.argv[2], 'w') as w: w.write('\n'.join(o))
except: print('Usage: python3 pb.py input.pb output.py')
