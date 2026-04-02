io.py

#f = open("irem2.txt", "x") #dosya oluşturma
dizi=[]
with open("irem.txt", 'r', encoding='utf-8') as f:
 a=f.readline
 dizi.append(a)
 b = f.readline()
 dizi.append(b)
 c = f.readline()
 dizi.append(c)
 d = f.readline()
 dizi.append(d)
ydizi=[]
for i in dizi:
    son=i.split(' ')
    k=(son[0])
    m=(son[1])
    x=(son)[2]
    n=(x[1:])
    y=(son)[3]
    yy=y[0:5]
    print(yy)
    dizilim='{} {} {}$'.format(k,m,n,yy)
    ydizi.append(dizilim)
    with open("irem2.txt", 'a',encoding='utf-8') as f:
        print(print())
        print()
