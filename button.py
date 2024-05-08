from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder




menu=InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton(text="Options ⚙️",callback_data="yes"),InlineKeyboardButton(text="Channel 🔈 ",callback_data="chanel")],
    [InlineKeyboardButton(text="Contact 🧑🏼‍💻",url="https://t.me/XAVIERXCK")],
  ]
 
  
)