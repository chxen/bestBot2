from datetime import datetime

from .google_api import google_client
from .models import User
from . import bot
from . import settings


async def job():
    times_1 = google_client.spreadsheets().values().get(
        spreadsheetId=settings.SPREADSHEET_ID,
        range='A1:A900',
        majorDimension='ROWS'
    ).execute()

    times_2 = google_client.spreadsheets().values().get(
        spreadsheetId=settings.SPREADSHEET_ID,
        range='C1:C900',
        majorDimension='ROWS'
    ).execute()

    times_3 = google_client.spreadsheets().values().get(
        spreadsheetId=settings.SPREADSHEET_ID,
        range='E1:E900',
        majorDimension='ROWS'
    ).execute()

    lessons_1 = google_client.spreadsheets().values().get(
        spreadsheetId=settings.SPREADSHEET_ID,
        range='B1:B900',
        majorDimension='ROWS'
    ).execute()

    lessons_2 = google_client.spreadsheets().values().get(
        spreadsheetId=settings.SPREADSHEET_ID,
        range='D1:D900',
        majorDimension='ROWS'
    ).execute()

    lessons_3 = google_client.spreadsheets().values().get(
        spreadsheetId=settings.SPREADSHEET_ID,
        range='F1:F900',
        majorDimension='ROWS'
    ).execute()

    futured = datetime.now()

    for time, lesson in zip(times_1['values'], lessons_1['values']):
        if time[0] == futured.strftime("%d.%m.%Y %H:%M"):
            users = User.select(User.group == '1')
            for user in users:
                await bot.send_message(user.id, f"Время пройти урок: {lesson[0]}")

    for time, lesson in zip(times_2['values'], lessons_2['values']):
        if time[0] == futured.strftime("%d.%m.%Y %H:%M"):
            users = User.select(User.group == '2')
            for user in users:
                await bot.send_message(user.id, f"Время пройти урок: {lesson[0]}")

    for time, lesson in zip(times_3['values'], lessons_3['values']):
        if time[0] == futured.strftime("%d.%m.%Y %H:%M"):
            users = User.select(User.group == '3')
            for user in users:
                await bot.send_message(user.id, f"Время пройти урок: {lesson[0]}")
