import logging, datetime, locale
from aiogram import Bot, Dispatcher, executor, types
from secret import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
format = '%Y-%m-%d'


async def ctd(a):
    second_date = datetime.datetime.strptime(a[-10:],format)
    first_date = datetime.datetime.today()
    diff_dates = second_date - first_date + datetime.timedelta(days=1)
    return str(diff_dates.days)


async def cbd(a):
    second_date = datetime.datetime.strptime(a[-10:],format)
    first_date = datetime.datetime.strptime(a[-21:-11],format)
    diff_dates = second_date - first_date
    return str(diff_dates.days)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.reply('Hello!\nI was made for counting days, use `/ctd` for count from today to date and `/cbd` for count between two dates. Use yyyy-mm-dd format.', parse_mode='markdown')


@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await msg.reply('Write `/ctd yyyy-mm-dd` or `/cbd yyyy-mm-dd yyyy-mm-dd`.', parse_mode='markdown')


@dp.message_handler(commands=['ctd'])
async def get_message(msg: types.Message):
    ans = await ctd(msg.text)
    await msg.answer(ans)


@dp.message_handler(commands=['cbd'])
async def get_message(msg: types.Message):
    ans = await cbd(msg.text)
    await msg.answer(ans)


@dp.message_handler(types.ChatType.is_private)
async def wrong_format(msg: types.Message):
    await msg.answer('Use commands (see /help for information).')


if __name__ == '__main__':
    executor.start_polling(dp)
