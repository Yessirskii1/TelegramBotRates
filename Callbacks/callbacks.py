from aiogram.types import CallbackQuery, Message
from aiogram import Router, F

from Keyboards import inline
from parsing_def import pars, pars_crypto
router = Router()


@router.callback_query(F.data == "cur")
async def cur(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("⬇Выбери валюту⬇", reply_markup=inline.currency_kb)

@router.callback_query(F.data == "crypto")
async def crypto(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("⬇Выбери криптовалюту⬇", reply_markup=inline.cryptocurrency_kb)

@router.callback_query(F.data == "back")
async def x(callback: CallbackQuery):
    await callback.message.delete()

@router.callback_query(F.data == "go_main_menu" )
async def get_eu(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Тебе интересен курс валюты или крипты ?", reply_markup=inline.main_kb)






@router.callback_query(F.data == "usd")
async def get_us(callback: CallbackQuery):
    await callback.message.answer(pars.get_usd(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "euro")
async def get_eu(callback: CallbackQuery):
    await callback.message.answer(pars.get_euro(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "thai")
async def get_eu(callback: CallbackQuery):
    await callback.message.answer(pars.get_thai(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "china" )
async def get_eu(callback: CallbackQuery):
    await callback.message.answer(pars.get_china(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "korea" )
async def get_eu(callback: CallbackQuery):
    await callback.message.answer(pars.get_korean(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "kz" )
async def get_eu(callback: CallbackQuery):
    await callback.message.answer(pars.get_kz(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "japan" )
async def get_eu(callback: CallbackQuery):
    await callback.message.answer(pars.get_jap(), reply_markup=inline.help_kb)
    await callback.answer("complete")





@router.callback_query(F.data == "btc")
async def get_bitok(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_btc(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "eth")
async def get_kefir(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_ethi(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "lite")
async def get_kefir(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_lite_coin(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "dog")
async def get_kefir(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_doge_coin(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "tet")
async def get_kefir(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_tether(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "xrp")
async def get_kefir(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_xrp(), reply_markup=inline.help_kb)
    await callback.answer("complete")

@router.callback_query(F.data == "bin")
async def get_kefir(callback: CallbackQuery):
    await callback.message.answer(pars_crypto.get_bc(), reply_markup=inline.help_kb)
    await callback.answer("complete")


