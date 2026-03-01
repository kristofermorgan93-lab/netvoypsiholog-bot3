import telebot
from telebot import types
import time
import os

# ТОКЕН БЕРЁМ ИЗ ПЕРЕМЕННЫХ ОКРУЖЕНИЯ
TOKEN = os.environ.get('BOT_TOKEN')

# Проверка, что токен загрузился (для отладки)
if TOKEN is None:
    print("❌ ОШИБКА: Токен не найден в переменных окружения!")
    exit(1)
else:
    print(f"✅ Токен загружен: {TOKEN[:10]}...")

# ID ТВОЕГО КАНАЛА
CHANNEL_ID = '@netvoipsiholog'

# ПРАКТИКИ И ТЕСТЫ (разбиты по категориям)
PRACTICES = {
    # ПРАКТИКИ
    'letter_to_mother': {
        'name': '👩‍🍼 Письмо матери',
        'link': 'https://t.me/netvoipsiholog/25',
        'category': 'practices'
    },
    'transformation_map': {
        'name': '🧭 Карта Трансформации',
        'link': 'https://t.me/netvoipsiholog/30',
        'category': 'practices'
    },
    'year_closure': {
        'name': '📅 Закрытие года',
        'link': 'https://t.me/c/3218564921/14',
        'category': 'practices'
    },
    'shadow_diary': {
        'name': '🖤 Дневник тени',
        'link': 'https://t.me/netvoipsiholog/24',
        'category': 'practices'
    },
    'letter_to_father': {
        'name': '👨‍🍼 Письмо отцу',
        'link': 'https://t.me/netvoipsiholog/32',
        'category': 'practices'
    },
    'neuro_reboot': {
        'name': '⚡ Нейропереворот',
        'link': 'https://t.me/netvoipsiholog/33',
        'category': 'practices'
    },
    
    # ТЕСТЫ
    'ready_for_relations': {
        'name': '❤️ Готов ли ты к здоровым отношениям?',
        'link': 'https://t.me/netvoipsiholog/26',
        'category': 'tests'
    },
    'rejection_trauma': {
        'name': '🚫 Травма отвержения',
        'link': 'https://t.me/netvoipsiholog/53',
        'category': 'tests'
    },
    'attachment_type': {
        'name': '🔗 Тип привязанности',
        'link': 'https://t.me/netvoipsiholog/75',
        'category': 'tests'
    }
}

bot = telebot.TeleBot(TOKEN)

# Функция проверки подписки
def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['creator', 'administrator', 'member']
    except Exception as e:
        print(f"Ошибка проверки подписки: {e}")
        return False

# Кнопка с ссылкой на канал
def subscription_button():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        "📢 Подписаться на канал", 
        url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
    )
    check_btn = types.InlineKeyboardButton("✅ Я подписался", callback_data="check_sub")
    markup.add(btn)
    markup.add(check_btn)
    return markup

# Главное меню (выбор категории)
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    practices_btn = types.InlineKeyboardButton("🧘 Практики", callback_data="category_practices")
    tests_btn = types.InlineKeyboardButton("📊 Тесты", callback_data="category_tests")
    info_btn = types.InlineKeyboardButton("ℹ️ О канале", callback_data="info")
    markup.add(practices_btn, tests_btn)
    markup.add(info_btn)
    return markup

# Меню с практиками
def practices_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for practice_id, practice in PRACTICES.items():
        if practice['category'] == 'practices':
            btn = types.InlineKeyboardButton(practice['name'], callback_data=f"item_{practice_id}")
            markup.add(btn)
    
    back_btn = types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
    markup.add(back_btn)
    return markup

# Меню с тестами
def tests_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for test_id, test in PRACTICES.items():
        if test['category'] == 'tests':
            btn = types.InlineKeyboardButton(test['name'], callback_data=f"item_{test_id}")
            markup.add(btn)
    
    back_btn = types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
    markup.add(back_btn)
    return markup

# Приветствие для новых пользователей
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    args = message.text.split()
    ref_source = "TikTok" if len(args) > 1 else "прямого перехода"
    
    welcome_text = f"""🧭 *НАВИГАЦИЯ ПО ПРАКТИКАМ И ТЕСТАМ*

🌟 Привет, {first_name}!

Рады видеть тебя с {ref_source}! 👋

Добро пожаловать! Здесь собраны все ключевые материалы для твоего роста. Подписывайся — впереди ещё больше техник по психологии, отношениям и нейропереворотам!

*Чтобы получить доступ к материалам, нужно подписаться на канал:*

👇 Нажми кнопку ниже, чтобы подписаться"""
    
    bot.send_message(
        message.chat.id, 
        welcome_text, 
        parse_mode='Markdown',
        reply_markup=subscription_button()
    )

# Обработка нажатия на "Я подписался"
@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub_callback(call):
    user_id = call.from_user.id
    
    if check_subscription(user_id):
        welcome_text = """✅ *Отлично! Подписка подтверждена*

🧭 *Добро пожаловать в навигатор практик и тестов!*

Выбери, что тебя интересует:
• 🧘 *Практики* — упражнения для проработки
• 📊 *Тесты* — самодиагностика и инсайты

*Обновляется регулярно.* Новые практики — в свежих постах на канале!"""
        
        bot.edit_message_text(
            welcome_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=main_menu()
        )
    else:
        bot.answer_callback_query(
            call.id,
            "❌ Подписка не найдена. Пожалуйста, подпишись на канал и нажми кнопку еще раз!",
            show_alert=True
        )

# Обработка выбора категории
@bot.callback_query_handler(func=lambda call: call.data.startswith('category_'))
def category_callback(call):
    category = call.data.replace('category_', '')
    
    if category == 'practices':
        text = "🧘 *Доступные практики:*\n\nВыбери практику для выполнения:"
        markup = practices_menu()
    elif category == 'tests':
        text = "📊 *Доступные тесты:*\n\nВыбери тест для самодиагностики:"
        markup = tests_menu()
    
    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )

# Обработка выбора практики/теста
@bot.callback_query_handler(func=lambda call: call.data.startswith('item_'))
def item_callback(call):
    item_id = call.data.replace('item_', '')
    item = PRACTICES.get(item_id)
    
    if item:
        category_icon = "🧘" if item['category'] == 'practices' else "📊"
        category_text = "практике" if item['category'] == 'practices' else "тесте"
        
        item_text = f"""{category_icon} *{item['name']}*

Твой материал готов! Переходи по ссылке, чтобы начать работу.

*Важно:* Если материал не открывается, проверь подписку на канал.

[🔗 Перейти к {category_text}]({item['link']})"""
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        if item['category'] == 'practices':
            back_btn = types.InlineKeyboardButton("◀️ К практикам", callback_data="category_practices")
        else:
            back_btn = types.InlineKeyboardButton("◀️ К тестам", callback_data="category_tests")
        
        main_btn = types.InlineKeyboardButton("🏠 Главное меню", callback_data="back_to_main")
        markup.add(back_btn, main_btn)
        
        bot.edit_message_text(
            item_text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            disable_web_page_preview=False,
            reply_markup=markup
        )
    else:
        bot.answer_callback_query(call.id, "Материал не найден")

# Информация о канале
@bot.callback_query_handler(func=lambda call: call.data == "info")
def info_callback(call):
    info_text = """ℹ️ *О канале*

Это пространство для твоего роста и трансформации. Здесь ты найдешь:
• Психологические практики
• Тесты для самодиагностики
• Техники по работе с отношениями
• Нейроперевороты — мощные упражнения для перепрошивки сценариев

📢 *Основной канал:* @netvoipsiholog

*Обновляется регулярно.* Подписывайся, чтобы не пропустить новые практики!"""
    
    markup = types.InlineKeyboardMarkup()
    channel_btn = types.InlineKeyboardButton(
        "📢 Перейти на канал", 
        url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
    )
    back_btn = types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
    markup.add(channel_btn)
    markup.add(back_btn)
    
    bot.edit_message_text(
        info_text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=markup
    )

# Возврат в главное меню
@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main(call):
    text = """🧭 *Навигатор практик и тестов*

Выбери, что тебя интересует:
• 🧘 *Практики* — упражнения для проработки
• 📊 *Тесты* — самодиагностика и инсайты

*Обновляется регулярно.* Новые практики — в свежих постах на канале!"""
    
    bot.edit_message_text(
        text,
        call.message.chat.id,
        call.message.message_id,
        parse_mode='Markdown',
        reply_markup=main_menu()
    )

# Команда /menu для быстрого доступа
@bot.message_handler(commands=['menu'])
def show_menu(message):
    user_id = message.from_user.id
    
    if check_subscription(user_id):
        text = """🧭 *Навигатор практик и тестов*

Выбери, что тебя интересует:
• 🧘 *Практики* — упражнения для проработки
• 📊 *Тесты* — самодиагностика и инсайты"""
        
        bot.send_message(
            message.chat.id, 
            text,
            parse_mode='Markdown',
            reply_markup=main_menu()
        )
    else:
        bot.send_message(
            message.chat.id,
            "🔒 *Для доступа к материалам нужно подписаться на канал!*\n\nПодпишись и нажми /start",
            parse_mode='Markdown',
            reply_markup=subscription_button()
        )

# Запуск бота
if __name__ == '__main__':
    print("🚀 Бот с практиками и тестами запущен...")
    bot.infinity_polling()
