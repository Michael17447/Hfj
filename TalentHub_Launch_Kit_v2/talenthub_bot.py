from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

WELCOME_TEXT = """
👋 Привет! Я — помощник TalentHub 🎯
Чем могу помочь?

▶️ /help — Как начать зарабатывать
▶️ /payout — Как вывести деньги
▶️ /rating — Как повысить рейтинг
▶️ /course — Бесплатные курсы
▶️ /contact — Связаться с поддержкой
"""

HELP_TEXT = """
🚀 Как начать зарабатывать на TalentHub:

1. Скачай приложение TalentHub (скоро в App Store и Google Play)
2. Зарегистрируйся — укажи свои таланты и цену
3. Откликайся на заказы рядом с тобой
4. Выполни — получи оплату на карту

💡 Первым 100 — бонус 300 руб за первый заказ!
"""

PAYOUT_TEXT = """
💸 Как вывести деньги с TalentHub:

1. Перейди в «Кошелёк» → «Вывести»
2. Выбери способ: карта, QIWI, крипто
3. Минимальная сумма — 100 руб
4. Деньги придут за 5 минут

⚠️ Оплата проходит только после подтверждения заказчиком.
"""

RATING_TEXT = """
⭐ Как повысить рейтинг на TalentHub:

✅ Выполняй заказы в срок  
✅ Общайся вежливо  
✅ Проси клиентов оставить отзыв  
✅ Добавь фото/видео выполненных работ  

🔝 Чем выше рейтинг — тем больше заказов ты получаешь!
"""

COURSE_TEXT = """
🎓 Бесплатные курсы от TalentHub:

1. «Как продавать свои таланты» — 30 мин
2. «Как договариваться с клиентами» — 20 мин
3. «Как масштабировать заработок» — 45 мин

👉 Скоро внутри приложения. Оставь email на сайте — пришлём уведомление!
🌐 https://talenthub.ru
"""

CONTACT_TEXT = """
📬 Связаться с поддержкой TalentHub:

Напиши нам: support@talenthub.ru
Или задай вопрос здесь — оператор ответит в течение 24 часов.

Также можешь присоединиться к чату:
👉 t.me/talenthub_chat
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)

async def payout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PAYOUT_TEXT)

async def rating(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RATING_TEXT)

async def course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(COURSE_TEXT)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CONTACT_TEXT)

def main():
    TOKEN = "8316668370:AAFDuDi5kqfCJ7p3ibBPbYVCwpmIOLFGLFo"  # ← Замени на свой токен от @BotFather

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("payout", payout))
    application.add_handler(CommandHandler("rating", rating))
    application.add_handler(CommandHandler("course", course))
    application.add_handler(CommandHandler("contact", contact))

    print("✅ TalentHub Telegram-бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()