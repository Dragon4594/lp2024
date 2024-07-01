import telebot
import requests
from bs4 import BeautifulSoup
#from telebot from types
TOKEN = '7296036355:AAGPotHeuNO43_QyWtFeU3wMCqvteMLnmbE'
avito="https://www.avito.ru/moskva/rabota"
bot=telebot.TeleBot(TOKEN)
'''@bot.message_handler(comands=['start'])
def start(message):'''
@bot.message_handler(content_types='text')
def tolk(message):
    bot.send_message(message.chat.id, message.text)
    #print(message.text)
    t=message.text
    f=""
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
            f=f+"ju"

    е="https://hh.ru/vacancies/"+f
    #print("https://hh.ru/vacancies/"+f)
    print(requests.get("https://hh.ru/vacancies/"+f).text)
bot.polling(none_stop=True)


p=requests.get(avito).text

a=BeautifulSoup(p,'lxml')

#print(p)


