# TelegramBlaster
TelegramBlaster is a small python script that I created for my students' team in order to send telegram messages to all contacts in a csv form. Customize it as you wish!

Initially created for sending recruitment follow-up emails for [BIT PoliTO](https://github.com/BITPoliTO) team, can be easily modified to fit your needs. 

## Installation
Python 3 is required as well as Telethon and its dependencies
```console
# install required Python 3 modules
$ python -m pip install -r requirements.txt
```

## Setup
In order to use the Blaster, you first need to:
- Create your own Telegram api id and hash [Click here to go to telegram](https://my.telegram.org/)
- Have a csv file with the fields "Telegram ITA" and "Telegram ENG" that contains the contacts
- Prepare a text in Italian and in English to send to your contacts

## Usage
### Method 1: Run directly
**TelegramBlaster** can be run directly by executing the following command
```console
$ python3 TelegramBlaster.py
```
Using this method the program will ask you the api keys, the messages and the csv file path.

### Method 2: Import script
**TelegramBlaster** can be imported in your Python script and used in the following way
```python
from TelegramBlaster import TelegramBlaster
TelegramBlaster(api_id, api_hash, csv_path)

or:
TelegramBlaster(api_id, api_hash, csv_path, self, api_id, api_hash, csv_path, message_ita='nessun_messaggio_inserito', message_eng='no_message_inserted'
```  
  
    
  
##### Created by [Alessandro Chiarelli](https://github.com/alexcarchiar) because I hate repetitive tasks!
