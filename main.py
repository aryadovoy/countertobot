import logging, datetime, locale
from aiogram import Bot, Dispatcher, executor, types
from secret import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
format = '%Y-%m-%d'


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.reply('Hello!\nI was made for counting days, use `/counttodate` for count from today to date and `/countdiff` for count between two dates. Use yyyy-mm-dd format.', parse_mode='markdown')

@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await msg.reply('Write `/counttodate yyyy-mm-dd` or `/countdiff yyyy-mm-dd yyyy-mm-dd`.', parse_mode='markdown')

@dp.message_handler(commands=['counttodate'])
async def get_message(msg: types.Message):
    second_date = datetime.datetime.strptime(msg.text[-10:],format)
    first_date = datetime.datetime.today()
    td = first_date.strftime('Today is %A, %d %B, %Y.')
    diff_dates = second_date - first_date + datetime.timedelta(days=1)
    await msg.answer(td + ' To ' + msg.text[-10:] + ' is ' + str(diff_dates.days) + ' days.')

@dp.message_handler(commands=['countdiff'])
async def get_message(msg: types.Message):
    second_date = datetime.datetime.strptime(msg.text[-10:],format)
    first_date = datetime.datetime.strptime(msg.text[-21:-11],format)
    td = first_date.strftime('First day is %A, %d %B, %Y.')
    diff_dates = second_date - first_date
    await msg.answer(td + ' To ' + msg.text[-10:] + ' is ' + str(diff_dates.days) + ' days.')

@dp.message_handler(types.ChatType.is_private)
async def wrong_format(msg: types.Message):
    await msg.answer('Use commands (see /help for information).')


if __name__ == '__main__':
    executor.start_polling(dp)
