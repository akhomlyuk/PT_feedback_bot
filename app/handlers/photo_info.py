from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import app.config.cfg as cfg
import logging
router: Router = Router()


@router.message(F.photo)
async def bot_get_photo_info(message: Message):
    if message.from_user.id != 539491282:
        logging.info(message.from_user)
    try:
        photo_id = message.photo[-1].file_id
        file = FSInputFile(photo_id)
        file_info = await cfg.bot.get_file(file)
        await cfg.bot.send_document(cfg.admins[0], file_info)
    except Exception as e:
        logging.warning(e)
        await message.answer(f'{e}')
