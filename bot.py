import logging
import random
import string
import aiogram.utils.markdown as md

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from aiogram.utils import executor


logging.basicConfig(level=logging.DEBUG)

BOT_TOKEN = '1770141520:AAFPzGv7eRssdexLzbmVzrAe7ld5j8Q6L_M'

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

@dp.message_handler(commands="start", state="*")
async def start_cmd(message: types.Message):
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
            md.text("Здравствуйте, я -", md.bold("GreenAl bot")),
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
    buttons = ['✏️Закaзать расчёт оборудoвания', "Аллюминевые стеллажи для выращивания грибов, шампиньонов",
               "Оборудование для сбора шампиньонов",
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
    buttons = ['✏️Заказать рaсчёт оборудования', "Уличное освещение", "Промышленное освещение", "Торговое освещение",
               "Фито-освещение", "Возврат"]
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
    buttons = ['✏️Закaзать расчёт оборудoвания', "Аллюминевые стеллажи для выращивания грибов, шампиньонов",
               "Оборудование для сбора шампиньонов",
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


@dp.message_handler(state='*', text=['Оборудование для сбора шамьпиньонов'])
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
    await bot.send_message(message.chat.id, 'Вы вернулись назад ', reply_markup=keyboard)


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
    buttons = ['✏️Заказать рaсчёт оборудования', "Уличное освещение", "Промышленное освещение", "Торговое освещение",
               "Фито-освещение", "Возврат"]
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
    await bot.send_message(message.chat.id, 'Вы вернулись назад ', reply_markup=keyboard)


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
@dp.message_handler(state='*', text='✏️Заказать рaсчёт оборудования')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать консультанту!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Здравствуйте!"),
        md.text('Готов ответить на все ваши вопросы!'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Закaзать расчёт оборудoвания')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать консультанту!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Здравствуйте!"),
        md.text('Готов ответить на все ваши вопросы!'),
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
            md.text("Hi, I'm-", md.bold("GreenAl bot")),
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
    buttons = ['✏️Ordеr equipment calculation', "Aluminum racks for growing mushrooms, champignons ",
               " Equipment for collecting chappignons ",
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
    buttons = ['✏️Order equipment calculation', "Street lighting ", " Industrial lighting ", " Commercial lighting ",
               " Phyto-lighting ", " Return"]
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
    buttons = ['Ordеr equipment calculation', "Aluminum racks for growing mushrooms, champignons ",
               " Equipment for collecting chappignons ",
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
    buttons = ['✏️Order equipment calculation', "Street lighting ", " Industrial lighting ", " Commercial lighting ",
               " Phyto-lighting ", " Return"]
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
@dp.message_handler(state='*', text='✏️Order equipment calculation')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Write to a consultant!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Good day!"),
        md.text('My name is Ilnar'),
        md.text('For ordering equipment, please contact me!'),
        md.text('Always happy to help you'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Ordеr equipment calculation')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Write to a consultant!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Good day!"),
        md.text('My name is Marat'),
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
            md.text("Merhaba ben -", md.bold("GreenAl bot")),
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
    buttons = ['✏️Sipаriş ekipmanı hesaplama', "Mantar, petrol yetiştirmek için alüminyum raflar ",
               " Şappignon toplama ekipmanı ", "Ek donanım",
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
    buttons = ['✏️Sipariş ekipmanı hesaplama', "Sokak aydınlatması ", " Endüstriyel aydınlatma ", " Ticari aydınlatma ",
               " Fito aydınlatma ", " Dönüş"]
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
    buttons = ['✏️Sipаriş ekipmanı hesaplama', "Mantar, petrol yetiştirmek için alüminyum raflar ",
               " Şappignon toplama ekipmanı ", "Ek donanım",
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
    btns = ["✏️Sipаriş ekipmanı hesaplama", " LED aydınlatma ", " Şirket hakkında"]
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
    buttons = ['✏️Sipariş ekipmanı hesaplama', "Sokak aydınlatması ", " Endüstriyel aydınlatma ", " Ticari aydınlatma ",
               " Fito aydınlatma ", " Dönüş"]
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
@dp.message_handler(state='*', text='✏️Sipariş ekipmanı hesaplama')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("güzel gün"),
        md.text('Benim ismim Ilnar'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Sipаriş ekipmanı hesaplama')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("güzel gün"),
        md.text('Benim ismim Marat'),
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
    buttons = ['Wyposażenie pieczarkarni', 'Oświetlenie ledowe', 'O firmie']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Cześć jestem -", md.bold("GreenAl bot")),
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
    buttons = ['✏️Zаmów kalkulację wyposażenia', "Aluminiowe stojaki do uprawy pieczarek",
               "Sprzęt do zbierania pieczarek",
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


@dp.message_handler(state='*', text='Oświetlenie ledowe')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Zamów kalkulację wyposażenia', "Oświetlenie uliczne", "Oświetlenie przemysłowe",
               "Oświetlenie komercyjne", "Fito-oświetlenie", "Powrót"]
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
    buttons = ['✏️Zаmów kalkulację wyposażenia', "Aluminiowe stojaki do uprawy pieczarek",
               "Sprzęt do zbierania pieczarek",
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
    btns = ["Wyposażenie pieczarkarni", "Oświetlenie ledowe", "O firmie"]
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
        'Wózek wiszący Standart do zbierania pieczarek',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Szerokość_1 950 mm"),
        md.text('Wysokość_3 130 mm'),
        md.text('Głębokość_610 mm'),
        md.text('Waga_59 kg'),
        md.text('Ładowność_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Wózek podłogowy do zbierania pieczarek',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Waga konstrukcji_15 kg"),
        md.text('Ładowność_150 kg'),
        md.text('Materiał siedziska_Plastik'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Platforma do zbierania grzybów',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Długość_1000 mm"),
        md.text('Wysokość_1125 mm'),
        md.text('Szerokość_535 mm'),
        md.text('Waga platformy_16 kg'),
        md.text('Waga stołka_5 kg'),
        md.text('Rozmiar komórki dla wag_330 * 360 mm'),
        md.text('Obciążenie dla 1 rzędu_10 kg'),
        md.text('Liczba rzędów na półki_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Wyposażenie dodatkowe'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Podstawka do ładowania wagi',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Wysokość_1300 mm"),
        md.text('Długość_1000 mm'),
        md.text('Szerokość_800 mm'),
        md.text('Liczba miejsc_20 szt'),
        md.text('Rozmiar komórki dla wag_330 * 360 mm'),
        md.text('Masa konstrukcji_38 kg'),
        md.text('Obciążenie na ogniwo_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Podstawka do ładowania wagi z gniazdami',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Wysokość_1300 mm"),
        md.text('Długość_1000 mm'),
        md.text('Szerokość_800 mm'),
        md.text('Liczba miejsc_20 szt'),
        md.text('Rozmiar komórki dla wag_330 * 360 mm'),
        md.text('Masa konstrukcji_38 kg'),
        md.text('Obciążenie na ogniwo_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Suszarka do wiader',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Długość_1 670 mm"),
        md.text('Wysokość_1 624 mm'),
        md.text('Szerokość_620 mm'),
        md.text('Masa konstrukcji_17 kg'),
        md.text('Ilość miejsc na wiadra_20 szt'),
        md.text('Ładowność_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Wstecz'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Wyposażenie pieczarkarni', 'Oświetlenie ledowe', 'O firmie']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Wróciłeś ', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='Oświetlenie ledowe')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Zamów kalkulację wyposażenia', "Oświetlenie uliczne", "Oświetlenie przemysłowe",
               "Oświetlenie komercyjne", "Fito-oświetlenie", "Powrót"]
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


@dp.message_handler(state='*', text=['Anulowanie'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Wyposażenie pieczarkarni ", " Oświetlenie ledowe ", " O firmie"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Twoja akcja została anulowana', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Oświetlenie uliczne'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 30 W"),
        md.text('Strumień świetlny _________ 4373 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 60 W"),
        md.text('Strumień świetlny _________ 8746 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Stopień ochrony _________ IP67"),
        md.text('Strumień świetlny _________ 7896 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 100 W"),
        md.text('Strumień świetlny _________ 15792 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 150 W"),
        md.text('Strumień świetlny _________ 23688 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 200 W"),
        md.text('Strumień świetlny _________ 31584 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 240 W"),
        md.text('Strumień świetlny _________ 39480 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Oświetlenie przemysłowe'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 30 W"),
        md.text('Strumień świetlny _________ 39480 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 60 W"),
        md.text('Strumień świetlny _________ 8932 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 90 W"),
        md.text('Strumień świetlny _________ 13398 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 120 W"),
        md.text('Strumień świetlny _________ 17864 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 150 W"),
        md.text('Strumień świetlny _________ 22330 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 50 W"),
        md.text('Strumień świetlny _________ 7896 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 100 W"),
        md.text('Strumień świetlny _________ 15792 Lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 150 W"),
        md.text('Strumień świetlny _________ 23688 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 200 W"),
        md.text('Strumień świetlny _________ 31584 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 240 W"),
        md.text('Strumień świetlny _________ 36480 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Oświetlenie komercyjne'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 10 W"),
        md.text('Strumień świetlny _________ 1500 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 20 W"),
        md.text('Strumień świetlny _________ 3000 lm'),
        md.text('Kol. temperatura ______ 5000 K'),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Fito-oświetlenie'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 30 W"),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Szczegóły na stronie!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Moc ______________ 60 W"),
        md.text('Stopień ochrony _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Powrót'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Wyposażenie pieczarkarni', 'Oświetlenie LED', 'O firmie']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Wróciłeś ', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['O firmie'])
async def wiki_request(message: types.Message):
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


################################################################################################################################################
@dp.message_handler(state='*', text='✏️Zamów kalkulację wyposażenia')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güzel gün"),
        md.text('Benim ismim Ilnar'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Zаmów kalkulację wyposażenia')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Bir danışmana yaz",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Güzel gün"),
        md.text('Benim ismim Marat'),
        md.text('Ekipman siparişi ile ilgili herhangi bir sorunuz varsa, lütfen benimle iletişime geçin!'),
        md.text('Sana yardım etmekten her zaman mutluluk duyarım'),
        sep='\n'

    ), reply_markup=keyboard),


##################################################################################################################################################

###############################################################################################################################################################

@dp.message_handler(state='*', text='🇩🇪Deutsch')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Ausgewählte Sprache:", md.bold("Deutsch")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Ausrüstung für Pilzfarmen ', ' LED-Beleuchtung ', ' Über das Unternehmen']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Hallo ich bin -", md.bold("GreenAl bot")),
            md.text('Ich helfe Ihnen gerne weiter!'),
            md.text('Verwenden Sie Ihre Tastatur, um loszulegen!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Ausrüstung für Pilzfarmen')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["✏️ Bеstellen Sie eine Berechnung der Ausrüstung",
               "Aluminiumregale für den Anbau von Pilzen, Champignons", "Ausrüstung zum Sammeln von Chappignons",
               "Zusatzausrüstung", "Zurück"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Willkommen in der Sektion:", md.bold("Ausrüstung für Pilzfarmen")),
            md.text("Wählen Sie den Bereich, der Sie interessiert!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='LED-Beleuchtung')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Bestellgeräteberechnung ', "Straßenbeleuchtung", "Industriebeleuchtung", "Gewerbliche Beleuchtung",
               "Phyto-Beleuchtung", "Rückkehr"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Willkommen in der Sektion:", md.bold("LED-Beleuchtung")),
            md.text("Wählen Sie den Bereich, der Sie interessiert!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['Über das Unternehmen'])
    async def wiki_request(message: types.Message):
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«GreenAl» LLC GreenAl stellt Produkte her:"),
                md.text('- Ausrüstung für Pilzfarmen;'),
                md.text('- Industrielle Gewächshauskomplexe;'),
                md.text('- Industrielle LED-Leuchten;'),
                md.text('- Komponenten für Solarenergie;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Ausrüstung für Pilzfarmen')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["✏️ Bеstellen Sie eine Berechnung der Ausrüstung",
               "Aluminiumregale für den Anbau von Pilzen, Champignons", "Ausrüstung zum Sammeln von Chappignons",
               "Zusatzausrüstung", "Zurück"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Willkommen in der Sektion:", md.bold("Ausrüstung für Pilzfarmen")),
            md.text("Wählen Sie den Bereich, der Sie interessiert!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Zurück'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Ausrüstung für Pilzfarmen", " LED-Beleuchtung", " Über das Unternehmen"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ihre Aktion wird abgebrochen', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Aluminiumregale für den Anbau von Pilzen, Champignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Aluminiumregale für den Anbau von Pilzen, Champignons',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Gestelllänge_30,0 m (Standard)"),
        md.text('Breite (innen) _ 1,34 m (Standard)'),
        md.text('Breite (außen) _ 1,5 m (Standard)'),
        md.text('Rackhöhe_von 2,8 bis 5,0 m'),
        md.text('Rackhöhe_von 2,8 bis 5,0 m'),
        md.text('Stützsäulenabstand_1,5 / 3 m'),
        md.text('Deckhöhe (Regalhöhe) _600 mm'),
        md.text('Seitenplattenhöhe_180 mm'),
        md.text('Gewicht const. Rack_1 900 kg'),
        md.text('Auslegungslast_195 kg / m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Ausrüstung zum Sammeln von Chappignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Hängender Wagen Standart zum Sammeln von Champignons',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Breite_1 950 mm"),
        md.text('Höhe_3 130 mm'),
        md.text('Tiefe_610 mm'),
        md.text('Gewicht_59 kg'),
        md.text('Tragfähigkeit_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Bodenwagen zum Sammeln von Champignons',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Strukturgewicht_15 kg"),
        md.text('Tragfähigkeit_150 kg'),
        md.text('Sitzmaterial_Kunststoff'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Pilzpflückplattform',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Länge_1000 mm"),
        md.text('Höhe_1125 mm'),
        md.text('Breite_535 mm'),
        md.text('Plattformgewicht_16 kg'),
        md.text('Stuhlgewicht_5 kg'),
        md.text('Zellengröße für Waage_330 * 360 mm'),
        md.text('Last für 1 Reihe_10 kg'),
        md.text('Anzahl der Reihen für Regale_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Zusatzausrüstung'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Ladestation skalieren',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Höhe_1300 mm"),
        md.text('Länge_1000 mm'),
        md.text('Breite_800 mm'),
        md.text('Anzahl der Sitze_20 Stk'),
        md.text('Zellengröße für Waage_330 * 360 mm'),
        md.text('Baugewicht_38 kg'),
        md.text('Belastung pro Zelle_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Waage Ladestation mit Steckdosen',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Höhe_1300 mm"),
        md.text('Länge_1000 mm'),
        md.text('Breite_800 mm'),
        md.text('Anzahl der Sitze_20 Stk'),
        md.text('Zellengröße für Waage_330 * 360 mm'),
        md.text('Baugewicht_38 kg'),
        md.text('Belastung pro Zelle_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Trockner für Eimer',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Länge_1 670 mm"),
        md.text('Höhe_1 624 mm'),
        md.text('Breite_620 mm'),
        md.text('Baugewicht_17 kg'),
        md.text('Anzahl der Plätze für Eimer_20 Stk'),
        md.text('Tragfähigkeit_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Zurück'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Ausrüstung für Pilzfarmen ',' LED-Beleuchtung ',' Über das Unternehmen"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ihre Aktion wird abgebrochen', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='LED-Beleuchtung')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Bestellgeräteberechnung ', "Straßenbeleuchtung", "Industriebeleuchtung", "Gewerbliche Beleuchtung",
               "Phyto-Beleuchtung", "Rückkehr"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Willkommen in der Sektion:", md.bold("LED-Beleuchtung")),
            md.text("Wählen Sie den Bereich, der Sie interessiert!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Rückkehr'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Ausrüstung für Pilzfarmen ", " LED-Beleuchtung ", "Über das Unternehmen"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ihre Aktion wird abgebrochen', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Straßenbeleuchtung'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 30 W"),
        md.text('Lichtstrom _________ 4373 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 60 W"),
        md.text('Lichtstrom _________ 8746 Lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 50 W"),
        md.text('Lichtstrom _________ 7896 Lm'),
        md.text('Farbe. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 100 W"),
        md.text('Lichtstrom _________ 15792 Lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Stärke des Schutzes_________IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 150 W"),
        md.text('Lichtstrom _________ 23688 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 200 W"),
        md.text('Lichtstrom _________ 31584 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 240 W"),
        md.text('Lichtstrom _________ 39480 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Industriebeleuchtung'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 30 W"),
        md.text('Lichtstrom _________ 39480 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 60 W"),
        md.text('Lichtstrom _________ 8932 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 90 W"),
        md.text('Lichtstrom _________ 13398 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 120 W"),
        md.text('Lichtstrom _________ 17864 Lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 150 W"),
        md.text('Lichtstrom _________ 22330 lm'),
        md.text('Farbe. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 50 W"),
        md.text('Lichtstrom _________ 7896 Lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 100 W"),
        md.text('Lichtstrom _________ 15792 Lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 150 W"),
        md.text('Lichtstrom _________ 23688 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 200 W"),
        md.text('Lichtstrom _________ 31584 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 240 W"),
        md.text('Lichtstrom _________ 36480 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Gewerbliche Beleuchtung'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 10 W"),
        md.text('Lichtstrom _________ 1500 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 20 W"),
        md.text('Lichtstrom _________ 3000 lm'),
        md.text('Far. Temperatur ______ 5000 K'),
        md.text('Schutzart _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Phyto-Beleuchtung'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 30 W"),
        md.text('Schutzart _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Details auf der Seite!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Leistung ______________ 60 W"),
        md.text('Schutzart _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Rückkehr'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Ausrüstung für Pilzfarmen ", " LED-Beleuchtung ", "Über das Unternehmen"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ihre Aktion wird abgebrochen', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['Über das Unternehmen'])
async def wiki_request(message: types.Message):
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«GreenAl» LLC GreenAl stellt Produkte her:"),
            md.text('- Ausrüstung für Pilzfarmen;'),
            md.text('- Industrielle Gewächshauskomplexe;'),
            md.text('- Industrielle LED-Leuchten;'),
            md.text('- Komponenten für Solarenergie;'),
            sep='\n'

        ),
    )


#################################################################################################################################################
@dp.message_handler(state='*', text='✏️Bestellgeräteberechnung')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Schreiben Sie an einen Berater!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Guten Tag!"),
        md.text('Ich heiße Ilnar'),
        md.text('Für die Bestellung von Geräten kontaktieren Sie mich bitte!'),
        md.text('Immer gerne für Sie da'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️ Bеstellen Sie eine Berechnung der Ausrüstung')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Schreiben Sie an einen Berater!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Guten Tag!"),
        md.text('Ich heiße Marat'),
        md.text('Für die Bestellung von Geräten kontaktieren Sie mich bitte!'),
        md.text('Immer gerne für Sie da'),
        sep='\n'

    ), reply_markup=keyboard),


########################################################################################################################################################

###################################################################################################################################################################

@dp.message_handler(state='*', text='🇫🇷Français')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Langue sélectionnée:", md.bold("Français")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Équipement pour les champignonnières', 'Éclairage LED', 'À propos de l']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Salut je suis -", md.bold("GreenAl bot")),
            md.text('Je serai ravi de vous aider!'),
            md.text('Utilisez votre clavier pour commencer!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Équipement pour les champignonnières')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Calcul dе l équipement de commande',
               "Supports en aluminium pour la culture de champignons, champignons",
               "Matériel pour la collecte de champignons",
               "Équipement optionel", "Retour à"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenue dans la section:", md.bold("Équipement pour les champignonnières")),
            md.text("Choisissez la section qui vous intéresse!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Éclairage LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Cаlcul de l équipement de commande', "Réverbères", "Éclairage industriel", "Éclairage commercial",
               "Phyto-éclairage", "Revenir"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenue dans la section:", md.bold("Éclairage LED")),
            md.text("Choisissez la section qui vous intéresse!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['À propos de l'])
    async def wiki_request(message: types.Message):
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«GreenAl» LLC GreenAl fabrique des produits:"),
                md.text('- Équipement pour les fermes de champignons;'),
                md.text('- Complexes de serres industrielles;'),
                md.text('- Luminaires industriels à LED;'),
                md.text('- Composants pour lénergie solaire;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Équipement pour les champignonnières')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Calcul dе l équipement de commande',
               "Supports en aluminium pour la culture de champignons, champignons",
               "Matériel pour la collecte de champignons",
               "Équipement optionel", "Retour à"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenue dans la section:", md.bold("Équipement pour les champignonnières")),
            md.text("Choisissez la section qui vous intéresse!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Annulation'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Équipement pour les champignonnières", "Éclairage LED", "À propos de l"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Votre action est annulée', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Supports en aluminium pour la culture de champignons, champignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Supports en aluminium pour la culture de champignons, champignons',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Longueur du rack_30,0 m (standard)"),
        md.text('Largeur (intérieure) _ 1,34 m (standard)'),
        md.text('Largeur (sortie) _ 1,5 m (standard)'),
        md.text('Hauteur du rack_de 2,8 à 5,0 m'),
        md.text('Nombre détages_de 3 à 7 pièces'),
        md.text('Espacement des colonnes de support_1,5 / 3 m'),
        md.text('Hauteur du plateau (étagère) _600 mm'),
        md.text('Hauteur du panneau latéral_180 mm'),
        md.text('Poids const. rack_1 900 kg'),
        md.text('Charge de conception_195 kg / m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Matériel pour la collecte de champignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Chariot suspendu Standart pour la collecte de champignons',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Largeur_1 950 mm"),
        md.text('Hauteur_3 130 mm'),
        md.text('Profondeur_610 mm'),
        md.text('Poids_59 kg'),
        md.text('Capacité de chargement_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Chariot au sol pour la collecte des champignons',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Poids de la structure_15 kg"),
        md.text('Capacité de chargement_150 kg'),
        md.text('Matériau du siège_Plastique'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Plateforme de cueillette de champignons',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Longueur_1000 mm"),
        md.text('Hauteur_1125 mm'),
        md.text('Largeur_535 mm'),
        md.text('Poids de la plate-forme_16 kg'),
        md.text('Poids du tabouret_5 kg'),
        md.text('Taille de cellule pour les balances_330 * 360 mm'),
        md.text('Charge pour 1 rangée_10 kg'),
        md.text('Nombre de rangées pour les étagères_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Équipement optionel'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Support de chargement de balance',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Hauteur_1300 mm"),
        md.text('Longueur_1000 mm'),
        md.text('Largeur_800 mm'),
        md.text('Nombre de places_20 pcs'),
        md.text('Taille de cellule pour les balances_330 * 360 mm'),
        md.text('Poids de construction_38 kg'),
        md.text('Charge par cellule_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Support de charge pour balance avec prises',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Hauteur_1300 mm"),
        md.text('Longueur_1000 mm'),
        md.text('Largeur_800 mm'),
        md.text('Nombre de places_20 pcs'),
        md.text('Taille de cellule pour les balances_330 * 360 mm'),
        md.text('Poids de construction_38 kg'),
        md.text('Charge par cellule_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Séchoir pour seaux',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Longueur_1 670 mm"),
        md.text('Hauteur_1 624 mm'),
        md.text('Largeur_620 mm'),
        md.text('Poids de construction_17 kg'),
        md.text('Nombre de places pour seaux_20 pcs'),
        md.text('Capacité de chargement_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Retour à'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Équipement pour les champignonnières", "Éclairage LED", "À propos de l"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Tu es revenu', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='Éclairage LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Cаlcul de l équipement de commande', "Réverbères", "Éclairage industriel", "Éclairage commercial",
               "Phyto-éclairage", "Revenir"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenue dans la section:", md.bold("Éclairage LED")),
            md.text("Choisissez la section qui vous intéresse!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Annulation'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Équipement pour les champignonnières", "Éclairage LED", "À propos de l"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Votre action est annulée', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Réverbères'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 30 W"),
        md.text('Flux lumineux _________ 4373 lm'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 60 W"),
        md.text('Flux lumineux _________ 8746 Lm'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 50 Вт"),
        md.text('Flux lumineux _________ 7896 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 100 Вт"),
        md.text('Flux lumineux _________ 15792 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 150 Вт"),
        md.text('Flux lumineux _________ 23688 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 200 Вт"),
        md.text('Flux lumineux _________ 31584 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 240 Вт"),
        md.text('Flux lumineux _________ 39480 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Éclairage industriel'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 30 Вт"),
        md.text('Flux lumineux _________ 39480 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 60 Вт"),
        md.text('Flux lumineux _________ 8932 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 90 Вт"),
        md.text('Flux lumineux _________ 13398 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 120 Вт"),
        md.text('Flux lumineux _________ 17864 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 150 Вт"),
        md.text('Flux lumineux _________ 22330 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 50 Вт"),
        md.text('Flux lumineux _________ 7896 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 100 Вт"),
        md.text('Flux lumineux _________ 15792 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 150 Вт"),
        md.text('Flux lumineux _________ 23688 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 200 Вт"),
        md.text('Flux lumineux _________ 31584 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 240 Вт"),
        md.text('Flux lumineux _________ 36480 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Éclairage commercial'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 10 Вт"),
        md.text('Flux lumineux _________ 1500 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 20 Вт"),
        md.text('Flux lumineux _________ 3000 Лм'),
        md.text('Coul. température ______ 5000 K'),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Phyto-éclairage'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 30 Вт"),
        md.text('Degré de protection _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Détails sur le site!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Puissance ______________ 60 Вт"),
        md.text('Degré de protection _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Revenir'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Équipement pour les champignonnières", "Éclairage LED", "À propos de l"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Tu es revenu ', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['À propos de l'])
async def wiki_request(message: types.Message):
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«GreenAl» LLC GreenAl fabrique des produits:"),
            md.text('- Équipement pour les fermes de champignons;'),
            md.text('- Complexes de serres industrielles;'),
            md.text('- Luminaires industriels à LED;'),
            md.text('- Composants pour lénergie solaire;'),
            sep='\n'

        ),
    )


#################################################################################################################################################
@dp.message_handler(state='*', text='✏️Cаlcul de l équipement de commande')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Écrivez à un consultant!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Bonne journée!"),
        md.text('Je m appelle Ilnar'),
        md.text('Pour commander du matériel, merci de me contacter!'),
        md.text('Toujours heureux de vous aider'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Calcul dе l équipement de commande')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Écrivez à un consultant!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Добрый день!"),
        md.text('Меня зовут Марат'),
        md.text('По вопросам заказа оборудывания обращайтесь комне!'),
        md.text('Всегда рад помочь вам'),
        sep='\n'

    ), reply_markup=keyboard),


#########################################################################################################################################################################3

############################################################################################################################################################

@dp.message_handler(state='*', text='🇮🇹Italiano')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Lingua selezionata:", md.bold("Italiano")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ["Attrezzature per fungaie", "Illuminazione a LED", "Informazioni sull azienda"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Ciao sono -", md.bold("GreenAl bot")),
            md.text('Sarò felice di aiutarti!'),
            md.text('Usa la tastiera per iniziare!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Attrezzature per fungaie')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Ordina il calcolo dell attrezzatura',
               "Rastrelliere in alluminio per la coltivazione di funghi, funghi prataioli",
               "Attrezzatura per la raccolta dei chappignon",
               "Attrezzatura aggiuntiva", "Indietro"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Benvenuto nella sezione:", md.bold("Attrezzature per fungaie")),
            md.text("Scegli la sezione che ti interessa!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Illuminazione a LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True)
    buttons = ["✏️Cаlcolo dell attrezzatura dell ordine", "Illuminazione stradale", "Illuminazione industriale",
               "Illuminazione commerciale",
               "Fitoilluminazione", "Ritorno"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Benvenuto nella sezione:", md.bold("Illuminazione a LED")),
            md.text("Scegli la sezione che ti interessa!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['Informazioni sull azienda'])
    async def wiki_request(message: types.Message):
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«ООО «GreenAl» GreenAl realizza prodotti:"),
                md.text('- Attrezzature per fungaie;'),
                md.text('- Complessi di serre industriali;'),
                md.text('- Apparecchi di illuminazione a LED industriali;'),
                md.text('- Componenti per energia solare;'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Attrezzature per fungaie')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Ordina il calcolo dell attrezzatura',
               "Rastrelliere in alluminio per la coltivazione di funghi, funghi prataioli",
               "Attrezzatura per la raccolta dei chappignon",
               "Attrezzatura aggiuntiva", "Indietro"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Benvenuto nella sezione:", md.bold("Attrezzature per fungaie")),
            md.text("Scegli la sezione che ti interessa!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Indietro'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Attrezzature per fungaie", "Illuminazione a LED", "Informazioni sull azienda"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'La tua azione è stata annullata', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Rastrelliere in alluminio per la coltivazione di funghi, funghi prataioli'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Rastrelliere in alluminio per la coltivazione di funghi, funghi prataioli',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Lunghezza rack_30,0 m (standard)"),
        md.text('Larghezza (interna) _ 1,34 m (standard)'),
        md.text('Larghezza (fuori) _ 1,5 m (standard)'),
        md.text('Altezza rack_da 2,8 a 5,0 m'),
        md.text('Numero di livelli_da 3 a 7 pezzi'),
        md.text('Interasse colonne di supporto_1,5 / 3 m'),
        md.text('Altezza piano (ripiano) _600 mm'),
        md.text('Altezza pannello laterale_180 mm'),
        md.text('Cost. Peso cremagliera_1 900 kg'),
        md.text('Carico di progetto_195 kg / m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Attrezzatura per la raccolta dei chappignon'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Carrello sospeso Standart per la raccolta di funghi prataioli',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Larghezza_1 950 mm"),
        md.text('Altezza_3 130 mm'),
        md.text('Profondità_610 mm'),
        md.text('Peso_59 kg'),
        md.text('Capacità di carico_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Carrello da pavimento per la raccolta dei funghi prataioli',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Peso struttura_15 kg"),
        md.text('Capacità di carico_150 kg'),
        md.text('Materiale sedile_Plastica'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Piattaforma per la raccolta dei funghi',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Lunghezza_1000 mm"),
        md.text('Altezza_1125 mm'),
        md.text('Larghezza_535 mm'),
        md.text('Peso piattaforma_16 kg'),
        md.text('Peso sgabello_5 kg'),
        md.text('Dimensione cella per scale_330 * 360 mm'),
        md.text('Carico per 1 fila_10 kg'),
        md.text('Numero di file per ripiani_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Attrezzatura aggiuntiva'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Supporto di ricarica in scala',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Altezza_1300 mm"),
        md.text('Lunghezza_1000 mm'),
        md.text('Larghezza_800 mm'),
        md.text('Numero di posti_20 pezzi'),
        md.text('Dimensione cella per scale_330 * 360 mm'),
        md.text('Peso di costruzione_38 kg'),
        md.text('Carico per cella_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Supporto di ricarica in scala con prese',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Altezza_1300 mm"),
        md.text('Lunghezza_1000 mm'),
        md.text('Larghezza_800 mm'),
        md.text('Numero di posti_20 pz'),
        md.text('Dimensione cella per scale_330 * 360 mm'),
        md.text('Peso di costruzione_38 kg'),
        md.text('Carico per cella_25 kg'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Lunghezza_1 670 mm"),
        md.text('Altezza_1 624 mm'),
        md.text('Larghezza_620 mm'),
        md.text('Peso di costruzione_17 kg'),
        md.text('Numero di posti per secchi_20 pz'),
        md.text('Capacità di carico_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Indietro'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Attrezzature per fungaie", "Illuminazione a LED", "Informazioni sull azienda"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Sei tornato', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='Illuminazione a LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True)
    buttons = ["✏️Cаlcolo dell attrezzatura dell ordine", "Illuminazione stradale", "Illuminazione industriale",
               "Illuminazione commerciale",
               "Fitoilluminazione", "Ritorno"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Benvenuto nella sezione:", md.bold("Illuminazione a LED")),
            md.text("Scegli la sezione che ti interessa!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Ritorno'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Attrezzature per fungaie", "Illuminazione a LED", "Informazioni sull azienda"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'La tua azione è stata annullata', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Illuminazione stradale'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 30 W"),
        md.text('Flusso luminoso _________ 4373 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="c",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 60 W"),
        md.text('Flusso luminoso _________ 8746 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 50 W"),
        md.text('Flusso luminoso _________ 7896 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 100 W"),
        md.text('Flusso luminoso _________ 15792 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 150 W"),
        md.text('Flusso luminoso _________ 23688 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 200 W"),
        md.text('Flusso luminoso _________ 31584 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 240 W"),
        md.text('Flusso luminoso _________ 39480 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Illuminazione industriale'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 30 W"),
        md.text('Flusso luminoso _________ 39480 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 60 W"),
        md.text('Flusso luminoso _________ 8932 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 90 W"),
        md.text('Flusso luminoso _________ 13398 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 120 W"),
        md.text('Flusso luminoso _________ 17864 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 150 W"),
        md.text('Flusso luminoso _________ 22330lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 50 W"),
        md.text('Flusso luminoso _________ 7896 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 100 W"),
        md.text('Flusso luminoso _________ 15792 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 150 W"),
        md.text('Flusso luminoso _________ 23688 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 200 W"),
        md.text('Flusso luminoso _________ 31584 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 240 W"),
        md.text('Flusso luminoso _________ 36480 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Illuminazione commerciale'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 10 W"),
        md.text('Flusso luminoso _________ 1500 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 20 W"),
        md.text('Flusso luminoso _________ 3000 lm'),
        md.text('Colore. temperatura ______ 5000 K'),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Fitoilluminazione'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 30 W"),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Dettagli sul sito!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potenza ______________ 60 W"),
        md.text('Grado di protezione _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Indietro'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["Attrezzature per fungaie", "Illuminazione a LED", "Informazioni sull'azienda"]
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'La tua azione è stata annullata', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['Informazioni sull azienda'])
async def wiki_request(message: types.Message):
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«ООО «GreenAl» GreenAl realizza prodotti:"),
            md.text('- Attrezzature per fungaie;'),
            md.text('- Complessi di serre industriali;'),
            md.text('- Apparecchi di illuminazione a LED industriali;'),
            md.text('- Componenti per energia solare;'),
            sep='\n'

        ),
    )


#################################################################################################################################################
@dp.message_handler(state='*', text='✏️Cаlcolo dell attrezzatura dell ordine')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Scrivi a un consulente!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Buona giornata!"),
        md.text('Il mio nome è Ilnar'),
        md.text('Per ordinare l attrezzatura, contattatemi!'),
        md.text('Sempre felice di aiutarti'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Ordina il calcolo dell attrezzatura')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Scrivi a un consulente!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Buona giornata!"),
        md.text('Il mio nome è Marat'),
        md.text('Per ordinare l attrezzatura, contattatemi!'),
        md.text('Sempre felice di aiutarti'),
        sep='\n'

    ), reply_markup=keyboard),


##############################################################################################################################################################

#######################################################################################################################################################################

@dp.message_handler(state='*', text='اللغة العربية🇦🇼')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("اللغة المختارة:", md.bold("اللغة العربية")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['معدات مزارع الفطر', 'الإنارة بالصمام المضيء', 'عن الشركة']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("مرحبا أنا -", md.bold("GreenAl bot")),
            md.text('سأكون مسرورا بمساعدتك!'),
            md.text('استخدم لوحة المفاتيح لتبدأ!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='معدات مزارع الفطر')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️طلب حساب المعدات', "رفوف الألمنيوم لزراعة الفطر والفطر",
               "معدات لجمع شبيجنونس",
               "معدات اختياريه", "ارجع الى"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("مرحبا بكم في القسم:", md.bold("معدات مزارع الفطر")),
            md.text("اختر القسم الذي يثير اهتمامك!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='الإنارة بالصمام المضيء')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️طلب حسا,ب المعدات', "إنارة الشوارع", "الإضاءة الصناعية", "الإضاءة التجارية",
               "الإضاءة النباتية", "إرجاع"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("مرحبا بكم في القسم:", md.bold("الإنارة بالصمام المضيء")),
            md.text("اختر القسم الذي يثير اهتمامك!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['عن الشركة'])
    async def wiki_request(message: types.Message):
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«ООО «جرين» GreenAl المنتجات المصنعة:"),
                md.text('- معدات مزارع الفطر.'),
                md.text('- مجمعات الدفيئة الصناعية.'),
                md.text('- مصابيح LED صناعية ؛'),
                md.text('- مكونات الطاقة الشمسية.'),
                sep='\n'

            ),
        )


####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='معدات مزارع الفطر')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️طلب حساب المعدات', "رفوف الألمنيوم لزراعة الفطر والفطر",
               "معدات لجمع شبيجنونس",
               "معدات اختياريه", "ارجع الى"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("مرحبا بكم في القسم:", md.bold("معدات مزارع الفطر")),
            md.text("اختر القسم الذي يثير اهتمامك!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['ارجع الى'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['معدات مزارع الفطر', 'الإنارة بالصمام المضيء', 'عن الشركة']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'تم إلغاء الإجراء الخاص بك', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['رفوف الألمنيوم لزراعة الفطر والفطر'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'رفوف الألمنيوم لزراعة الفطر والفطر',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("طول الرف _30.0 م (قياسي)"),
        md.text('العرض (داخلي) _ 1.34 م (قياسي)'),
        md.text('العرض (خارج) _ 1.5 متر (قياسي)'),
        md.text('ارتفاع الرف _ من 2.8 إلى 5.0 م'),
        md.text('عدد الطبقات_من 3 إلى 7 قطع'),
        md.text('تباعد أعمدة الدعم_1.5 / 3 م'),
        md.text('ارتفاع سطح السفينة (الرف) _600 ملم'),
        md.text('ارتفاع اللوح الجانبي: 180 ملم'),
        md.text('الوزن الثابت. Rack_1 900 كجم'),
        md.text('تحميل التصميم_195 كجم / م 2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['معدات لجمع شبيجنونس'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'عربة معلقة ستاندارت لجمع الفطر',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Width_1 950 مم"),
        md.text('الارتفاع_3 130 ملم'),
        md.text('العمق_610 ملم'),
        md.text('الوزن_59 كجم'),
        md.text('سعة التحميل :_170 كجم'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'عربة أرضية لجمع الفطر',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("وزن الهيكل _ 15 كجم"),
        md.text('سعة التحميل :_150 كجم'),
        md.text('مقعد material_Plastic'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'منصة قطف الفطر',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("الطول: 1000 مم"),
        md.text('الطول_1125 ملم'),
        md.text('العرض_535 مم'),
        md.text('وزن المنصة_16 كجم'),
        md.text('وزن البراز _5 كجم'),
        md.text('حجم الخلية للمقاييس_330 * 360 مم'),
        md.text('تحميل صف واحد_10 كجم'),
        md.text('عدد صفوف الرفوف_4'
                ''),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['معدات اختياريه'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'حامل شحن الميزان',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("الإرتفاع_1300 مم"),
        md.text('الطول: 1000 مم'),
        md.text('Width_800 مم'),
        md.text('عدد المقاعد_20 جهاز كمبيوتر شخصى'),
        md.text('حجم الخلية للمقاييس_330 * 360 مم'),
        md.text('وزن البناء_38 كجم'),
        md.text('تحميل لكل خلية_25 كجم'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'حامل شحن الميزان مع مآخذ',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("الإرتفاع_1300 مم"),
        md.text('الطول: 1000 مم'),
        md.text('Width_800 مم'),
        md.text('عدد المقاعد_20 جهاز كمبيوتر شخصى'),
        md.text('حجم الخلية للمقاييس_330 * 360 مم'),
        md.text('وزن البناء_38 كجم'),
        md.text('تحميل لكل خلية_25 كجم'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'مجفف للدلاء',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("الطول: 670 مم"),
        md.text('الارتفاع: 624 ملم'),
        md.text('العرض_620 مم'),
        md.text('وزن البناء_17 كجم'),
        md.text('عدد أماكن الدلاء_20 قطعة'),
        md.text('سعة التحميل :_120 كجم'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['ارجع الى'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['معدات مزارع الفطر', 'الإنارة بالصمام المضيء', 'عن الشركة']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'لقد عدت', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='الإنارة بالصمام المضيء')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️طلب حسا,ب المعدات', "إنارة الشوارع", "الإضاءة الصناعية", "الإضاءة التجارية",
               "الإضاءة النباتية", "إرجاع"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("مرحبا بكم في القسم:", md.bold("الإنارة بالصمام المضيء")),
            md.text("اختر القسم الذي يثير اهتمامك!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['إرجاع'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['معدات مزارع الفطر', 'الإنارة بالصمام المضيء', 'عن الشركة']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'تم إلغاء الإجراء الخاص بك', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['إنارة الشوارع'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 30 واط"),
        md.text('الفيض الضوئي ______________ 4373 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 60 واط"),
        md.text('الفيض الضوئي ______________ 8746 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 50 واط"),
        md.text('الفيض الضوئي ______________ 7896 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 100 واط"),
        md.text('الفيض الضوئي ______________ 15792 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 150 واط"),
        md.text('الفيض الضوئي ______________ 23688 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 200 واط"),
        md.text('الفيض الضوئي ______________ 31584 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 240 واط"),
        md.text('الفيض الضوئي ______________ 39480 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['الإضاءة الصناعية'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 30 واط"),
        md.text('الفيض الضوئي ______________ 39480 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 60 واط"),
        md.text('الفيض الضوئي ______________ 8932 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 90 واط"),
        md.text('الفيض الضوئي ______________ 13398 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 120 واط"),
        md.text('الفيض الضوئي ______________ 17864 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 150 واط"),
        md.text('الفيض الضوئي ______________ 22330 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 50 واط"),
        md.text('الفيض الضوئي ______________ 7896 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 100 واط"),
        md.text('الفيض الضوئي ______________ 15792 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 150 واط"),
        md.text('الفيض الضوئي ______________ 23688 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 200 واط"),
        md.text('الفيض الضوئي ______________ 31584 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 240 واط"),
        md.text('الفيض الضوئي ______________ 36480 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['الإضاءة التجارية'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 10 واط"),
        md.text('الفيض الضوئي ______________ 1500 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 20 واط"),
        md.text('الفيض الضوئي ______________ 3000 لومن'),
        md.text('اللون. درجة الحرارة ______________ 5000 ك'),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['الإضاءة النباتية'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 30 واط"),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="التفاصيل على الموقع!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("قوة ______________ 60 واط"),
        md.text('درجة الحماية ______________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['إرجاع'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['معدات مزارع الفطر', 'الإنارة بالصمام المضيء', 'عن الشركة']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'لقد عدت', reply_markup=keyboard)


#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################

@dp.message_handler(state='*', text=['عن الشركة'])
async def wiki_request(message: types.Message):
    await Form.wiki.set()
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("«ООО «جرين» GreenAl المنتجات المصنعة:"),
            md.text('- معدات مزارع الفطر.'),
            md.text('- مجمعات الدفيئة الصناعية.'),
            md.text('- مصابيح LED صناعية ؛'),
            md.text('- مكونات الطاقة الشمسية.'),
            sep='\n'

        ),
    )


#################################################################################################################################################

@dp.message_handler(state='*', text='✏️طلب حسا,ب المعدات')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="اكتب إلى مستشار!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("يوم جيد!"),
        md.text('اسمي إيلنار'),
        md.text('لطلب المعدات ، الرجاء الاتصال بي!'),
        md.text('دائما سعيد لمساعدتك'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️طلب حساب المعدات')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="اكتب إلى مستشار!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("يوم جيد!"),
        md.text('اسمي مارات'),
        md.text('لطلب المعدات ، الرجاء الاتصال بي!'),
        md.text('دائما سعيد لمساعدتك'),
        sep='\n'

    ), reply_markup=keyboard),

###############################################################################################################################################################

#########################################################################################################################################################################

@dp.message_handler(state='*', text='🇪🇸Español')
async def start_cmd(message: types.Message):
    global keyboard
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Idioma seleccionado:", md.bold("Español")),
            sep='\n'
        ),
        parse_mode=ParseMode.MARKDOWN,
    )
    chatId = message.chat.id
    text = message.text.lower()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['Equipo para granjas de hongos', 'Iluminación LED', 'Acerca de la compañía']
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Hola yo soy -", md.bold("GreenAl bot")),
            md.text('¡Estaré encantado de ayudarle!'),
            md.text('¡Usa tu teclado para comenzar!'),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Equipo para granjas de hongos')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Cálculo del equipo de pedido', "Rejillas de aluminio para el cultivo de setas, champiñones.",
               "Equipo para recolectar chappignons",
               "Equipamiento opcional", "De regreso"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenidos a la sección:", md.bold("Equipo para granjas de hongos")),
            md.text("¡Elige la sección que más te interese!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text='Iluminación LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Cálculo dеl equipo de pedido', "Alumbrado público", "Iluminacion industrial", "Iluminación comercial",
               "Fito-iluminación", "Regreso"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenidos a la sección:", md.bold("Iluminación LED")),
            md.text("¡Elige la sección que más te interese!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )

    @dp.message_handler(state='*', text=['Acerca de la compañía'])
    async def wiki_request(message: types.Message):
        await Form.wiki.set()
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("«ООО «GreenAl» GreenAl fabrica productos:"),
                md.text('- Equipo para granjas de hongos;'),
                md.text('- Complejos de invernaderos industriales;'),
                md.text('- Lámparas LED industriales;'),
                md.text('- Componentes para energía solar;'),
                sep='\n'

            ),
        )

####################################---Блок для "Оборудывание для грибных ферм"--- #####################################################################################

@dp.message_handler(state='*', text='Equipo para granjas de hongos')
async def voice_pitch(message: types.Message, state: FSMContext):
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Cálculo del equipo de pedido', "Rejillas de aluminio para el cultivo de setas, champiñones.",
               "Equipo para recolectar chappignons",
               "Equipamiento opcional", "De regreso"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenidos a la sección:", md.bold("Equipo para granjas de hongos")),
            md.text("¡Elige la sección que más te interese!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['De regreso'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Equipo para granjas de hongos', 'Iluminación LED', 'Acerca de la compañía']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Ваше действие отменено', reply_markup=keyboard)


#####################################################################################################################

#######################################----Блок для "Green-al-mushroom"----###########################################################################


@dp.message_handler(state='*', text=['Rejillas de aluminio para el cultivo de setas, champiñones.'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Rejillas de aluminio para el cultivo de setas, champiñones.',
    )
    file = open('Shelvings for mushroom growing.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stellazh-6-yarusnyy/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Longitud del bastidor_30,0 m (estándar)"),
        md.text('Ancho (interior) _ 1,34 m (estándar)'),
        md.text('Ancho (exterior) _ 1,5 m (estándar)'),
        md.text('Altura de la rejilla_ de 2,8 a 5,0 m'),
        md.text('Número de niveles_ de 3 a 7 piezas'),
        md.text('Espacio entre columnas de soporte_1,5 / 3 m'),
        md.text('Altura de la plataforma (balda) _600 mm'),
        md.text('Altura del tablero lateral_180 mm'),
        md.text('Peso constante rack_1 900 kg'),
        md.text('Carga de diseño_195 kg / m2'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Equipo para recolectar chappignons'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Carro colgante Standart para recoger champiñones',
    )
    file = open('Picking lorry Standart.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-podvesnaya-st/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Ancho_1 950 mm"),
        md.text('Altura_3 130 mm'),
        md.text('Profundidad_610 mm'),
        md.text('Peso_59 kg'),
        md.text('Capacidad de carga_170 kg'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Carro de suelo para recoger champiñones',
    )
    file = open('Picking trolley for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/telezhka-napolnaya/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Peso estructura_15 kg"),
        md.text('Capacidad de carga_150 kg'),
        md.text('Material del asiento_Plástico'),
        sep='\n'

    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Plataforma de recolección de setas',
    )
    file = open('Picking platform for lower beds.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/platforma-dlya-sbora/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Longitud_1000 mm"),
        md.text('Altura_1125 mm'),
        md.text('Ancho_535 mm'),
        md.text('Peso de la plataforma_16 kg'),
        md.text('Peso del taburete_5 kg'),
        md.text('Tamaño de celda para scale_330 * 360 mm'),
        md.text('Carga por 1 fila_10 kg'),
        md.text('Número de filas para estantes_4'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Equipamiento opcional'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Soporte de carga de báscula',
    )
    file = open('Cart for charging scales.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Altura_1300 mm"),
        md.text('Longitud_1000 mm'),
        md.text('Ancho_800 mm'),
        md.text('Número de asientos_20 piezas'),
        md.text('Tamaño de celda para scale_330 * 360 mm'),
        md.text('Peso de construcción_38 kg'),
        md.text('Carga por celda_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Soporte de carga de báscula con enchufes',
    )
    file = open('Cart for charging scales with sockets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/stend-dlya-zaryadki-s-rozetkami/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Altura_1300 mm"),
        md.text('Longitud_1000 mm'),
        md.text('Ancho_800 mm'),
        md.text('Número de asientos_20 piezas'),
        md.text('Tamaño de celda para scale_330 * 360 mm'),
        md.text('Peso de construcción_38 kg'),
        md.text('Carga por celda_25 kg'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'Secadora para cubetas',
    )
    file = open('Cart for drying buckets.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-mushroom.ru/catalog/tovar/sushilka/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Longitud_1 670 mm"),
        md.text('Altura_1 624 mm'),
        md.text('Ancho_620 mm'),
        md.text('Peso de construcción_17 kg'),
        md.text('Número de lugares para cubos_20 piezas'),
        md.text('Capacidad de carga_120 kg'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['De regreso'])
async def cancel(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Equipo para granjas de hongos', 'Iluminación LED', 'Acerca de la compañía']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Regresaste ', reply_markup=keyboard)


########################################################################################################################

###############################---Блок для "LED светодиодное освещение"---##########################################################3

@dp.message_handler(state='*', text='Iluminación LED')
async def voice_pitch(message: types.Message, state: FSMContext):
    with open('userlog.txt', 'a') as file:  # Создается текстовый файл
        # в него записывается ID пользователя, его юзернейм и дата нажатия на кнопку START в боте.
        file.write(
            f'\n\nUser ID: {message.from_user.id}\n\nUsername: {message.from_user.username}\n\nDate visited: {message.date}\n----------------------')
    await Form.voice.set()
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False)
    buttons = ['✏️Cálculo dеl equipo de pedido', "Alumbrado público", "Iluminacion industrial", "Iluminación comercial",
               "Fito-iluminación", "Regreso"]
    for button in buttons:
        keyboard.add(button)
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Bienvenidos a la sección:", md.bold("Iluminación LED")),
            md.text("¡Elige la sección que más te interese!"),
            sep='\n'
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state='*', text=['Regreso'])
async def cancel(message: types.Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btns =['Equipo para granjas de hongos', 'Iluminación LED', 'Acerca de la compañía']
    for btn in btns:
        keyboard.add(btn)
    await state.finish()
    await bot.send_message(message.chat.id, 'Tu acción está cancelada', reply_markup=keyboard)


#################################################################################################################

#########################---Блок для "Green-al-light"---#####################################################################################


@dp.message_handler(state='*', text=['Alumbrado público'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'Green-Al-StreetA30',
    )
    file = open('GreenAlStreetA30.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=file)
    file.close()
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/15/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 30 W"),
        md.text('Flujo luminoso _________ 4373 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/16/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 60 W"),
        md.text('Flujo luminoso _________ 8746 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/36/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 50 W"),
        md.text('Flujo luminoso _________ 7896 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/32/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 100 W"),
        md.text('Flujo luminoso _________ 15792 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/33/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 150 W"),
        md.text('Flujo luminoso _________ 23688 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/39/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 200 W"),
        md.text('Flujo luminoso _________ 31584 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/40/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 240 W"),
        md.text('Flujo luminoso _________ 39480 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Iluminacion industrial'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/41/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 30 W"),
        md.text('Flujo luminoso _________ 39480 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        ' GreenAl-Prom A60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/23/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 60 W"),
        md.text('Flujo luminoso _________ 8932 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A90',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/24/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 90 W"),
        md.text('Flujo luminoso _________ 13398 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom А120',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/42/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 120 W"),
        md.text('Flujo luminoso _________ 17864 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Prom A150',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/47/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 150 W"),
        md.text('Flujo luminoso _________ 22330 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/48/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 50 W"),
        md.text('Flujo luminoso _________ 7896 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/43/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 100 W"),
        md.text('Flujo luminoso _________ 15792 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/44/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 150 W"),
        md.text('Flujo luminoso _________ 23688 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/45/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 200 W"),
        md.text('Flujo luminoso _________ 31584 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
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
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/46/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 240 W"),
        md.text('Flujo luminoso _________ 36480 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Iluminación comercial'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 10',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/25/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 10 W"),
        md.text('Flujo luminoso _________ 1500 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Trade Line 20',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/26/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 20 W"),
        md.text('Flujo luminoso _________3000 lm'),
        md.text('Color. temperatura ______ 5000 K'),
        md.text('Grado de protección _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text=['Fito-iluminación'])
async def default_test(message):
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 30',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/27/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 30 W"),
        md.text('Grado de protección _________ IP67'),
        sep='\n'
    ), reply_markup=keyboard),
    await bot.send_message(
        message.chat.id,
        'GreenAl-Phyto 60',
    )
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Detalles en el sitio!",
                                            url="https://www.green-al-light.ru/catalog/tovar/28/")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("Potencia ______________ 60 W"),
        md.text('Grado de protección _________ IP67'),
        sep='\n'

    ), reply_markup=keyboard),

#####################################################################################################################

########################################---Блок для "О компнии"---#########################################################################################################



#################################################################################################################################################
@dp.message_handler(state='*', text='✏️Cálculo dеl equipo de pedido')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="¡Escriba a un consultor!",
                                            url="https://t.me/ilnary")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("¡Buenos días!"),
        md.text('Mi nombre es ilnar'),
        md.text('¡Para pedir equipo, por favor contácteme!'),
        md.text('Siempre feliz de ayudarte'),
        sep='\n'

    ), reply_markup=keyboard),


@dp.message_handler(state='*', text='✏️Cálculo del equipo de pedido')
async def voice_pitch(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="¡Escriba a un consultor!",
                                            url="https://t.me/MaratZainashev")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, md.text(
        md.text("¡Buenos días!"),
        md.text('Mi nombre es marat'),
        md.text('¡Para pedir equipo, por favor contácteme!'),
        md.text('Siempre feliz de ayudarte'),
        sep='\n'

    ), reply_markup=keyboard),


executor.start_polling(dp, skip_updates=True)
