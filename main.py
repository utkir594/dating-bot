from aiogram import Bot, Dispatcher, types, executor
import logging

# Bot tokeningizni shu yerga yozing
API_TOKEN = '7998312444:AAEzr3JibLUzHX8Yf8EVl4ShP1WSm0rQFrE'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Foydalanuvchilarni vaqtincha xotirada saqlaymiz
users = {}

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    users[message.from_user.id] = {}
    await message.answer("👋 Salom! Tanishuv botiga xush kelibsiz. Ismingizni yozing:")

@dp.message_handler(lambda message: message.from_user.id in users and 'name' not in users[message.from_user.id])
async def set_name(message: types.Message):
    users[message.from_user.id]['name'] = message.text
    await message.answer("🗓 Yoshingizni kiriting:")

@dp.message_handler(lambda message: message.from_user.id in users and 'age' not in users[message.from_user.id])
async def set_age(message: types.Message):
    if not message.text.isdigit():
        return await message.answer("❗ Iltimos, yoshni son bilan kiriting.")
    users[message.from_user.id]['age'] = int(message.text)
    await message.answer("👫 Jinsingiz? (Erkak/Ayol):")

@dp.message_handler(lambda message: message.from_user.id in users and 'gender' not in users[message.from_user.id])
async def set_gender(message: types.Message):
    gender = message.text.lower()
    if gender not in ['erkak', 'ayol']:
        return await message.answer("❗ Faqat 'Erkak' yoki 'Ayol' deb yozing.")
    users[message.from_user.id]['gender'] = gender
    await message.answer("✅ Rahmat! Endi boshqalarning profilini ko'rish uchun /search ni bosing.")

@dp.message_handler(commands=['search'])
async def search_profiles(message: types.Message):
    your_data = users.get(message
