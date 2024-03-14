from aiogram import Router, F
from aiogram.types import Message
import logging
import json
import app.config.cfg as cfg

bot = cfg.bot
router: Router = Router()


@router.message(F.text)
async def bot_get_message_info(message: Message):
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
        json_fromuser = json.dumps(from_user, indent=2)
        json_chat = json.dumps(chat, indent=2)
        json_data = json.dumps(data, indent=2)
        await bot.send_message(cfg.admins[0], f'<b>message_from_user</b>\n<code>{json_fromuser}</code>\n'
                                              f'<b>message_chat</b>\n<code>{json_chat}</code>\n'
                                              f'<b>message</b>\n<code>{json_data}</code>',
                               parse_mode='HTML')
        await bot.send_message(cfg.admins[0], f'\n\n<b>ℹ️ От пользователя</b>: {from_user.get("first_name")} @{chat.get("username")}'
                                              f'\n<b>💬 Сообщение</b>: {data.get("text")}',
                               parse_mode='HTML')
        await message.answer("✅ Ваше сообщение отправлено, автор постарается ответить в ближайшее время")
    except Exception as e:
        logging.warning(e)
        await message.answer(f'{e}')
