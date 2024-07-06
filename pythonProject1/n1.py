import psycopg2
from pymongo import MongoClient
import pymongo
mon = MongoClient("mongodb+srv://Dragon4594:1242EefD933@cluster0.hyechba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
colection = mon.one_database.one_colection
'''user = {
    "_id": "33g",
    "iddd" : "3"
}
colection.insert_one(user)'''

def i(s):
    for l in colection.find({"_id":  s}):
        return l
print(i("33g")!="None")
print("----")
c={"_id": "33g"}
c1={"$set": {"iddd": "4"}}
colection.update_one(c,c1)
print("===")
print(i("33g"))
l=""
for l in colection.find({"_id":  "33g"}):
    print("+")
    print(l)
print(l=="")
for i in range(2):
    for i1 in range(2):
        print(i|i1)
'''f=""
    for i in range(0,len(t)):
        if (t[i]=='а'):
            f=f+"a"
        if (t[i]=='б'):
            f=f+"b"
        if (t[i]=='в'):
            f=f+"v"
        if (t[i]=='г'):
            f=f+"g"
        if (t[i]=='д'):
            f=f+"d"
        if (t[i]=='e'):
            f=f+"e"
        if (t[i]=='ё'):
            f=f+"yo"
        if (t[i]=='ж'):
            f=f+"zh"
        if (t[i]=='з'):
            f=f+"z"
        if (t[i]=='и'):
            f=f+"i"
        if (t[i]=='й'):
            f=f+"y"
        if (t[i]=='к'):
            f=f+"k"
        if (t[i]=='л'):
            f=f+"l"
        if (t[i]=='м'):
            f=f+"m"
        if (t[i]=='н'):
            f=f+"n"
        if (t[i]=='о'):
            f=f+"o"
        if (t[i]=='п'):
            f=f+"p"
        if (t[i]=='р'):
            f=f+"r"
        if (t[i]=='с'):
            f=f+"s"
        if (t[i]=='т'):
            f=f+"t"
        if (t[i]=='у'):
            f=f+"u"
        if (t[i]=='ф'):
            f=f+"f"
        if (t[i]=='х'):
            f=f+"kh"
        if (t[i]=='ц'):
            f=f+"c"
        if (t[i]=='ч'):
            f=f+"ch"
        if (t[i]=='ш'):
            f=f+"sh"
        if (t[i]=='ы'):
            f=f+"y"
        if (t[i]=='я'):
            f=f+"ja"
        if (t[i]=='ю'):
            f=f+"ju"'''
'''def inf(t4,m,message):
    for t5 in range(5):
        params = {
            "page": str(t5),
            "q": t4
        }
        # avito="https://www.avito.ru/moskva/rabota/"
        habr1 = "https://career.habr.com"
        habr = "https://career.habr.com/vacancies"
        # p=requests.get(avito).text
        p = requests.get(habr, params=params)
        a = BeautifulSoup(p.text, 'lxml')
        bloc = a.find_all('div', 'section-box', )
        #bloc1 = a.find_all('div', '/vacancies/')
        # print (bloc[1])
        # print("-------")

        # for i in range(0,len(bloc)):
        t = ""
        t1 = ""
        h = ""
        r = False
        for i in range(1, len(bloc)):
            s = str(bloc[i])
            t2 = 0
            for g in range(1, len(s)):
                if ((s[g] == '₽')):
                    for z in range(0, g):
                        if ((s[z] == '/') & (s[z + 1] == 'v')):
                            t2 = t2 + 1
                            if (t2 == 2):
                                t2 = 0
                                for f in range(z, z + 50):
                                    if (t2 == 0):
                                        if (s[f] != '"'):
                                            t1 = t1 + s[f]
                                        if (s[f] == '"'):
                                            t2 = 1
                                    if (t2 == 1):
                                        if (s[f + 1] != '<') & (s[f + 1] != '>'):
                                            h = h + s[f + 1]
                                        if (s[f + 1] == '<'):
                                            t2 = 2

                        # print(z)

                    for n in range(g - 25, g + 1):

                        if (s[n - 1] == ">"):
                            r = True
                        if (r):
                            t = t + s[n]
                    r = False
                    if ((requests.get(habr1 + t1).status_code) != 404):
                        #print(h)
                        #print(t)
                        #print(habr1 + t1)
                        bot.send_message(message.chat.id, h)
                        bot.send_message(message.chat.id, t)
                        bot.send_message(message.chat.id, habr1 + t1)
                        bot.send_message(message.chat.id, '===================')
                        m=m-1
                    t = ""
                    t1 = ""
                    h = ""
                    if (m==0):
                        return 0'''
'''host ="127.0.0.1"
user ="postgres"
password = "1242EefD933"
db_name = "Databases(1)"
port = "5432"
connection = psycopg2.connect(
    database="rasp_bd",
    user="postgres",
    password="1242EefD933",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
cursor.execute(
    "SELECT version();"
)
print(f"Server version: {cursor.fetchone()}")'''