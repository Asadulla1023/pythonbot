from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes

from datetime import datetime

updater = Updater("5901133443:AAEpNA18Jk6m62xy8VPSsGkbiAHJTzP_D8A", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Hello {update.message.from_user.first_name}, Welcome to the Bot. Please write\
		/help to see the commands available."
    )


def help_commad(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""
Hi {update.message.from_user.username} write \n
1. /time
2. /img
2. /select
3. /buttons
"""
    )


def time_reply(update: Update, context: CallbackContext):
    now = datetime.now()
    data_time = now.strftime("%H: %M: %S")
    update.message.reply_text(f"{str(data_time)}")


def send_img_handler(update: Update, context: CallbackContext):
    update.message.bot.send_photo(
        photo=open("ss.jpg", "rb"), chat_id=update.message.chat_id
    )


def selectBtn_handler(update: Update, context: ContextTypes) -> None:
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
        ],
        [
            InlineKeyboardButton("⬅️", callback_data="leftArr"),
            InlineKeyboardButton("❌", callback_data="delete"),
            InlineKeyboardButton("➡️", callback_data="rightArr"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        """
1. Armani White - BILLIE EILISH.                                
2. bbno$ & Rich Brian - edamame                                 
3. Sxmpra - COWBELL WARRIOR!                                    
4. BoyWithUke - Toxic                                           
5. Enrasta - Jovannah (Original music)                          
""",
        reply_markup=reply_markup,
    )


def buttons(update: Update, context: CallbackContext):
    button = [
        [
            KeyboardButton(text="React darsliklar"),
            KeyboardButton(text="Next darsliklar"),
        ],
        [KeyboardButton(text="Back 🔙")],
    ]

    markup = ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text("Choose an option:", reply_markup=markup)




def button(update: Update, context: ContextTypes):
    query = update.callback_query
    keyboard = [[
        InlineKeyboardButton("❤️/💔", callback_data="likedis"),
        InlineKeyboardButton("❌", callback_data="delete")
    ]]

    keyboardMarkup = InlineKeyboardMarkup(keyboard)

    if query.data == "1":
        query.message.bot.send_audio(
            audio=open("./music/Armani White - BILLIE EILISH.mp3", "rb"),
            chat_id=query.message.chat_id,
            reply_markup=keyboardMarkup
        )

    if query.data == "2":
        query.message.bot.send_audio(
            audio=open("./music/bbno$ & Rich Brian - edamame.mp3", "rb"),
            chat_id=query.message.chat_id,
            reply_markup=keyboardMarkup
        )
    if query.data == "3":
        # query.message.reply_audio(audio=open("./music/Sxmpra - COWBELL WARRIOR!.mp3", 'rb'))
        query.message.bot.send_audio(
            audio=open("./music/Sxmpra - COWBELL WARRIOR!.mp3", "rb"),
            chat_id=query.message.chat_id,
            reply_markup=keyboardMarkup
        )
    if query.data == "4":
        query.message.bot.send_audio(
            audio=open("./music/BoyWithUke - Toxic.mp3", "rb"),
            chat_id=query.message.chat_id,
            reply_markup=keyboardMarkup
        )
    if query.data == "5":
        query.message.bot.send_audio(
            audio=open("./music/Mc Rd - Soca Soca Soca.mp3", "rb"),
            chat_id=query.message.chat_id,
            reply_markup=keyboardMarkup
        )

    if query.data == "delete":
        query.message.delete()


def err(update: Update, context: CallbackContext):
    print(f"Err {update}\nErr2 {context.error}")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(f"Unknown command —— {update.message.text}")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(f"Unknown text —— {update.message.text}")


updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("help", help_commad))
updater.dispatcher.add_handler(CommandHandler("time", time_reply))
updater.dispatcher.add_handler(CommandHandler("select", selectBtn_handler))
updater.dispatcher.add_handler(CommandHandler("buttons", buttons))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler("img", send_img_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))


updater.dispatcher.add_error_handler(err)

updater.start_polling()
