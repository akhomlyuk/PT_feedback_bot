from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from app.texts import show_description
import app.config.cfg as cfg
import logging

router: Router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    try:
        # if message.from_user.id not in cfg.admins:
        logging.info(f'Бот активирован: {message.from_user}')
        await message.answer(show_description, disable_web_page_preview=True)
    except Exception as e:
        logging.error(e)


@router.message(Command("help"))
async def cmd_help(message: Message):
    try:
        if message.from_user.id not in cfg.admins:
            logging.info(f"From user: {message.from_user} and {message.from_user.username}")
        await message.answer(show_description, disable_web_page_preview=True)
    except Exception as e:
        logging.warning(e)
        await message.answer(f'{e}')
