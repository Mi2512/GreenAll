import logging
import random
import string
import emoji
import aiogram.utils.markdown as md

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.utils import executor

from messages import *
from db import users_db

logging.basicConfig(level=logging.DEBUG)

BOT_TOKEN = '1767589392:AAG_A359ruZWcbfGQL-u5icTH5ljSZRERYQ'

bot = Bot(token=BOT_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# states

class \
        Form(StatesGroup):
    wiki = State()
    voice = State()
    voice_hi = State()
    voice_low = State()
    image = State()


##############################################---Start для всех языков---##############################################################

@dp.message_handler(commands='start')
async def start_cmd(message: types.Message):
    if not users_db.find_one({"chat_id": message.chat.id}):
        users_db.insert_one({"chat_id": message.chat.id})
        await bot.send_message(message.chat.id, HELLO_MESSAGE)
        # Если пользователь есть в базе
    else:
        await bot.send_message(message.chat.id, HELLO_AGAIN_MESSAGE)
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['🇷🇺Русский', '🇬🇧English', '🇹🇷Türk', '🇵🇱Polskie', '🇩🇪Deutsch', '🇫🇷Français', '🇮🇹Italiano',
               'اللغة العربية🇦🇼', '🇪🇸Español']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text('Выберите язык для продолжения!'),
            sep='\n'
        ),
        reply_markup=keyboard,
    )


###########################------------------------------Чат бот для "Русский"------------------------------ #####################################################################################################################

@dp.message_handler(state='*', text='🇷🇺Русский')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Выбран язык:", md.bold("Русский")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Оборудование для грибных ферм', 'LED светодиодное освещение', 'О компании']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Здравствуйте, я -", md.bold("Green Al bot")),
            md.text('Буду рад помочь вам!'),
            md.text('Воспользуйтесь клавиатурой, чтобы начать!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Оборудование для грибных ферм')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✔Закaзать расчёт оборудывания', "Аллюминевые стеллажи для выращивания грибов, шампиньонов", "Оборудование для сбора шапьпиньонов",
               "Дополнительное оборудование", "Назад"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Добро пожаловать в раздел:", md.bold("Оборудование для грибных ферм")),
            md.text("Выберите раздел который вам интересен!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='LED светодиодное освещение')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✔Заказать расчёт оборудывания', "Уличное освещение", "Промышленное освещение", "Торговое освещение", "Фито-освещение", "Возврат"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Добро пожаловать в раздел:", md.bold("LED светодиодное освещение")),
            md.text("Выберите раздел который вам интересен!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['О компании'])
    async def wiki_request(message: types.Message):
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«ООО «ГринАл» GreenAl изготавливает продукцию:"),
                md.text('- Оборудование для грибных ферм;'),
                md.text('- Промышленные тепличные комплексы;'),
                md.text('- Промышленные светодиодные светильники;'),
                md.text('- Комплектующие для солнечной энергетики;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Оборудование для грибных ферм')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✔Закaзать расчёт оборудывания', "Аллюминевые стеллажи для выращивания грибов, шампиньонов", "Оборудование для сбора шапьпиньонов",
               "Дополнительное оборудование", "Назад"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Добро пожаловать в раздел:", md.bold("Оборудование для грибных ферм")),
            md.text("Выберите раздел который вам интересен!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Отмена'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Оборудование для грибных ферм", "LED светодиодное освещение", "О компании"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ваше действие отменено', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Аллюминевые стеллажи для выращивания грибов, шампиньонов'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Аллюминевые стеллажи для выращивания грибов, шампиньонов',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Длина стеллажа_30,0 м (стандарт)"),
        md.text('Ширина (внутр.)_1,34 м (стандарт)'),
        md.text('Ширина (нар.)_1,5 м (стандарт)'),
        md.text('Высота стеллажа_от 2,8 до 5,0 м'),
        md.text('Кол-во ярусов_от 3 до 7 шт'),
        md.text('Шаг опорных стоек_1,5 / 3 м'),
        md.text('Высота яруса (полки)_600 мм'),
        md.text('Высота бокового борта_180 мм'),
        md.text('Вес конст. стеллажа_1 900 кг'),
        md.text('Расчетная нагрузка_195 кг/м2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Оборудование для сбора шапьпиньонов'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Тележка подвесная Standart для сбора шампиньонов',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Ширина_1 950 мм"),
        md.text('Высота_3 130 мм'),
        md.text('Глубина_610 мм'),
        md.text('Вес_59 кг'),
        md.text('Грузоподъемность_170 кг'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Тележка напольная для сбора шампиньонов',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Вес конструкции_15 кг"),
        md.text('Грузоподъемность_150 кг'),
        md.text('Материал сиденья_Пластик'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Платформа для сбора шампиньонов',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Длина_1000 мм"),
        md.text('Высота_1125 мм'),
        md.text('Ширина_535 мм'),
        md.text('Вес платформы_16 кг'),
        md.text('Вес табурета_5 кг'),
        md.text('Размер ячейки для весов_330*360 мм'),
        md.text('Нагрузка на 1 ряд_10  кг'),
        md.text('Количество рядов для размещения полок_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Дополнительное оборудование'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Стенд для зарядки весов',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Высота_1300 мм"),
        md.text('Длина_1000 мм'),
        md.text('Ширина_800 мм'),
        md.text('Количество мест_20 шт'),
        md.text('Размер ячейки для весов_330*360 мм'),
        md.text('Вес конструкции_38 кг'),
        md.text('Нагрузка на одну ячейку_25 кг'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Стенд для зарядки весов с розетками',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Высота_1300 мм"),
        md.text('Длина_1000 мм'),
        md.text('Ширина_800 мм'),
        md.text('Количество мест_20 шт'),
        md.text('Размер ячейки для весов_330*360 мм'),
        md.text('Вес конструкции_38 кг'),
        md.text('Нагрузка на одну ячейку_25 кг'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Сушилка для ведер',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Длина_1 670 мм"),
        md.text('Высота_1 624 мм'),
        md.text('Ширина_620 мм'),
        md.text('Вес конструкции_17 кг'),
        md.text('Количество мест для ведер_20 шт'),
        md.text('Грузоподъемность_120 кг'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Назад'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Оборудование для грибных ферм', 'LED светодиодное освещение', 'О компании']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Вы вернулсь назад ', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='LED светодиодное освещение')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✔Заказать расчёт оборудывания',"Уличное освещение", "Промышленное освещение", "Торговое освещение", "Фито-освещение", "Возврат"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Добро пожаловать в раздел:", md.bold("LED светодиодное освещение")),
            md.text("Выберите раздел который вам интересен!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Отмена'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Оборудование для грибных ферм", "LED светодиодное освещение", "О компании"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ваше действие отменено', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Уличное освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button),
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________30 Вт"),
        md.text('Световой поток_________4373 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA60',
    )
    file = open('GreenAlStreetA60.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________60 Вт"),
        md.text('Световой поток_________8746 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB50',
    )
    file = open('GreenAlStreetB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________50 Вт"),
        md.text('Световой поток_________7896 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB100',
    )
    file = open('GreenAlStreetB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________100 Вт"),
        md.text('Световой поток_________15792 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB150',
    )
    file = open('GreenAlStreetB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________150 Вт"),
        md.text('Световой поток_________23688 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB200',
    )
    file = open('GreenAlStreetB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________200 Вт"),
        md.text('Световой поток_________31584 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB250',
    )
    file = open('GreenAlStreetB250.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________240 Вт"),
        md.text('Световой поток_________39480 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Промышленное освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________30 Вт"),
        md.text('Световой поток_________39480 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________60 Вт"),
        md.text('Световой поток_________8932 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________90 Вт"),
        md.text('Световой поток_________13398 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________120 Вт"),
        md.text('Световой поток_________17864 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________150 Вт"),
        md.text('Световой поток_________22330 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B50',
    )
    file = open('GreenAlPromB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________50 Вт"),
        md.text('Световой поток_________7896 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B100',
    )
    file = open('GreenAlPromB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________100 Вт"),
        md.text('Световой поток_________15792 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B150',
    )
    file = open('GreenAlPromB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________150 Вт"),
        md.text('Световой поток_________23688 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B200',
    )
    file = open('GreenAlPromB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________200 Вт"),
        md.text('Световой поток_________31584 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B240',
    )
    file = open('GreenAlPromB240.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________240 Вт"),
        md.text('Световой поток_________36480 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Торговое освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________10 Вт"),
        md.text('Световой поток_________1500 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________20 Вт"),
        md.text('Световой поток_________3000 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Фито-освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________30 Вт"),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________60 Вт"),
        md.text('Степень защиты_________IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Возврат'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Оборудование для грибных ферм', 'LED светодиодное освещение', 'О компании']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Вы вернулсь назад ', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['О компании'])
async def wiki_request(message: types.Message):
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«ООО «ГринАл» GreenAl изготавливает продукцию:"),
            md.text('- Оборудование для грибных ферм;'),
            md.text('- Промышленные тепличные комплексы;'),
            md.text('- Промышленные светодиодные светильники;'),
            md.text('- Комплектующие для солнечной энергетики;'),
            sep='\n'

        ),
    )


#################################################################################################################################################
@dp.message_handler(state='*', text='✔Заказать расчёт оборудывания')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать консультанту!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("Добрый день!")),
        md.text('Меня зовут ФИО'),
        md.text('По вопросам заказа оборудывания обращайтесь комне!'),
        md.text('Всегда рад помочь вам'),
        sep='\n'

    ), reply_markup=keyboard),

@dp.message_handler(state='*', text='✔Закaзать расчёт оборудывания')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать консультанту!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("Добрый день!")),
        md.text('Меня зовут ФИО'),
        md.text('По вопросам заказа оборудывания обращайтесь комне!'),
        md.text('Всегда рад помочь вам'),
        sep='\n'

    ), reply_markup=keyboard),


#####################################################################################################################################################3
@dp.message_handler(state='*', text='🇬🇧English')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Selected language:", md.bold("English")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Equipment for mushroom farms ', ' LED lighting ', ' About the company']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Hi, I'm-", md.bold("Green Al bot")),
            md.text('I will be glad to help you!'),
            md.text('Use your keyboard to get started!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Equipment for mushroom farms')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Ordеr equipment calculation', "Aluminum racks for growing mushrooms, champignons ", " Equipment for collecting chappignons ",
               "Additional equipment", "Back"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Welcome to the section:", md.bold("Equipment for mushroom farms")),
            md.text("Choose the section that interests you!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='LED lighting')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Order equipment calculation', "Street lighting ", " Industrial lighting ", " Commercial lighting ", " Phyto-lighting ", " Return"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Welcome to the section:", md.bold("LED lighting")),
            md.text("Choose the section that interests you!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['About the company'])
    async def wiki_request(message: types.Message):
        with open('userlog.txt', 'a') as file:  # Создается текстовый файл
            # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
            file.write(
                f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«GreenAl» LLC GreenAl manufactures products:"),
                md.text('- Equipment for mushroom farms;'),
                md.text('- Industrial greenhouse complexes;'),
                md.text('- Industrial LED luminaires;'),
                md.text('- Components for solar energy;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Equipment for mushroom farms')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Ordеr equipment calculation', "Aluminum racks for growing mushrooms, champignons ", " Equipment for collecting chappignons ",
               "Additional equipment", "Back"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Welcome to the section:", md.bold("Equipment for mushroom farms")),
            md.text("Choose the section that interests you!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Cancellation'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Equipment for mushroom farms ", " LED lighting ", " About the company"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Your action is canceled', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Aluminum racks for growing mushrooms, champignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Aluminum racks for growing mushrooms, champignons',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Rack length_30.0 m (standard)"),
        md.text('Width (inner) _ 1.34 m (standard)'),
        md.text('Width (out) _ 1.5 m (standard)'),
        md.text('Shelving height_2.8 to 5.0 m '),
        md.text('Number of tiers_from 3 to 7 pieces'),
        md.text('Support column spacing_1.5 / 3 m'),
        md.text('Deck (shelf) height _600 mm'),
        md.text('Side board height_180 mm'),
        md.text('Weight const. rack_1 900 kg'),
        md.text('Design load_195 kg / m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Equipment for collecting chappignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Hanging trolley Standart for collecting champignons',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Width_1 950 mm"),
        md.text('Height_3 130 mm'),
        md.text('Depth_610 mm'),
        md.text('Weight_59 kg'),
        md.text('Loading capacity_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Floor trolley for collecting champignons',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Structure weight_15 kg"),
        md.text('Loading capacity_150 kg'),
        md.text('Seat material_Plastic'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Mushroom picking platform',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Length_1000 mm"),
        md.text('Height_1125 mm'),
        md.text('Width_535 mm'),
        md.text('Platform weight_16 kg'),
        md.text('Stool weight_5 kg'),
        md.text('Cell size for scales_330 * 360 mm'),
        md.text('Load for 1 row_10 kg'),
        md.text('Number of rows for shelves_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Additional equipment'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Scale charging stand',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Height_1300 mm"),
        md.text('Length_1000 mm'),
        md.text('Width_800 mm'),
        md.text('Number of seats_20 pcs'),
        md.text('Cell size for scales_330 * 360 mm'),
        md.text('Construction weight_38 kg'),
        md.text('Load per cell_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Scale charging stand with sockets',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Height_1300 mm"),
        md.text('Length_1000 mm'),
        md.text('Width_800 mm'),
        md.text('Number of seats_20 pcs'),
        md.text('Cell size for scales_330 * 360 mm'),
        md.text('Construction weight_38 kg'),
        md.text('Load per cell_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Dryer for buckets',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Length_1 670 mm"),
        md.text('Height_1 624 mm'),
        md.text('Width_620 mm'),
        md.text('Construction weight_17 kg'),
        md.text('Number of places for buckets_20 pcs'),
        md.text('Loading capacity_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Back'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Equipment for mushroom farms ', ' LED lighting ', ' About the company']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'You came back', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='LED lighting')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Order equipment calculation', "Street lighting ", " Industrial lighting ", " Commercial lighting ", " Phyto-lighting ", " Return"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Welcome to the section:", md.bold("LED lighting")),
            md.text("Choose the section that interests you!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Cancellation'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Equipment for mushroom farms ", " LED lighting ", " About the company"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Your action is canceled', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Street lighting'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 30 W"),
        md.text('Luminous flux _________ 4373 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA60',
    )
    file = open('GreenAlStreetA60.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 60 W"),
        md.text('Luminous flux _________ 8746 Lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB50',
    )
    file = open('GreenAlStreetB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 50 W"),
        md.text('Luminous flux _________ 7896 Lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB100',
    )
    file = open('GreenAlStreetB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 100 W"),
        md.text('Luminous flux _________ 15792 Lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB150',
    )
    file = open('GreenAlStreetB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 150 W"),
        md.text('Luminous flux _________ 23688 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB200',
    )
    file = open('GreenAlStreetB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 200 W"),
        md.text('Luminous flux _________ 31584 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB250',
    )
    file = open('GreenAlStreetB250.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 240 W"),
        md.text('Luminous flux _________ 39480 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Industrial lighting'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 30 W"),
        md.text('Luminous flux _________ 39480 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 60 W"),
        md.text('Luminous flux _________ 8932 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 90 W"),
        md.text('Luminous flux _________ 13398 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 120 W"),
        md.text('Luminous flux _________ 17864 Lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 150 W"),
        md.text('Luminous flux _________ 22330 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B50',
    )
    file = open('GreenAlPromB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 50 W"),
        md.text('Luminous flux _________ 7896 Lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B100',
    )
    file = open('GreenAlPromB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 100 W"),
        md.text('Luminous flux _________ 15792 Lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B150',
    )
    file = open('GreenAlPromB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 150 W"),
        md.text('Luminous flux _________ 23688 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B200',
    )
    file = open('GreenAlPromB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 200 W"),
        md.text('Luminous flux _________ 31584 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B240',
    )
    file = open('GreenAlPromB240.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 240 W"),
        md.text('Luminous flux _________ 36480 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Commercial lighting'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 10 W"),
        md.text('Luminous flux _________ 1500 lm'),
        md.text('Color. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 20 W"),
        md.text('Luminous flux _________ 3000 lm'),
        md.text('Col. temperature ______ 5000 K'),
        md.text('Protection degree _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Phyto-lighting'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 30 W"),
        md.text('Protection degree _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details on the site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Power ______________ 60 W"),
        md.text('Protection degree _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Return'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Equipment for mushroom farms ', ' LED lighting ', ' About the company']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'You came back ', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['About the company'])
async def wiki_request(message: types.Message):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«GreenAl» LLC GreenAl manufactures products:"),
            md.text('- Equipment for mushroom farms;'),
            md.text('- Industrial greenhouse complexes;'),
            md.text('- Industrial LED luminaires;'),
            md.text('- Components for solar energy;'),
            sep='\n'

        ),
    )


############################################################################################################################################
@dp.message_handler(state='*', text='Order equipment calculation')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Write to a consultant!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("Good day!")),
        md.text('My name is ФИО'),
        md.text('For ordering equipment, please contact me!'),
        md.text('Always happy to help you'),
        sep='\n'

    ), reply_markup=keyboard),

@dp.message_handler(state='*', text='Ordеr equipment calculation')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Write to a consultant!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("Good day!")),
        md.text('My name is ФИО'),
        md.text('For ordering equipment, please contact me!'),
        md.text('Always happy to help you'),
        sep='\n'

    ), reply_markup=keyboard),

#####################################################################################################################################################
@dp.message_handler(state='*', text='🇹🇷Türk')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Dil seçildi:", md.bold("Türk")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Mantar çiftlikleri için donatım ', ' LED aydınlatma ', 'Şirket hakkında']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Merhaba ben -", md.bold("Green Al bot")),
            md.text('Sana yardım etmekten memnun olacağım!'),
            md.text('Başlamak için klavyenizi kullanın!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Mantar çiftlikleri için donatım')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Sipаriş ekipmanı hesaplama',"Mantar, petrol yetiştirmek için alüminyum raflar ", " Şappignon toplama ekipmanı ", "Ek donanım",
               "Geri"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bölüme hoş geldiniz:", md.bold("Mantar çiftlikleri için donatım")),
            md.text("Sizi ilgilendiren bölümü seçin!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='LED aydınlatma')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Sipariş ekipmanı hesaplama', "Sokak aydınlatması ", " Endüstriyel aydınlatma ", " Ticari aydınlatma ", " Fito aydınlatma ", " Dönüş"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bölüme hoş geldiniz:", md.bold("LED aydınlatma")),
            md.text("Sizi ilgilendiren bölümü seçin!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['Şirket hakkında'])
    async def wiki_request(message: types.Message):
        with open('userlog.txt', 'a') as file:  # Создается текстовый файл
            # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
            file.write(
                f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«GreenAl» LLC GreenAl şu ürünleri üretir:"),
                md.text('- Mantar çiftlikleri için donatım;'),
                md.text('- Endüstriyel sera kompleksleri;'),
                md.text('- Endüstriyel LED armatürler;'),
                md.text('- Güneş enerjisi için bileşenler;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Mantar çiftlikleri için donatım')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Sipаriş ekipmanı hesaplama', "Mantar, petrol yetiştirmek için alüminyum raflar ", " Şappignon toplama ekipmanı ", "Ek donanım",
               "Geri"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bölüme hoş geldiniz:", md.bold("Mantar çiftlikleri için donatım")),
            md.text("Sizi ilgilendiren bölümü seçin!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['İptal'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Mantar çiftlikleri için donatım ", " LED aydınlatma ", " Şirket hakkında"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Eyleminiz iptal edildi', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Mantar, petrol yetiştirmek için alüminyum raflar'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Mantar, petrol yetiştirmek için alüminyum raflar',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Raf uzunluğu_30.0 m (standart)"),
        md.text('ШIrina (dahili) _ 1,34 m (standart)'),
        md.text('Genişlik (çıkış) _ 1,5 m (standart)'),
        md.text('Raf yüksekliği: 2,8 - 5,0 m'),
        md.text('Katman sayısı 3 ila 7 adet'),
        md.text('Destek sütun aralığı_1.5 / 3 m'),
        md.text('Güverte (raf) yüksekliği _600 mm'),
        md.text('Yan panel yüksekliği_180 mm'),
        md.text('Ağırlık sabiti raf_1 900 kg'),
        md.text('Tasarım yükü_195 kg/m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Şappignon toplama ekipmanı'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Petrol toplama için askı arabası Standart',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Genişlik_1 950 mm"),
        md.text('Yükseklik_3 130 mm'),
        md.text('Derinlik_610 mm'),
        md.text('Ağırlık_59 kg'),
        md.text('Yükleme kapasitesi_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Petrol toplamak için zemin arabası',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Yapı ağırlığı_15 kg"),
        md.text('Yükleme kapasitesi_150 kg'),
        md.text('Koltuk malzemesi_Plastik'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Mantar toplama platformu',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Uzunluk_1000 mm"),
        md.text('Yükseklik_1125 mm'),
        md.text('Genişlik_535 mm'),
        md.text('Platform ağırlığı_16 kg'),
        md.text('Dışkı ağırlığı_5 kg'),
        md.text('Ölçekler için hücre boyutu_330 * 360 mm'),
        md.text('1 sıra_10 kg için yük'),
        md.text('Raflar için sıra sayısı_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Ek donanım'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Ölçekli şarj standı',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Yükseklik_1300 mm"),
        md.text('Uzunluk_1000 mm'),
        md.text('Genişlik_800 mm'),
        md.text('Koltuk sayısı_20 adet'),
        md.text('Ölçekler için hücre boyutu_330 * 360 mm'),
        md.text('İnşaat ağırlığı_38 kg'),
        md.text('Hücre başına yük_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Soketli tartı şarj standı',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Yükseklik_1300 mm"),
        md.text('Uzunluk_1000 mm'),
        md.text('Genişlik_800 mm'),
        md.text('Koltuk sayısı_20 adet'),
        md.text('Ölçekler için hücre boyutu_330 * 360 mm'),
        md.text('İnşaat ağırlığı_38 kg'),
        md.text('Hücre başına yük_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Kovalar için kurutucu',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Uzunluk_1 670 mm"),
        md.text('Yükseklik_1 624 mm'),
        md.text('Genişlik_620 mm'),
        md.text('Yapı ağırlığı_17 kg'),
        md.text('Kova yeri sayısı_20 adet '),
        md.text('Yükleme kapasitesi_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Geri'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Mantar çiftlikleri için donatım ', ' LED aydınlatma ', ' Şirket hakkında']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Geri geldin ', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='LED aydınlatma')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Sipariş ekipmanı hesaplama', "Sokak aydınlatması ", " Endüstriyel aydınlatma ", " Ticari aydınlatma ", " Fito aydınlatma ", " Dönüş"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bölüme hoş geldiniz:", md.bold("LED aydınlatma")),
            md.text("Sizi ilgilendiren bölümü seçin!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['İptal'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Mantar çiftlikleri için donatım ", " LED aydınlatma ", " Şirket hakkında"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Eyleminiz iptal edildi', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Sokak aydınlatması'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 30 W"),
        md.text('Işık akısı _________ 4373 Lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA60',
    )
    file = open('GreenAlStreetA60.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 60 W"),
        md.text('Işık akısı _________ 8746 Lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB50',
    )
    file = open('GreenAlStreetB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 50 W"),
        md.text('Işık akısı _________ 7896 Lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB100',
    )
    file = open('GreenAlStreetB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 100 W"),
        md.text('Işık akısı _________ 15792 Lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB150',
    )
    file = open('GreenAlStreetB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 150 W"),
        md.text('Işık akısı _________ 23688 lm'),
        md.text('Renk sıcaklık ______ 5000 K '),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB200',
    )
    file = open('GreenAlStreetB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 200 W"),
        md.text('Işık akısı _________ 31584 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB250',
    )
    file = open('GreenAlStreetB250.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 240 W"),
        md.text('Işık akısı _________ 39480 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Endüstriyel aydınlatma'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 30 W"),
        md.text('Işık akısı _________ 39480 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 60 W"),
        md.text('Işık akısı _________ 8932 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 90 W"),
        md.text('Işık akısı _________ 13398 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 120 W"),
        md.text('Işık akısı _________ 17864 Lm'),
        md.text('Işık akısı _________ 17864 Lm'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 150 W"),
        md.text('Işık akısı _________ 22330 lm'),
        md.text('Renk sıcaklık ______ 5000 K '),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B50',
    )
    file = open('GreenAlPromB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 50 W"),
        md.text('Işık akısı _________ 7896 Lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B100',
    )
    file = open('GreenAlPromB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 100 W"),
        md.text('Işık akısı _________ 15792 Lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B150',
    )
    file = open('GreenAlPromB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 150 W"),
        md.text('Işık akısı _________ 23688 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B200',
    )
    file = open('GreenAlPromB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 200 W"),
        md.text('Işık akısı _________ 31584 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B240',
    )
    file = open('GreenAlPromB240.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 240 W"),
        md.text('Işık akısı _________ 36480 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Ticari aydınlatma'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 10 W"),
        md.text('Işık akısı _________ 1500 lm'),
        md.text('Renk sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 20 W"),
        md.text('Işık akısı _________ 3000 lm'),
        md.text('Renk. sıcaklık ______ 5000 K'),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Fito aydınlatma'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 30 W"),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Sitedeki detaylar",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güç ______________ 60 W"),
        md.text('Koruma derecesi _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Dönüş'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Mantar çiftlikleri için donatım ', ' LED aydınlatma ', ' Şirket hakkında']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Geri geldin ', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['Şirket hakkında'])
async def wiki_request(message: types.Message):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«GreenAl» LLC GreenAl şu ürünleri üretir:"),
            md.text('- Mantar çiftlikleri için donatım;'),
            md.text('- Endüstriyel sera kompleksleri;'),
            md.text('- Endüstriyel LED armatürler;'),
            md.text('- Güneş enerjisi için bileşenler;'),
            sep='\n'

        ),
    )


################################################################################################################################################
@dp.message_handler(state='*', text='Sipariş ekipmanı hesaplama')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("güzel gün")),
        md.text('Benim ismim ФИО'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),

@dp.message_handler(state='*', text='Sipаriş ekipmanı hesaplama')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("güzel gün")),
        md.text('Benim ismim ФИО'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),
#######################################################################################################################################################
@dp.message_handler(state='*', text='🇵🇱Polskie')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Wybrany język:", md.bold("Polskie")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Wyposażenie pieczarkarni', 'Oświetlenie LED', 'O firmie']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Cześć jestem -", md.bold("Green Al bot")),
            md.text('Chętnie Ci pomogę!'),
            md.text('Użyj klawiatury, aby rozpocząć!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Wyposażenie pieczarkarni')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["Aluminiowe stojaki do uprawy pieczarek", "Sprzęt do zbierania pieczarek",
               "Wyposażenie dodatkowe", "Wstecz"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Witamy w sekcji:", md.bold("Sprzęt dla pieczarkarni")),
            md.text("Wybierz dział, który Cię interesuje!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Oświetlenie LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["Oświetlenie uliczne", "Oświetlenie przemysłowe", "Oświetlenie komercyjne", "Fito-oświetlenie", "Powrót"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Witamy w sekcji:", md.bold("Oświetlenie LED")),
            md.text("Wybierz dział, który Cię interesuje!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['O firmie'])
    async def wiki_request(message: types.Message):
        with open('userlog.txt', 'a') as file:  # Создается текстовый файл
            # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
            file.write(
                f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«GreenAl» LLC GreenAl produkuje:"),
                md.text('- Sprzęt do pieczarkarni;'),
                md.text('- Przemysłowe kompleksy szklarniowe;'),
                md.text('- Oprawy przemysłowe LED;'),
                md.text('- Komponenty do energii słonecznej;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Wyposażenie pieczarkarni')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["Aluminiowe stojaki do uprawy pieczarek", "Sprzęt do zbierania pieczarek",
               "Wyposażenie dodatkowe", "Wstecz"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Witamy w sekcji:", md.bold("Sprzęt dla pieczarkarni")),
            md.text("Wybierz dział, który Cię interesuje!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Anulowanie'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Wyposażenie pieczarkarni", "Oświetlenie LED", "O firmie"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ваше действие отменено', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Aluminiowe stojaki do uprawy pieczarek'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Aluminiowe stojaki do uprawy pieczarek, ',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Długość regału_30,0 m (standard)"),
        md.text('Szerokość (wewnętrzna) _ 1,34 m (standard)'),
        md.text('Szerokość (nar.) _ 1,5 m (standard)'),
        md.text('Wysokość regału_ od 2,8 do 5,0 m'),
        md.text('Liczba tiers_ od 3 do 7 sztuk'),
        md.text('Rozstaw podpór: 1,5 / 3 m'),
        md.text('Wysokość pokładu (półki) _600 mm'),
        md.text('Wysokość deski bocznej_180 mm'),
        md.text('Stała waga stojak_1 900 kg'),
        md.text('Obciążenie obliczeniowe_195 kg/m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Sprzęt do zbierania pieczarek'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Тележка подвесная Standart для сбора шампиньонов',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Ширина_1 950 мм"),
        md.text('Высота_3 130 мм'),
        md.text('Глубина_610 мм'),
        md.text('Вес_59 кг'),
        md.text('Грузоподъемность_170 кг'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Тележка напольная для сбора шампиньонов',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Вес конструкции_15 кг"),
        md.text('Грузоподъемность_150 кг'),
        md.text('Материал сиденья_Пластик'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Платформа для сбора шампиньонов',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Длина_1000 мм"),
        md.text('Высота_1125 мм'),
        md.text('Ширина_535 мм'),
        md.text('Вес платформы_16 кг'),
        md.text('Вес табурета_5 кг'),
        md.text('Размер ячейки для весов_330*360 мм'),
        md.text('Нагрузка на 1 ряд_10  кг'),
        md.text('Количество рядов для размещения полок_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Дополнительное оборудование'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Стенд для зарядки весов',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Высота_1300 мм"),
        md.text('Длина_1000 мм'),
        md.text('Ширина_800 мм'),
        md.text('Количество мест_20 шт'),
        md.text('Размер ячейки для весов_330*360 мм'),
        md.text('Вес конструкции_38 кг'),
        md.text('Нагрузка на одну ячейку_25 кг'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Стенд для зарядки весов с розетками',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Высота_1300 мм"),
        md.text('Длина_1000 мм'),
        md.text('Ширина_800 мм'),
        md.text('Количество мест_20 шт'),
        md.text('Размер ячейки для весов_330*360 мм'),
        md.text('Вес конструкции_38 кг'),
        md.text('Нагрузка на одну ячейку_25 кг'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Сушилка для ведер',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Длина_1 670 мм"),
        md.text('Высота_1 624 мм'),
        md.text('Ширина_620 мм'),
        md.text('Вес конструкции_17 кг'),
        md.text('Количество мест для ведер_20 шт'),
        md.text('Грузоподъемность_120 кг'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Назад'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Оборудование для грибных ферм', 'LED светодиодное освещение', 'О компании']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Вы вернулсь назад ', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='LED светодиодное освещение')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["Уличное освещение", "Промышленное освещение", "Торговое освещение", "Фито-освещение", "Возврат"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Добро пожаловать в раздел:", md.bold("LED светодиодное освещение")),
            md.text("Выберите раздел который вам интересен!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Отмена'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Оборудование для грибных ферм", "LED светодиодное освещение", "О компании"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ваше действие отменено', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Уличное освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button),
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________30 Вт"),
        md.text('Световой поток_________4373 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA60',
    )
    file = open('GreenAlStreetA60.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________60 Вт"),
        md.text('Световой поток_________8746 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB50',
    )
    file = open('GreenAlStreetB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________50 Вт"),
        md.text('Световой поток_________7896 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB100',
    )
    file = open('GreenAlStreetB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________100 Вт"),
        md.text('Световой поток_________15792 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB150',
    )
    file = open('GreenAlStreetB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________150 Вт"),
        md.text('Световой поток_________23688 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB200',
    )
    file = open('GreenAlStreetB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________200 Вт"),
        md.text('Световой поток_________31584 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetB250',
    )
    file = open('GreenAlStreetB250.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________240 Вт"),
        md.text('Световой поток_________39480 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Промышленное освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________30 Вт"),
        md.text('Световой поток_________39480 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________60 Вт"),
        md.text('Световой поток_________8932 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________90 Вт"),
        md.text('Световой поток_________13398 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________120 Вт"),
        md.text('Световой поток_________17864 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________150 Вт"),
        md.text('Световой поток_________22330 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B50',
    )
    file = open('GreenAlPromB50.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________50 Вт"),
        md.text('Световой поток_________7896 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B100',
    )
    file = open('GreenAlPromB100.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________100 Вт"),
        md.text('Световой поток_________15792 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B150',
    )
    file = open('GreenAlPromB150.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________150 Вт"),
        md.text('Световой поток_________23688 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B200',
    )
    file = open('GreenAlPromB200.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________200 Вт"),
        md.text('Световой поток_________31584 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom B240',
    )
    file = open('GreenAlPromB240.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробности на сайте!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________240 Вт"),
        md.text('Световой поток_________36480 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Торговое освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________10 Вт"),
        md.text('Световой поток_________1500 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________20 Вт"),
        md.text('Световой поток_________3000 Лм'),
        md.text('Цвет. температура______5000 К'),
        md.text('Степень защиты_________IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Фито-освещение'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________30 Вт"),
        md.text('Степень защиты_________IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на сайт продукта",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Мощность______________60 Вт"),
        md.text('Степень защиты_________IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Возврат'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Оборудование для грибных ферм', 'LED светодиодное освещение', 'О компании']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Вы вернулсь назад ', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['О компании'])
async def wiki_request(message: types.Message):
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«ООО «ГринАл» GreenAl изготавливает продукцию:"),
            md.text('- Оборудование для грибных ферм;'),
            md.text('- Промышленные тепличные комплексы;'),
            md.text('- Промышленные светодиодные светильники;'),
            md.text('- Комплектующие для солнечной энергетики;'),
            sep='\n'

        ),
    )
################################################################################################################################################
@dp.message_handler(state='*', text='Sipariş ekipmanı hesaplama')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("güzel gün")),
        md.text('Benim ismim ФИО'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),

@dp.message_handler(state='*', text='Sipаriş ekipmanı hesaplama')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("", md.bold("güzel gün")),
        md.text('Benim ismim ФИО'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),

##################################################################################################################################################

executor.start_polling(dp, skip_updates=True)
