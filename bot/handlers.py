from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hbold, hlink
from peewee import IntegrityError
import asyncio

from bot.database import db
from .dispatcher import dispatcher
from . models import User


@dispatcher.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        User.create(id=message.from_user.id, name=name)
    except IntegrityError:
        db.rollback()
        await message.answer(
            text="Не удалось зарегестрировать пользователя!",
            disable_web_page_preview=True
        )
        return

    await message.answer(
        text=f'Добро пожаловать в бот расписаний, ' +
             '<b>{message.from_user.full_name}</b>!\n' +
             hbold('Пожалуйста пришли мне номер группы. Только цифру: 1, 2, 3.\n') +
             'Таблица с расписанием доступна по ' +
             hlink(
                 'ссылке',
                 'https://docs.google.com/spreadsheets/d'
                 '/1xT_P8rhQ7_0paAHbE-elHp0P-73en13Ms99d6tw-KVA/edit#gid=0'
             ),
        disable_web_page_preview=True)


@dispatcher.message_handler()
async def enter_group(message: types.Message):
    group = message.text
    if group == '1' or group == '2' or group == '3':
        user = User.get(id=message.from_user.id)
        user.group = group
        user.save()
        await message.answer(
            f'Данные были обновлены. '
            f'Запись в бд: id пользователя{user}, группа {user.group}'
        )

    else:
        await message.answer(
            'Неверный номер группы. '
            'Вызовите команду /start еще раз и введите номер группы: 1, 2 или 3.'
        )

    await asyncio.sleep(1)
