from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='TATU'),
            KeyboardButton(text='TDTU')
        ],
        [
            KeyboardButton(text='Irrigatsiya'),
            KeyboardButton(text='OZMU')
        ],
        [
            KeyboardButton(text='Hamma_universitetlar_joylashuvi')
        ]
    ],
    resize_keyboard=True
)