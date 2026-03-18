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

# ПРАКТИКИ, ТЕСТЫ И ГАЙДЫ
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
    
    # НОВЫЕ ГАЙДЫ
    'antiprocrastination': {
        'name': '⏳ Антипрокрастинация',
        'category': 'guides',
        'price': 990,
        'description': '⏳ *Гайд «Антипрокрастинация»*\n\nПерестань откладывать жизнь на потом.\n\nВ комплекте:\n✅ PDF-гайд с техниками\n✅ Чек-лист «Мои победы»',
        'prodamus_link': 'https://getman-help.payform.ru/?invoice_id=e58590883ed1495cfb57efe0fccbc372&paylink=1',
        'boosty_link': 'https://boosty.to/evgeniy_getman/posts/886b6d7f-b500-478a-ae9f-96f0c7f375bd?share=post_link'
    },
    'antianxiety': {
        'name': '🌿 Антитревога',
        'category': 'guides',
        'price': 990,
        'description': '🌿 *Гайд «Антитревога»*\n\nПерестань жить в постоянном напряжении.\n\nВ комплекте:\n✅ PDF-гайд с техниками',
        'prodamus_link': 'https://getman-help.payform.ru/?invoice_id=c920cf5c66584bbee8c0ec272ca0c8e0&paylink=1',
        'boosty_link': 'https://boosty.to/evgeniy_getman/posts/eca8a389-c989-4a1b-b5c5-b047f860a998?share=post_link'
    },
    'selfesteem': {
        'name': '💪 Самооценка',
        'category': 'guides',
        'price': 990,
        'description': '💪 *Гайд «Самооценка»*\n\nПерестань сомневаться в себе.\n\nВ комплекте:\n✅ PDF-гайд\n✅ Чек-лист «Опора на себя»',
        'prodamus_link': 'https://getman-help.payform.ru/?invoice_id=3d9b03898a587f28fb95a8f4b4ab16cd&paylink=1',
        'boosty_link': 'https://boosty.to/evgeniy_getman/posts/f9c900b1-5e28-4a42-888d-cc12b9af50dd?share=post_link'
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
    btn = types.InlineKeyboardButton(
        "📢 Подписаться на канал", 
        url=f"https://t.me/{CHANNEL_ID.replace('@', '')}"
    )
    check_btn = types.InlineKeyboardButton("✅ Я подписался", callback_data="check_sub")
    markup.add(btn)
    markup.add(check_btn)
    return markup

# Главное меню
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    test_btn = types.InlineKeyboardButton("🧪 Пройти тест на созависимость", callback_data="start_test")
    practices_btn = types.InlineKeyboardButton("🧘 Практики", callback_data="category_practices")
    tests_btn = types.InlineKeyboardButton("📊 Другие тесты", callback_data="category_tests")
    guides_btn = types.InlineKeyboardButton("📚 Гайды", callback_data="category_guides")
    info_btn = types.InlineKeyboardButton("ℹ️ О канале", callback_data="info")
    
    markup.add(test_btn)
    markup.add(practices_btn, tests_btn)
    markup.add(guides_btn)
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

# Меню с гайдами
def guides_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for guide_id, guide in PRACTICES.items():
        if guide['category'] == 'guides':
            btn = types.InlineKeyboardButton(guide['name'], callback_data=f"guide_{guide_id}")
            markup.add(btn)
    
    back_btn = types.InlineKeyboardButton("◀️ В главное меню", callback_data="back_to_main")
    markup.add(back_btn)
    return markup

# Меню выбора способа оплаты для гайда
def payment_options_menu(guide_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    guide = PRACTICES.get(guide_id)
    if guide:
        markup.add(
            types.InlineKeyboardButton("🇷🇺 Картой РФ / СБП (Prodamus)", callback_data=f"pay_prodamus_{guide_id}"),
            types.InlineKeyboardButton("🌍 Зарубежной картой (Boosty)", callback_data=f"pay_boosty_{guide_id}"),
            types.InlineKeyboardButton("◀️ Назад к гайдам", callback_data="category_guides")
        )
    return markup

# Приветствие для новых пользователей
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    args = message.text.split()
    ref_source = "TikTok" if len(args) > 1 else "прямого перехода"
    
    if check_subscription(user_id):
        welcome_text = f"""🧭 *Навигатор практик и тестов*

🌟 Привет, {first_name}!

Рады видеть тебя с {ref_source}!

Выбери, что тебя интересует:
• 🧪 *Тест на созависимость* — узнай свой уровень
• 🧘 *Практики* — упражнения для проработки
• 📊 *Тесты* — самодиагностика
• 📚 *Гайды* — новые пособия (антипрокрастинация, антитревога, самооценка)"""
        
        bot.send_message(
            message.chat.id, 
            welcome_text, 
            parse_mode='Markdown',
            reply_markup=main_menu()
        )
    else:
        welcome_text = f"""🧭 *НАВИГАЦИЯ ПО ПРАКТИКАМ И ТЕСТАМ*

🌟 Привет, {first_name}!

Рады видеть тебя с {ref_source}! 👋

*Чтобы получить доступ к материалам, нужно подписаться на канал:*

👇 Нажми кнопку ниже, чтобы подписаться"""
        
        bot.send_message(
            message.chat.id, 
            welcome_text, 
            parse_mode='Markdown',
            reply_markup=subscription_button()
        )

# ===== ОБРАБОТКА ВСЕХ КНОПОК =====
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    
    # ===== ПРОВЕРКА ПОДПИСКИ =====
    if call.data == "check_sub":
        if check_subscription(user_id):
            bot.edit_message_text(
                "✅ Подписка подтверждена!\n\nВыбери действие:",
                call.message.chat.id,
                call.message.message_id,
                reply_markup=main_menu()
            )
        else:
            bot.answer_callback_query(call.id, "❌ Подписка не найдена", show_alert=True)
    
    # ===== ВОЗВРАТ В МЕНЮ =====
    elif call.data == "back_to_main":
        bot.edit_message_text(
            "Выбери действие:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=main_menu()
        )
    
    # ===== НАЧАЛО ТЕСТА =====
    elif call.data == "start_test":
        user_sessions[user_id] = {
            'question': 0,
            'answers': []
        }
        
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("✅ Да", callback_data="answer_2"),
            types.InlineKeyboardButton("🤔 Иногда", callback_data="answer_1"),
            types.InlineKeyboardButton("❌ Нет", callback_data="answer_0")
        )
        
        bot.edit_message_text(
            f"*Вопрос 1 из 15:*\n\n{QUESTIONS[0]}",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=markup
        )
    
    # ===== ОТВЕТЫ НА ВОПРОСЫ =====
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
                
                bot.edit_message_text(
                    f"*Вопрос {session['question'] + 1} из 15:*\n\n{QUESTIONS[session['question']]}",
                    call.message.chat.id,
                    call.message.message_id,
                    parse_mode='Markdown',
                    reply_markup=markup
                )
            else:
                total = sum(session['answers'])
                
                if total <= 10:
                    result_text = RESULTS['low']['text']
                elif total <= 20:
                    result_text = RESULTS['medium']['text']
                else:
                    result_text = RESULTS['high']['text']
                
                bot.edit_message_text(
                    result_text,
                    call.message.chat.id,
                    call.message.message_id,
                    parse_mode='Markdown'
                )
                
                markup = types.InlineKeyboardMarkup()
                guides_btn = types.InlineKeyboardButton("📚 Посмотреть гайды", callback_data="category_guides")
                menu_btn = types.InlineKeyboardButton("◀️ В меню", callback_data="back_to_main")
                markup.add(guides_btn)
                markup.add(menu_btn)
                
                bot.send_message(
                    call.message.chat.id,
                    "📚 *Хочешь проработать другие темы?*\n\n"
                    "У меня есть новые гайды:\n"
                    "⏳ Антипрокрастинация\n"
                    "🌿 Антитревога\n"
                    "💪 Самооценка",
                    parse_mode='Markdown',
                    reply_markup=markup
                )
                
                del user_sessions[user_id]
    
    # ===== КАТЕГОРИИ =====
    elif call.data == "category_practices":
        bot.edit_message_text(
            "🧘 *Доступные практики:*\n\nВыбери практику для выполнения:",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=practices_menu()
        )
    
    elif call.data == "category_tests":
        bot.edit_message_text(
            "📊 *Доступные тесты:*\n\nВыбери тест для самодиагностики:",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=tests_menu()
        )
    
    elif call.data == "category_guides":
        bot.edit_message_text(
            "📚 *Наши гайды:*\n\nВыбери тему, которая тебе откликается:",
            call.message.chat.id,
            call.message.message_id,
            parse_mode='Markdown',
            reply_markup=guides_menu()
        )
    
    # ===== ПРАКТИКИ/ТЕСТЫ =====
    elif call.data.startswith('item_'):
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
            
            try:
                bot.edit_message_text(
                    item_text,
                    call.message.chat.id,
                    call.message.message_id,
                    parse_mode='Markdown',
                    disable_web_page_preview=False,
                    reply_markup=markup
                )
            except:
                pass
        else:
            bot.answer_callback_query(call.id, "Материал не найден")
    
    # ===== ГАЙДЫ =====
    elif call.data.startswith('guide_'):
        guide_id = call.data.replace('guide_', '')
        guide = PRACTICES.get(guide_id)
        
        if guide:
            text = f"""{guide['description']}

💰 *Цена: {guide['price']}₽*

👇 Выбери способ оплаты:
🇷🇺 Картой РФ / СБП
🌍 Зарубежной картой (Boosty)

После оплаты напиши @evgeniy_getman с подтверждением — отправлю материалы."""
            
            bot.edit_message_text(
                text,
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown',
                reply_markup=payment_options_menu(guide_id)
            )
    
    # ===== ОПЛАТА =====
    elif call.data.startswith('pay_prodamus_'):
        guide_id = call.data.replace('pay_prodamus_', '')
        guide = PRACTICES.get(guide_id)
        
        if guide:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("💳 Перейти к оплате", url=guide['prodamus_link']))
            back_btn = types.InlineKeyboardButton("◀️ Назад к гайду", callback_data=f"guide_{guide_id}")
            markup.add(back_btn)
            
            bot.edit_message_text(
                f"🔗 *Ссылка для оплаты через Prodamus готова!*\n\n"
                f"Гайд: {guide['name']}\n"
                f"Сумма: {guide['price']} ₽\n\n"
                f"После оплаты напиши @evgeniy_getman с подтверждением — отправлю материалы.",
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown',
                reply_markup=markup
            )
    
    elif call.data.startswith('pay_boosty_'):
        guide_id = call.data.replace('pay_boosty_', '')
        guide = PRACTICES.get(guide_id)
        
        if guide:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("💳 Перейти к оплате", url=guide['boosty_link']))
            back_btn = types.InlineKeyboardButton("◀️ Назад к гайду", callback_data=f"guide_{guide_id}")
            markup.add(back_btn)
            
            bot.edit_message_text(
                f"🔗 *Ссылка для оплаты через Boosty готова!*\n\n"
                f"Гайд: {guide['name']}\n\n"
                f"После оплаты напиши @evgeniy_getman с подтверждением — отправлю материалы.",
                call.message.chat.id,
                call.message.message_id,
                parse_mode='Markdown',
                reply_markup=markup
            )
    
    # ===== ИНФО =====
    elif call.data == "info":
        info_text = """ℹ️ *О канале*

Это пространство для твоего роста и трансформации. Здесь ты найдешь:
• Психологические практики
• Тесты для самодиагностики
• Техники по работе с отношениями
• Гайды по актуальным темам

📢 *Основной канал:* @netvoipsiholog

*Обновляется регулярно.* Подписывайся, чтобы не пропустить новинки!"""
        
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

# Команда /menu для быстрого доступа
@bot.message_handler(commands=['menu'])
def show_menu(message):
    user_id = message.from_user.id
    
    if check_subscription(user_id):
        text = """🧭 *Навигатор практик и тестов*

Выбери, что тебя интересует:
• 🧘 *Практики* — упражнения для проработки
• 📊 *Тесты* — самодиагностика и инсайты
• 📚 *Гайды* — новые пособия"""
        
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

# Функция для получения file_id
@bot.message_handler(content_types=['document', 'audio', 'photo', 'video', 'voice'])
def handle_files(message):
    ADMIN_ID = int(os.getenv('ADMIN_ID', '7579002030'))
    
    if message.from_user.id != ADMIN_ID:
        return
    
    response = "📁 ИНФОРМАЦИЯ О ФАЙЛЕ:\n\n"
    
    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        response += f"📄 Документ: {file_name}\n"
        response += f"📎 File ID: {file_id}\n\n"
        response += file_id
    elif message.audio:
        file_id = message.audio.file_id
        title = message.audio.title or "audio"
        response += f"🎵 Аудио: {title}\n"
        response += f"📎 File ID: {file_id}\n\n"
        response += file_id
    elif message.photo:
        photo = message.photo[-1]
        file_id = photo.file_id
        response += f"🖼️ Фото: {photo.width}x{photo.height}\n"
        response += f"📎 File ID: {file_id}\n\n"
        response += file_id
    elif message.video:
        file_id = message.video.file_id
        response += f"🎬 Видео: видеофайл\n"
        response += f"📎 File ID: {file_id}\n\n"
        response += file_id
    elif message.voice:
        file_id = message.voice.file_id
        response += f"🎤 Голосовое: {message.voice.duration} сек\n"
        response += f"📎 File ID: {file_id}\n\n"
        response += file_id
    
    bot.reply_to(message, response)

# ===== ЗАПУСК БОТА =====
if __name__ == '__main__':
    print("🚀 Бот с практиками, тестами и новыми гайдами запущен...")
    bot.infinity_polling()
