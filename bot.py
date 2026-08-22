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

# ВОПРОСЫ ДЛЯ ТЕСТА
QUESTIONS = [
    "Я часто беру ответственность за чувства других людей",
    "Мне трудно сказать 'нет', даже когда не хочется что-то делать",
    "Я постоянно думаю о проблемах близких людей",
    "Мне кажется, что без меня другие не справятся",
    "Я чувствую вину, когда занимаюсь собой",
    "Мне важно, что обо мне думают другие",
    "Я терплю неуважение в отношениях",
    "Мне трудно просить о помощи",
    "Я часто оправдываю плохое поведение других",
    "Моё настроение зависит от настроения партнёра",
    "Я пытаюсь 'спасать' и 'исправлять' близких",
    "Мне страшно, что меня бросят",
    "Я готова на всё, чтобы сохранить отношения",
    "Я не знаю, чего хочу на самом деле",
    "Мне трудно принимать комплименты"
]

# РЕЗУЛЬТАТЫ ТЕСТА
RESULTS = {
    "low": {
        "range": (0, 10),
        "text": """
📊 *Результат: Низкий уровень созависимости*

У вас здоровые отношения с собой и другими. Вы умеете выстраивать личные границы и заботиться о себе.

*Но помните:* даже при хорошем результате профилактика не помешает. Полный гайд поможет укрепить ваши здоровые паттерны и избежать проблем в будущем.
"""
    },
    "medium": {
        "range": (11, 20),
        "text": """
📊 *Результат: Средний уровень созависимости*

У вас есть склонность к созависимости. Эти паттерны уже влияют на вашу жизнь и отношения, хотя вы можете этого не замечать.

*Что делать:* Вам точно нужна проработка. Полный гайд '5 шагов выхода из созависимости' поможет вам увидеть свои слепые зоны и начать меняться.
"""
    },
    "high": {
        "range": (21, 30),
        "text": """
📊 *Результат: Высокий уровень созависимости*

У вас выраженная созависимость, которая мешает вам жить счастливо. Вы слишком много берёте на себя, терпите неуважение и теряете себя в отношениях.

*Срочно нужно:* Вам жизненно необходима работа над собой. Полный гайд '5 шагов выхода из созависимости' + аудиомедитация — это ваш первый шаг к свободе.
"""
    }
}

# ===== ВСЕ ПРОДУКТЫ =====
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
    },
    
    # ===== ГАЙДЫ (7 штук) =====
    'codependency_guide': {
        'name': '📘 Выход из созависимости',
        'category': 'guides',
        'description': '📘 *Гайд «5 шагов выхода из созависимости»*\n\nТвой путь к свободе и здоровым отношениям.\n\n✅ PDF-гайд (20 страниц)\n✅ Аудиомедитация «Освобождение»\n✅ Дневник прогресса\n✅ Скрипты разговоров\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/7tbZAPa/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/0b9dddb2-3b0b-45e8-9caa-e5f395c850cb?share=post_link',
        'group_link': 'https://t.me/+aZxoSirTo6Y2ZDJi'
    },
    'antiprocrastination': {
        'name': '⏳ Антипрокрастинация',
        'category': 'guides',
        'description': '⏳ *Гайд «Антипрокрастинация»*\n\nПерестань откладывать жизнь на потом.\n\n✅ PDF-гайд с техниками\n✅ Чек-лист «Мои победы»\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/5cbZALH/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/886b6d7f-b500-478a-ae9f-96f0c7f375bd?share=post_link',
        'group_link': 'https://t.me/+ZHEiYXGSRJE5MDJi'
    },
    'antianxiety': {
        'name': '🌿 Антитревога',
        'category': 'guides',
        'description': '🌿 *Гайд «Антитревога»*\n\nПерестань жить в постоянном напряжении.\n\n✅ PDF-гайд с техниками\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/s9bZAJT/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/eca8a389-c989-4a1b-b5c5-b047f860a998?share=post_link',
        'group_link': 'https://t.me/+jKd96l7sxHRiOGYy'
    },
    'selfesteem': {
        'name': '💪 Самооценка',
        'category': 'guides',
        'description': '💪 *Гайд «Самооценка»*\n\nПерестань сомневаться в себе.\n\n✅ PDF-гайд\n✅ Чек-лист «Опора на себя»\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/ojbZAHV/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/f9c900b1-5e28-4a42-888d-cc12b9af50dd?share=post_link',
        'group_link': 'https://t.me/+tHhnbOtl3jRjNGUy'
    },
    'narcissist': {
        'name': '🔍 Нарцисс: как распознать',
        'category': 'guides',
        'description': '🔍 *Гайд «Нарцисс: как распознать и не влюбиться»*\n\nКак не попасть в ловушку обаяния и не потерять себя.\n\n✅ PDF-гайд с признаками нарцисса\n✅ Чек-лист «Красные флаги»\n✅ Техники выхода из отношений с нарциссом\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/hfbZAE8/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/9a7d13bc-e4db-4bdf-8db3-7e4be8caf6e3?share=post_link',
        'group_link': 'https://t.me/+dvM830sJgR40YTFi'
    },
    'boundaries': {
        'name': '🛡️ Границы',
        'category': 'guides',
        'description': '🛡️ *Гайд «Границы»*\n\nКак говорить «нет» без чувства вины.\n\n✅ PDF-гайд с техниками\n✅ Чек-лист «Мои границы»\n✅ Скрипты разговоров\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/8dbZAzj/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/0c85e8df-7271-4f5f-a186-fa9e9618dc63?share=post_link',
        'group_link': 'https://t.me/+OjKcFbdPqaoyMGUy'
    },
    
    # НОВЫЙ ГАЙД — ОТПУСКАНИЕ
    'letting_go': {
        'name': '🕊️ Отпускание',
        'category': 'guides',
        'description': '🕊️ *Гайд «Отпускание»*\n\nКак отпустить прошлое, людей и ситуации, которые тянут вниз.\n\n✅ PDF-гайд с практиками\n✅ Чек-лист «Что я отпускаю»\n✅ Медитация «Освобождение»\n\n💰 *Цена: 990₽*\n\nПосле оплаты материалы выдаются в Telegram-группе',
        'prodamus': 'https://payform.ru/pkckUfX/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/46e2c89a-bafb-40ae-aa51-07a99e250282?share=post_link',
        'group_link': 'https://t.me/+IZdXn_tC2LpmZTUy'
    },
    
    # ===== ТЕТРАДЬ «ДЕНЬГИ=Я» =====
    'money_notebook': {
        'name': '💰 Деньги = Я',
        'category': 'notebook',
        'description': """💰 *Тетрадь-практикум «Деньги = Я»*

Твой личный финансовый дневник. 30 дней практик, чтобы перестать бояться денег, наладить отношения с финансами и начать зарабатывать больше.

*Что внутри тетради:*
📓 30 ежедневных практик
💎 Работа с убеждениями о деньгах
📊 Отслеживание финансовых привычек

*🎁 3 БОНУСА В ПОДАРОК:*
✅ Чек-лист «Моя цена» — определи свою реальную стоимость
✅ Скрипты для переговоров — шаблоны разговоров о деньгах
✅ Таблица доходов и расходов — готовый шаблон для ведения бюджета

*🔥 Цена: 2490₽*
*🎯 По промокоду «ВПЕРЕД» — 1990₽*

После оплаты материалы выдаются в Telegram-группе""",
        'price': '2490₽ (по промокоду «ВПЕРЕД» — 1990₽)',
        'prodamus': 'https://payform.ru/ijc6dWJ/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/f78172f4-c4ae-4c42-8d10-a35960a88351?share=post_link',
        'group_link': 'https://t.me/+mzldZA7y5X8wYTli'
    }
}

bot = telebot.TeleBot(TOKEN)

# Хранилище для состояний теста
user_sessions = {}

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
    btn = types.InlineKeyboardButton("📢 Подписаться на канал", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")
    check_btn = types.InlineKeyboardButton("✅ Я подписался", callback_data="check_sub")
    markup.add(btn, check_btn)
    return markup

# Главное меню
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🧪 Пройти тест на созависимость", callback_data="start_test"),
        types.InlineKeyboardButton("📚 Все гайды (7)", callback_data="category_guides"),
        types.InlineKeyboardButton("💰 Тетрадь Деньги=Я", callback_data="notebook_money"),
        types.InlineKeyboardButton("🧘 Практики", callback_data="category_practices"),
        types.InlineKeyboardButton("📊 Тесты", callback_data="category_tests"),
        types.InlineKeyboardButton("ℹ️ О канале", callback_data="info")
    )
    return markup

# Меню с практиками
def practices_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for practice_id, practice in PRACTICES.items():
        if practice['category'] == 'practices':
            markup.add(types.InlineKeyboardButton(practice['name'], callback_data=f"item_{practice_id}"))
    markup.add(types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main"))
    return markup

# Меню с тестами
def tests_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for test_id, test in PRACTICES.items():
        if test['category'] == 'tests':
            markup.add(types.InlineKeyboardButton(test['name'], callback_data=f"item_{test_id}"))
    markup.add(types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main"))
    return markup

# Меню со ВСЕМИ гайдами (7 штук)
def guides_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for guide_id, guide in PRACTICES.items():
        if guide['category'] == 'guides':
            markup.add(types.InlineKeyboardButton(guide['name'], callback_data=f"guide_{guide_id}"))
    markup.add(types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main"))
    return markup

# Приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    args = message.text.split()
    ref_source = "TikTok" if len(args) > 1 else "прямого перехода"
    
    if check_subscription(user_id):
        welcome_text = f"""🧭 *Навигатор*

🌟 Привет, {first_name}!

Рады видеть тебя с {ref_source}!

Что тебя интересует?
• 🧪 *Тест на созависимость* (бесплатно)
• 📚 *Гайды* — 7 штук (990₽)
• 💰 *Тетрадь Деньги=Я* — премиум-продукт
• 🧘 Практики и 📊 тесты"""
        
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=main_menu())
    else:
        welcome_text = f"""🧭 *НАВИГАЦИЯ*

🌟 Привет, {first_name}!

Рады видеть тебя с {ref_source}! 👋

*Чтобы получить доступ к материалам, нужно подписаться на канал:*"""
        
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=subscription_button())

# ===== ОБРАБОТКА КНОПОК =====
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    
    # ПРОВЕРКА ПОДПИСКИ
    if call.data == "check_sub":
        if check_subscription(user_id):
            bot.edit_message_text("✅ Подписка подтверждена!\n\nВыбери действие:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
        else:
            bot.answer_callback_query(call.id, "❌ Подписка не найдена", show_alert=True)
    
    # ВОЗВРАТ В МЕНЮ
    elif call.data == "back_to_main":
        bot.edit_message_text("Выбери действие:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    # НАЧАЛО ТЕСТА
    elif call.data == "start_test":
        user_sessions[user_id] = {'question': 0, 'answers': []}
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("✅ Да", callback_data="answer_2"),
            types.InlineKeyboardButton("🤔 Иногда", callback_data="answer_1"),
            types.InlineKeyboardButton("❌ Нет", callback_data="answer_0")
        )
        
        bot.edit_message_text(f"*Вопрос 1 из 15:*\n\n{QUESTIONS[0]}", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
    # ОТВЕТЫ НА ВОПРОСЫ
    elif call.data.startswith("answer_"):
        score = int(call.data.split('_')[1])
        session = user_sessions.get(user_id)
        
        if session:
            session['answers'].append(score)
            session['question'] += 1
            
            if session['question'] < 15:
                markup = types.InlineKeyboardMarkup()
                markup.add(
                    types.InlineKeyboardButton("✅ Да", callback_data="answer_2"),
                    types.InlineKeyboardButton("🤔 Иногда", callback_data="answer_1"),
                    types.InlineKeyboardButton("❌ Нет", callback_data="answer_0")
                )
                
                bot.edit_message_text(f"*Вопрос {session['question'] + 1} из 15:*\n\n{QUESTIONS[session['question']]}", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
            else:
                total = sum(session['answers'])
                
                if total <= 10:
                    result_text = RESULTS['low']['text']
                elif total <= 20:
                    result_text = RESULTS['medium']['text']
                else:
                    result_text = RESULTS['high']['text']
                
                bot.edit_message_text(result_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown')
                
                markup = types.InlineKeyboardMarkup()
                markup.add(
                    types.InlineKeyboardButton("📘 Купить гайд по созависимости", callback_data="guide_codependency_guide"),
                    types.InlineKeyboardButton("📚 Смотреть все гайды", callback_data="category_guides"),
                    types.InlineKeyboardButton("◀️ В меню", callback_data="back_to_main")
                )
                
                bot.send_message(call.message.chat.id, "📘 *Теперь тебе нужен этот гайд*\n\n«5 шагов выхода из созависимости» — твоя пошаговая инструкция к свободе.", parse_mode='Markdown', reply_markup=markup)
                
                del user_sessions[user_id]
    
    # КАТЕГОРИИ
    elif call.data == "category_practices":
        bot.edit_message_text("🧘 *Доступные практики:*", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=practices_menu())
    
    elif call.data == "category_tests":
        bot.edit_message_text("📊 *Доступные тесты:*", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=tests_menu())
    
    elif call.data == "category_guides":
        bot.edit_message_text("📚 *Все гайды (7):*", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=guides_menu())
    
    # ПРАКТИКИ/ТЕСТЫ
    elif call.data.startswith('item_'):
        item_id = call.data.replace('item_', '')
        item = PRACTICES.get(item_id)
        
        if item:
            category_icon = "🧘" if item['category'] == 'practices' else "📊"
            category_text = "практике" if item['category'] == 'practices' else "тесте"
            
            item_text = f"""{category_icon} *{item['name']}*

Твой материал готов!

[🔗 Перейти к {category_text}]({item['link']})"""
            
            markup = types.InlineKeyboardMarkup()
            if item['category'] == 'practices':
                markup.add(types.InlineKeyboardButton("◀️ К практикам", callback_data="category_practices"))
            else:
                markup.add(types.InlineKeyboardButton("◀️ К тестам", callback_data="category_tests"))
            markup.add(types.InlineKeyboardButton("🏠 Главное меню", callback_data="back_to_main"))
            
            bot.edit_message_text(item_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', disable_web_page_preview=False, reply_markup=markup)
    
    # ГАЙДЫ
    elif call.data.startswith('guide_'):
        guide_id = call.data.replace('guide_', '')
        guide = PRACTICES.get(guide_id)
        
        if guide:
            text = f"""{guide['description']}

👇 Выбери способ оплаты:"""
            
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("🇷🇺 Картой РФ (Prodamus)", url=guide['prodamus']),
                types.InlineKeyboardButton("🌍 Зарубежной картой (Boosty)", url=guide['boosty']),
                types.InlineKeyboardButton("◀️ Ко всем гайдам", callback_data="category_guides")
            )
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
    # ТЕТРАДЬ
    elif call.data == "notebook_money":
        product = PRACTICES.get('money_notebook')
        
        if product:
            text = f"""{product['description']}

👇 Выбери способ оплаты:"""
            
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("🇷🇺 Картой РФ (Prodamus)", url=product['prodamus']),
                types.InlineKeyboardButton("🌍 Зарубежной картой (Boosty)", url=product['boosty']),
                types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
            )
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
    # ИНФО
    elif call.data == "info":
        info_text = """ℹ️ *О канале*

Это пространство для твоего роста.

📢 *Канал:* @netvoipsiholog"""
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("📢 Перейти на канал", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"),
            types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
        )
        
        bot.edit_message_text(info_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)

# КОМАНДА /MENU
@bot.message_handler(commands=['menu'])
def show_menu(message):
    if check_subscription(message.from_user.id):
        bot.send_message(message.chat.id, "Выбери действие:", reply_markup=main_menu())
    else:
        bot.send_message(message.chat.id, "🔒 Подпишись на канал!", reply_markup=subscription_button())

# ПОЛУЧЕНИЕ FILE_ID
@bot.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice'])
def handle_files(message):
    ADMIN_ID = int(os.getenv('ADMIN_ID', '7579002030'))
    
    if message.from_user.id != ADMIN_ID:
        return
    
    if message.document:
        bot.reply_to(message, f"📄 File ID: `{message.document.file_id}`", parse_mode='Markdown')
    elif message.audio:
        bot.reply_to(message, f"🎵 File ID: `{message.audio.file_id}`", parse_mode='Markdown')

# ===== ЗАПУСК =====
if __name__ == '__main__':
    print("🚀 Бот со всеми продуктами запущен...")
    bot.infinity_polling()
