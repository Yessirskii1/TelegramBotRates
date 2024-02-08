from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from Keyboards import inline

router = Router()

@router.message(CommandStart)
async def start(message: Message):
    await message.answer("Добро пожаловать🖐🏼, это Сurrency&Crypto бот!"
                        "\n\nЯ подскажу тебе актуальные курсы валют и крипты."
                        "\n\nВсе акутальные курсы берутся с официального сайта <b>ЦБ</b> и <b>Binance</b>.")
    await message.answer("<b>Тебе интересна крипта или валюта ?</b>", reply_markup=inline.main_kb)

