from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# الردود المرتبطة بكل رسالة
responses = {
    "i love you": "i meaw u 😽",
    "i hate you": "fuck u 🙀",
    "do you want food?": "yeeeeees 🍗",
    "i have food": "i love u 😻",
    "how are you?": "i want food 🐟",
    "تحبيني؟": "اذا تجيبلي تونة اي 🐱"
}

# الكلمات الي راح تطلع كأزرار في الكيبورد
keyboard_buttons = [
    ["i love you", "i hate you"],
    ["do you want food?", "i have food"],
    ["how are you?", "تحبيني؟"]
]

# كيبورد جاهز للرد
reply_keyboard = ReplyKeyboardMarkup(keyboard_buttons, resize_keyboard=True)

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "😺 Hi! I'm your cat bot. Choose something from the buttons below:",
        reply_markup=reply_keyboard
    )

# دالة للردود حسب الزر
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()
    reply = responses.get(user_text, "meow? 😼")
    await update.message.reply_text(reply, reply_markup=reply_keyboard)

# توكن البوت - غيره بالتوكن مالتك
BOT_TOKEN = "8234996962:AAFKvBYQnVWowg_5s_MHVrJ-O9gw8MCDwkk"

# إعداد البوت
app = ApplicationBuilder().token(BOT_TOKEN).build()

# تسجيل الأوامر والمحادثات
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🐾 Bot is running...")

# تشغيل البوت
app.run_polling()
