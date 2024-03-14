from aiogram import Bot
import os

bot_token = os.getenv('pt_feedback_bot_token')
bot = Bot(token=bot_token, parse_mode="HTML")

admins = [539491282]
