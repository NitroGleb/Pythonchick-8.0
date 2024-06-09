import random
import aiogram
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from choose import WorkState
anekdot = []
# Добавь анекдоты сюда
random_game_for_one = random.choice(anekdot)

async def message_handler(msg: Message):
    text1 = f'Вот тебе мой анекдот {random_game_for_one}!\n'
    await msg.answer(text1)

#BotCommand(
            #command = 'anekdot',
            #description = 'Рассказать анекдот'
        #)
