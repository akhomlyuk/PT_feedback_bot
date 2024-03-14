import asyncio
import logging
import os
from aiogram import Dispatcher, types
import app.config.cfg as cfg
from app.handlers import help, message_info
from sys import platform

if platform == "win32":
    os.makedirs(os.path.expanduser('~') + r'\PycharmProjects\PT_feedback_bot\logs', exist_ok=True)
    logging.basicConfig(level=logging.INFO, force=True, filename=os.path.expanduser('~') + r'\PycharmProjects\PT_feedback_bot\logs\bot.log',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
else:
    os.makedirs(os.path.expanduser('~') + '/PT_feedback_bot/logs', exist_ok=True)
    logging.basicConfig(level=logging.INFO, force=True, filename=os.path.expanduser('~') + '/PT_feedback_bot/logs/bot.log',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = cfg.bot
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(help.router)
dp.include_router(message_info.router)


@dp.errors()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f'Ошибка при обработке запроса {update}: {exception}')


async def main():
    try:
        logging.info('Bot starting...')
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit) as e:
        logging.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
