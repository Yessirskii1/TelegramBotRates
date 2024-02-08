import asyncio
from aiogram import Bot, Dispatcher
from Handlers import commands
from Callbacks import callbacks

async def main():
    bot = Bot("6883034354:AAEG5qsuhZeeUOTElWOdf7H1-jqeBysZoMk", parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        commands.router,
        callbacks.router
    )

    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())