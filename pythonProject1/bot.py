import telebot
import requests
import psycopg2
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
from pymongo import MongoClient

mon = MongoClient(
    "mongodb+srv://Dragon4594:1242EefD933@cluster0.hyechba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
colection = mon.one_database.one_colection
#from telebot from types
TOKEN = '7296036355:AAGPotHeuNO43_QyWtFeU3wMCqvteMLnmbE'

'''def f(s):

        line=""
        for line in colection.find({"_id":  s}):
            return line'''



bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'приветствую какую должность хотите найти?')
    bot.send_message(message.chat.id, 'можете ввести название профессии/зарплату/удалённо/полный рабочий день')
@bot.message_handler(content_types='text')
def tolk(message):
    #bot.send_message(message.chat.id, '/программист')
    #print(message.text)
    file=open('v.txt','w',encoding="utf-8")
    t4=str(message.text)
    s1=0

    if ((t4!="/start")|(t4!="/+5")|(t4!="/-5")):
        bot.send_message(message.chat.id, 'пожалуйста подождите')
        n2=0

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
                            #updata(s1+t4,h,t,habr1+t1)
                            h5=str(s1)+t4
                            line=""
                            o=0
                            for line in colection.find({"_id": h5}):
                                o=o+1
                            if (line!=""):
                                colection.update_one({"_id":str(s1)+t4},{"$set": {"vakansii_name":h}})
                                colection.update_one({"_id": str(s1) + t4},{"$set": {"vakansii_zp":t}})
                                colection.update_one({"_id": str(s1) + t4},{"$set": {"vakansii_https":habr1+t1}})
                                #print("-")
                            if(line==""):
                                user = {
                                    "_id":str(s1)+t4,
                                    "idd": (s1),
                                    "namevakansii":t4,
                                    "vakansii_name": h,
                                    "vakansii_zp": t,
                                    "vakansii_https":habr1 + t1,
                                    "=======":"======="
                                }
                                #print("+")
                                colection.insert_one(user)

                            '''user = {
                                "_id": str(s1) + t4,
                                "idd": (s1),
                                "namevakansii": t4,
                                "vakansii_name": h,
                                "vakansii_zp": t,
                                "vakansii_https": habr1 + t1,
                                "=======": "======="
                            
                            }'''

                            bot.send_message(message.chat.id, h)
                            bot.send_message(message.chat.id, t)
                            bot.send_message(message.chat.id, habr1 + t1)
                            bot.send_message(message.chat.id, '===================')
                            s1=s1+1
                        t = ""
                        t1 = ""
                        h = ""
    #inf(t4,5,message)
        bot.send_message(message.chat.id, "найдено вакансий "+str(s1) +" по профессии "+t4)
                    #print("============")



bot.polling(none_stop=True)





