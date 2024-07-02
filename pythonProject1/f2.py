import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
params={
    "q" : " программист"
}
#avito="https://www.avito.ru/moskva/rabota/"
habr="https://career.habr.com/vacancies"
#p=requests.get(avito).text
p=requests.get(habr, params=params)
a=BeautifulSoup(p.text,'lxml')
bloc = a.find_all('div','section-box','Программист')
bloc1 = a.find_all('div','/vacancies/')
print (bloc)
print("=======================")
print(bloc1)
print(p.status_code)
#html = BS(p.content, 'html.parser')
#for el in html.select(".items-items-kAJAgr>."):
#    title = el.select
#print(p.text)