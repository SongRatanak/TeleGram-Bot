from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '7315085989:AAFbFytBPUvgfB7qwZ4MbeGE0vIYbAmaGzg'

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Check if the message is from a private chat and return if it is
    if update.effective_chat.type == "private":
        await update.message.reply_text("Sorry, this bot is only available in group chats.")
        return

    # Only respond if in a group chat or if directly called in a group
    if update.effective_chat.type == "group" and not update.message.text.startswith(f"/start@{context.bot.username}"):
        return

    # Store the user's username only if it hasn't been stored yet
    message = update.message or update.callback_query.message
    if 'username' not in context.user_data:
        username = message.from_user.username
        context.user_data['username'] = username if username else 'User'  # Default to 'User' if no username

    username = context.user_data['username']  # Retrieve stored username
    text = f"សួស្តី {username} 🙏🏻 \n ខ្ញុំជាជំនួយការនិមិ្មតរបស់មជ្ឈមណ្ឌលបច្ចេកវិទ្យាព័តមាន សូមជ្រើសរើសប្រភេទនៃបញ្ហារបស់អ្នក ខ្ញុំនឹងរីករាយក្នុងការជួយអ្នក។ 😊"
    
    keyboard = [
        [InlineKeyboardButton("1. ភ្លេចលេខកូដ Microsoft Team", callback_data='team')],
        [InlineKeyboardButton("2. ការប្រើប្រាស់ RUPP Wifi", callback_data='wifi')],
        [InlineKeyboardButton("3. ការប្រើប្រាស់ Moodle CCUN", callback_data='moodle')],
        [InlineKeyboardButton("4. ជជែកជាមួយក្រុមការងារ IT Center", callback_data='contact_it')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    else:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup)

# Main menu handler with submenu options
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    username = context.user_data.get('username', 'User')  # Retrieve the stored username
    if query.data == 'team':
        keyboard = [
            [InlineKeyboardButton("ក្នុងករណីអ្នកបានភ្ជាប់លេខទូរស័ព្ទរួចហើយ", callback_data='reset_with_phone')],
            [InlineKeyboardButton("ក្នុងករណីអ្នកមិនបានភ្ជាប់លេខទូរស័ព្ទ", callback_data='reset_without_phone')],
            [InlineKeyboardButton("Back", callback_data='back')],
        ]
        text = f"សូមជ្រើសរើសប្រភេទនៃបញ្ហាខាងក្រោម, {username}:"

    elif query.data == 'wifi':
        text = (
            "<b> ✅ ជំហ៊ានទី ១: ការទាញយក Microsoft Outlook</b>\n"
            "[សម្រាប់ Android]\nhttps://youtu.be/MnS_SMZhltg?si=mYIAltFBcKtWzire\n"
            "[សម្រាប់ IOS]\nhttps://youtu.be/P2SHPH3qcWA?si=dWRNwC_0LDHzqW3_\n\n"
            "<b> ✅ ជំហ៊ានទី ២: របៀបប្រើប្រាស Microsoft Outlook</b>\n"
            "[សម្រាប់ Android]\n https://youtu.be/l9Df_M8fyE4?si=Y_DZjMoLoonvdDWC\n"
            "[សម្រាប់ IOS]\n https://youtu.be/WMr2QLpp6Eo?si=WJYllw3FMVKpMAKD\n\n"
            "<b> ✅ ជំហ៊ានទី ៣: របៀបទៅយក លេខកូដWifi ពី Admin Central</b>\n"
            "[Link] \n https://youtu.be/gPOqGYq2d-4?si=SVqLnngLH-rlgQxk\n\n"
            "<b> ✅ ជំហ៊ានទី ៤: របៀបភ្ជាប់ RUPP-WiFi</b>\n"
            "[សម្រាប់ Android 13 Google Pixel 7]\nhttps://youtu.be/BVMyzzdfP1U?si=r3Mc2riBnecaEaLa\n"
            "[សម្រាប់ Android Xiaomi] \nhttps://youtu.be/ehcVKxjeGMs?si=rNgnzW-bFepMYz8q\n"
            "[សម្រាប់ IPhone/iPad]\n https://youtu.be/XmgJN1gKE6g?si=GdaFaopgmVsh3kx9 \n\n"
        )
        keyboard = [[InlineKeyboardButton("Back", callback_data='back')]]

    elif query.data == 'moodle':
        text = (
            "<b> 📕 របៀបរៀនជាមួយ CCUN eLeaning-Moodleសម្រាប់និស្សិត</b>\n"
            "[Watch here]\n https://youtu.be/1wqcNqTUqPM?si=i5BXPPGMEMPhelrP\n\n"
             "<b> 👦🏻 របៀបផ្លាស់ប្តូរ Profile  នឹងលេខកូដសម្ងាត់ CCUN eLeaning-Moodle សម្រាប់និស្សិត </b>\n"
            "[Watch here]\nhttps://youtu.be/kVl-UB-8mPU?si=iAXTvpKEJr9CouvX\n\n"
            "<b> 📱 របៀបរៀនក្នុងទូរស័ព្ទដៃ CCUN eLeaning-Moodle សម្រាប់និស្សិត </b>\n"
            "[Watch here]\n https://youtu.be/bfCjGhxviFI?si=giwi4CIkneUYOOCw\n\n"
            "<b> 💻 របៀបរៀននៅលើកុំព្យូរទ័រ CCUN eLeaning-Moodle សម្រាប់និស្សិត </b>\n"
            "[Watch here]\n https://youtu.be/qAloFVeyH7U?si=uttbOsksCho51aJP"
        )
        keyboard = [[InlineKeyboardButton("Back", callback_data='back')]]
        
    elif query.data == 'contact_it':
        text = f"ដើម្បីជជែកជាមួយក្រុមការងារ IT Center សូមបើកបុតនេះ: <a href='https://t.me/ITCenter_Helpdesk_bot'> 🤖 IT Center Bot</a>"
        keyboard = [[InlineKeyboardButton("Back", callback_data='back')]]
        
    else:
        await start(update, context)
        return

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode="HTML")

# Submenu handler for Microsoft Team options
async def submenu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'reset_with_phone':
        text = (
            "ក្នុងករណីអ្នកបានភ្ជាប់លេខទូរស័ព្ទរួចហើយ:\n"
            "[Android]\n https://youtu.be/kkRkylDla_w?si=su_Py_1ErRwfg_qy\n"
            "[iOS]\n https://youtu.be/DzUOGHssEA8?si=zM_IDEQrNW4--pF5\n"
            "[Windows & Mac]\n https://youtu.be/YVOmx2qwIiI?si=zkji6sfhfnU2VkXj"
        )
    elif query.data == 'reset_without_phone':
        text = (
            "ក្នុងករណីអ្នកមិនបានភ្ជាប់លេខទូរស័ព្ទ:\n"
            "[Phone]\n https://youtu.be/0o2rJjq7zmc?si=AiG3Zt_7o2oy2QG5"
        )
    else:
        await start(update, context)
        return

    keyboard = [[InlineKeyboardButton("Back", callback_data='team')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup)

# Main function to set up the bot
def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu_handler, pattern='^(team|wifi|moodle|contact_it|back)$'))
    application.add_handler(CallbackQueryHandler(submenu_handler, pattern='^(reset_with_phone|reset_without_phone)$'))
    
    # Start polling for updates and handle incoming updates live
    application.run_polling()

if __name__ == '__main__':
    main()
