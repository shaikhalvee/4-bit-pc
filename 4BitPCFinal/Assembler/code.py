import sys

f=open('source.txt','r')
SOURCE=[ row[:-1] for row in f.readlines() ]

mapping={}

for i in range(len(SOURCE)):
	raw=SOURCE[i].split()
	mapping[raw[0]]=(hex(int(i)),len(raw)-1)

b=0
for line in sys.stdin:
	line=line.strip()
	if(b==2):
		print(hex(int(line)).replace('0x',''))
		b=0
	else:
		a,b=mapping[line]
		print(a.replace('0x',''))
