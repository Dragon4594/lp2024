import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
for t5 in range(70):
    '''params={
        "page" : str(t5),
        "q" : " программист"
    }
    #avito="https://www.avito.ru/moskva/rabota/"
    habr1="https://career.habr.com/"
    habr="https://career.habr.com/vacancies"
    #p=requests.get(avito).text
    p=requests.get(habr, params=params)
    a=BeautifulSoup(p.text,'lxml')
    bloc = a.find_all('div','section-box')
    bloc1 = a.find_all('div','/vacancies/')
    #print (bloc[1])
    #print("-------")

    t=""
    t1=""
    h=""
    r=False
    for i in range(1,len(bloc)):
        s=str(bloc[i])
        t2=0
        for g in range(1,len(s)):
            if ((s[g]=='₽')):
                for z in range(0,g):
                    if ((s[z]=='/')&(s[z+1]=='v')):
                        t2=t2+1
                        if (t2==2):
                            t2=0
                            for f in range(z,z+50):
                                if (t2==0):
                                    if (s[f]!='"'):
                                        t1=t1+s[f]
                                    if (s[f]=='"'):
                                        t2=1
                                if (t2==1):
                                    if (s[f+1]!='<')&(s[f+1]!='>'):
                                        h=h+s[f+1]
                                    if (s[f + 1] == '<'):
                                        t2=2

                    #print(z)

                for n in range(g-25,g+1):

                    if (s[n-1]==">"):
                        r=True
                    if (r):
                        t=t+s[n]
                r=False
                if ((requests.get(habr1+t1).status_code)!=404):
                    print(h)
                    print(t)
                    print(habr1+t1)
                    print(requests.get(habr1+t1).status_code)
                #print((requests.get(habr1+t1).status_code))
                t=""
                t1=""
                h=""
                print("============")'''
    params = { "p": str(t5),
                "q":"программист"}
    avito="https://www.avito.ru/moskva/rabota"
    p1 = requests.get(avito, params=params)
    a1 = BeautifulSoup(p1.text, 'lxml')
    bloc1 = a1.find('div')
    print(bloc1)
    print(p1.status_code)

#html = BS(p.content, 'html.parser')
#for el in html.select(".items-items-kAJAgr>."):
#    title = el.select
#print(p.text)