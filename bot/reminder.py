from datetime import datetime, date, timedelta
from aiogram.bot import bot
import asyncio

from bot.data.config import service, spreadsheet_id, BOT_TOKEN
from bot.loader import db


async def send_message(id, text):
    await bot.send_message(id, text)


async def job():
    otvet1 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:A900',
        majorDimension='ROWS'
    ).execute()

    otvet2 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='C1:C900',
        majorDimension='ROWS'
    ).execute()

    otvet3 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='E1:E900',
        majorDimension='ROWS'
    ).execute()

    lesson1 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='B1:B900',
        majorDimension='ROWS'
    ).execute()

    lesson2 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='D1:D900',
        majorDimension='ROWS'
    ).execute()

    lesson3 = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='F1:F900',
        majorDimension='ROWS'
    ).execute()

    futured = datetime.now()

    for i in range(0, 1000):
        if otvet1['values'][i][0] == futured.strftime("%d.%m.%Y %H:%M"):
            await send_message(int(db.get_id_group(groupi='1')[0]), f"Время пройти урок: {lesson1['values'][i][0]}")

    for j in range(0, 1000):
        if otvet2['values'][j][0] == futured.strftime("%d.%m.%Y %H:%M"):
            await send_message(int(db.get_id_group(groupi='2')[0]), f"Время пройти урок: {lesson2['values'][j][0]}")

    for k in range(0, 1000):
        if otvet3['values'][k][0] == futured.strftime("%d.%m.%Y %H:%M"):
            await send_message(int(db.get_id_group(groupi='3')[0]), f"Время пройти урок: {lesson3['values'][k][0]}")
    print("1")
    #await asyncio.sleep(1)

'''
schedule.every(1).seconds.do(job)
schedule.every(5).to(10).days.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
'''
