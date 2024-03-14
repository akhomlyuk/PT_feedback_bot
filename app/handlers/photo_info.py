from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import app.config.cfg as cfg
import logging
import json

router: Router = Router()


@router.message(F.photo)
async def bot_get_photo_info(message: Message):
    if message.from_user.id != 539491282:
        logging.info(message.from_user)
    try:
        msg_obj = message.model_dump(mode='python')
        msg_obj_ex = message.model_dump(mode='python', exclude={'from_user', 'chat', 'date'})
        from_user = {}
        chat = {}
        data = {}
        for key, value in msg_obj_ex.items():
            if value is not None:
                data[key] = value
        for key, value in msg_obj['from_user'].items():
            if value is not None:
                from_user[key] = value
        for key, value in msg_obj['chat'].items():
            if value is not None:
                chat[key] = value

        photo_id = message.photo[-1].file_id
        photo_caption = message.caption
        await cfg.bot.send_photo(cfg.admins[0], photo_id)
        await cfg.bot.send_message(cfg.admins[0], f"Caption: {photo_caption}")
        await cfg.bot.send_message(cfg.admins[0], f'\n\n<b>ℹ️ От пользователя</b>: {from_user.get("first_name")} @{chat.get("username")}',
                                   parse_mode='HTML')
    except Exception as e:
        logging.warning(e)
        await message.answer(f'{e}')
