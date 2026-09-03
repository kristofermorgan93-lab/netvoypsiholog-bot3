import telebot
from telebot import types
import time
import os

# ТОКЕН
TOKEN = os.environ.get('BOT_TOKEN')
if TOKEN is None:
    print("❌ ОШИБКА: Токен не найден!")
    exit(1)
else:
    print(f"✅ Токен загружен: {TOKEN[:10]}...")

CHANNEL_ID = '@netvoipsiholog'

# ===== ТЕСТ НА СОЗАВИСИМОСТЬ =====
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
    
    # ===== ГАЙДЫ (6) =====
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
    
    # ===== НОВЫЙ ПРАКТИКУМ «ТЕНЬ» =====
    'shadow_practicum': {
        'name': '🗝️ Тень. Глубокое погружение',
        'category': 'practicums',
        'description': """🗝️ *Практикум «Тень. Глубокое погружение»*

Как перестать бороться с собой и присвоить свою силу.

*Что внутри:*
✅ Тест-самодиагностика «Есть ли у тебя Тень?»
✅ Упражнение «Путь в Тень»
✅ Упражнение «Озеро»
✅ Дневник работы с Тенью (7 дней)
✅ Карта Тени (шпаргалка для быстрой работы)

*Бонус:*
🗺️ Карта Тени — отдельный PDF-файл

💰 *Цена: 2490₽*

После оплаты материалы выдаются в Telegram-группе""",
        'prodamus': 'https://payform.ru/l3ctECA/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/a097b699-d717-440c-9fde-b38d4d15e832?share=post_link',
        'group_link': 'https://t.me/+xahqAkcA8dRiNTMy'
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
✅ Чек-лист «Моя цена»
✅ Скрипты для переговоров
✅ Таблица доходов и расходов

💰 *Цена: 2490₽*

После оплаты материалы выдаются в Telegram-группе""",
        'prodamus': 'https://payform.ru/ijc6dWJ/',
        'boosty': 'https://boosty.to/evgeniy_getman/posts/f78172f4-c4ae-4c42-8d10-a35960a88351?share=post_link',
        'group_link': 'https://t.me/+mzldZA7y5X8wYTli'
    }
}

bot = telebot.TeleBot(TOKEN)
user_sessions = {}

# ===== ПРОВЕРКА ПОДПИСКИ =====
def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['creator', 'administrator', 'member']
    except:
        return False

# ===== КНОПКИ =====
def subscription_button():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📢 Подписаться на канал", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")
    check_btn = types.InlineKeyboardButton("✅ Я подписался", callback_data="check_sub")
    markup.add(btn, check_btn)
    return markup

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🧪 Пройти тест на созависимость", callback_data="start_test"),
        types.InlineKeyboardButton("🗝️ Практикум Тень", callback_data="practicum_shadow"),
        types.InlineKeyboardButton("📚 Все гайды", callback_data="category_guides"),
        types.InlineKeyboardButton("💰 Тетрадь Деньги=Я", callback_data="notebook_money"),
        types.InlineKeyboardButton("🧘 Практики", callback_data="category_practices"),
        types.InlineKeyboardButton("📊 Тесты", callback_data="category_tests"),
        types.InlineKeyboardButton("ℹ️ О канале", callback_data="info")
    )
    return markup

def practices_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for pid, p in PRACTICES.items():
        if p['category'] == 'practices':
            markup.add(types.InlineKeyboardButton(p['name'], callback_data=f"item_{pid}"))
    markup.add(types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main"))
    return markup

def tests_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for tid, t in PRACTICES.items():
        if t['category'] == 'tests':
            markup.add(types.InlineKeyboardButton(t['name'], callback_data=f"item_{tid}"))
    markup.add(types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main"))
    return markup

def guides_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for gid, g in PRACTICES.items():
        if g['category'] == 'guides':
            markup.add(types.InlineKeyboardButton(g['name'], callback_data=f"guide_{gid}"))
    markup.add(types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main"))
    return markup

# ===== ОБРАБОТЧИКИ =====
@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    if check_subscription(message.from_user.id):
        welcome_text = f"""🧭 *Навигатор*

🌟 Привет, {first_name}!

Рады видеть тебя!

Что тебя интересует?
• 🧪 *Тест на созависимость* (бесплатно)
• 🗝️ *Практикум Тень* (новинка!)
• 📚 *Гайды* — 990₽
• 💰 *Тетрадь Деньги=Я* — 2490₽
• 🧘 Практики и 📊 тесты"""
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=main_menu())
    else:
        welcome_text = f"""🧭 *НАВИГАЦИЯ*

🌟 Привет, {first_name}!

*Чтобы получить доступ к материалам, нужно подписаться на канал:*"""
        bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=subscription_button())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    
    if call.data == "check_sub":
        if check_subscription(user_id):
            bot.edit_message_text("✅ Подписка подтверждена!\n\nВыбери действие:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
        else:
            bot.answer_callback_query(call.id, "❌ Подписка не найдена", show_alert=True)
    
    elif call.data == "back_to_main":
        bot.edit_message_text("Выбери действие:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    
    elif call.data == "start_test":
        user_sessions[user_id] = {'question': 0, 'answers': []}
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("✅ Да", callback_data="answer_2"),
            types.InlineKeyboardButton("🤔 Иногда", callback_data="answer_1"),
            types.InlineKeyboardButton("❌ Нет", callback_data="answer_0")
        )
        bot.edit_message_text(f"*Вопрос 1 из 15:*\n\n{QUESTIONS[0]}", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
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
    
    elif call.data == "category_practices":
        bot.edit_message_text("🧘 *Доступные практики:*", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=practices_menu())
    
    elif call.data == "category_tests":
        bot.edit_message_text("📊 *Доступные тесты:*", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=tests_menu())
    
    elif call.data == "category_guides":
        bot.edit_message_text("📚 *Все гайды (6):*", call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=guides_menu())
    
    elif call.data.startswith('item_'):
        item_id = call.data.replace('item_', '')
        item = PRACTICES.get(item_id)
        if item:
            cat_icon = "🧘" if item['category'] == 'practices' else "📊"
            cat_text = "практике" if item['category'] == 'practices' else "тесте"
            text = f"""{cat_icon} *{item['name']}*
Твой материал готов!
[🔗 Перейти к {cat_text}]({item['link']})"""
            markup = types.InlineKeyboardMarkup()
            if item['category'] == 'practices':
                markup.add(types.InlineKeyboardButton("◀️ К практикам", callback_data="category_practices"))
            else:
                markup.add(types.InlineKeyboardButton("◀️ К тестам", callback_data="category_tests"))
            markup.add(types.InlineKeyboardButton("🏠 Главное меню", callback_data="back_to_main"))
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', disable_web_page_preview=False, reply_markup=markup)
    
    elif call.data.startswith('guide_'):
        gid = call.data.replace('guide_', '')
        g = PRACTICES.get(gid)
        if g:
            text = f"""{g['description']}\n\n👇 Выбери способ оплаты:"""
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("🇷🇺 Картой РФ (Prodamus)", url=g['prodamus']),
                types.InlineKeyboardButton("🌍 Зарубежной картой (Boosty)", url=g['boosty']),
                types.InlineKeyboardButton("◀️ Ко всем гайдам", callback_data="category_guides")
            )
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
    # ===== НОВЫЙ ПРАКТИКУМ «ТЕНЬ» =====
    elif call.data == "practicum_shadow":
        product = PRACTICES.get('shadow_practicum')
        if product:
            text = f"""{product['description']}\n\n👇 Выбери способ оплаты:"""
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("🇷🇺 Картой РФ (Prodamus)", url=product['prodamus']),
                types.InlineKeyboardButton("🌍 Зарубежной картой (Boosty)", url=product['boosty']),
                types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
            )
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
    elif call.data == "notebook_money":
        product = PRACTICES.get('money_notebook')
        if product:
            text = f"""{product['description']}\n\n👇 Выбери способ оплаты:"""
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(
                types.InlineKeyboardButton("🇷🇺 Картой РФ (Prodamus)", url=product['prodamus']),
                types.InlineKeyboardButton("🌍 Зарубежной картой (Boosty)", url=product['boosty']),
                types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
            )
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='Markdown', reply_markup=markup)
    
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

# ===== ЗАПУСК =====
if __name__ == '__main__':
    print("🚀 Бот с практикумом «Тень» запущен...")
    bot.infinity_polling()
