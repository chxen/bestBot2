import httplib2
import apiclient.discovery
from aiogram import types, Bot
from oauth2client.service_account import ServiceAccountCredentials

BOT_TOKEN = "1924578488:AAHAwHcFin_SM4nFF08oUrCvzCAHP6m76kA"
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

CREDENTIALS_FILE = "C:\\Users\\Zver\\PycharmProject\\bestBot1\\bot\\handlers\\users\\creeds.json"
spreadsheet_id = '1xT_P8rhQ7_0paAHbE-elHp0P-73en13Ms99d6tw-KVA'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


'''
# Функции для работы с гугл таблицей

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:A1',
    majorDimension='ROWS'
).execute()
print(values)

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B3:C4",
             "majorDimension": "ROWS",
             "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
            {"range": "D5:E6",
             "majorDimension": "COLUMNS",
             "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
        ]
    }
).execute()
'''
