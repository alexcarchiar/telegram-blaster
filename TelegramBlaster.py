'''
TelegramBlaster by alexcarchiar, realized for BIT PoliTO
It's mostly just a script, don't take it as final code.
It will work, but you may need to adapt it.
If you have any problems, don't hesitate to contact me!
(visit alessandrochiarelli.com to find out how)

In order for it to work:
- get your api id and api hash from Telegram developer website
- write the username down in a csv file. In BIT PoliTO's case, we
    have Italian and International students, the rows are -Telegram ITA- and
    - Telegram ENG - : modify accordingly to your situation
- prepare your message: BIT PoliTO always has an italian version and an english version

You should import this file into an other and use it as a class
Remember that this is meant to be used with CLI! Telegram might ask you to log in the app!
I am not collecting any data, I'm just using Telethon. Read Telegram and Telethon documentation
if you have any concerns.

Check requirements.txt to install the required dependencies

As you can see, once you construct the class, it will immediately send all the texts.
It is not called blaster for nothign!
'''
import csv
from telethon import TelegramClient
import telethon

class TelegramBlaster():

    def __init__(self, api_id, api_hash, csv_path, message_ita='nessun_messaggio_inserito', message_eng='no_message_inserted'):
        self.api_hash = api_hash
        self.api_id = api_id
        self.csv_path = csv_path

        if message_ita=='nessun_messaggio_inserito':
            self.message_ita = input("Inserisci il messaggio in italiano (scrivi \\n per andare a capo)\n")
        else:
            self.message_ita = message_ita
        
        if message_eng=='no_message_inserted':
            self.message_eng = input("Insert your message in english (write \\n for new line)\n")
        else:
            self.message_eng = message_eng

        self.client = TelegramClient('anon', api_id, api_hash)
        with self.client:
            self.client.loop.run_until_complete(self.__main())

    def __make_list_ita(self):
        name_list = []
        with open(self.csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tag = row['Telegram ITA']
                if tag == '' or tag == '.': #removing invalid tags
                    continue
                else:
                    if(tag[0] == '@'): #removing the @ symbol
                        tag = tag[1:]
                    name_list.append(tag)
        return name_list

    def __make_list_eng(self):
            name_list = []
            with open(self.csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    tag = row['Telegram ENG']
                    if tag == '' or tag == '.': #removing invalid tags
                        continue
                    else:
                        if(tag[0] == '@'): #removing the @ symbol
                            tag = tag[1:]
                        name_list.append(tag)
            return name_list

    async def __main(self):
        users = self.__make_list_ita()
        for name in users:
            message = await self.client.send_message(
                name,
                self.message_ita,
                link_preview=False
            )

        users = self.__make_list_eng()
        for name in users:
            message = await self.client.send_message(
                name,
                self.message_eng,
                link_preview=False
            )

if __name__ == '__main__':
    api_id = input("Insert api id\n")
    api_hash = input("Insert api hash\n")
    csv_path = input("Insert csv path\n")
    TelegramBlaster(api_id, api_hash, csv_path)

