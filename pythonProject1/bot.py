import telebot
import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup
#from telebot from types
TOKEN = '7296036355:AAGPotHeuNO43_QyWtFeU3wMCqvteMLnmbE'
#avito="https://www.avito.ru/moskva/rabota"
bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'приветствую какую должность хотите найти?')
    bot.send_message(message.chat.id, 'можете ввести название профессии/зарплату/удалённо/полный рабочий день')
@bot.message_handler(content_types='text')
def tolk(message):
    #bot.send_message(message.chat.id, '/программист')
    #print(message.text)
    t4=message.text
    s1=0
    if (t4!='/start'):
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
                            s1=s1+1
                        t = ""
                        t1 = ""
                        h = ""
    #inf(t4,5,message)
                    #print("============")
        bot.send_message(message.chat.id, str(s1))

bot.polling(none_stop=True)





