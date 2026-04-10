import telebot
from telebot import types

# --- CONFIGURATION ---
TOKEN = '8662593320:AAH2OcQocxGG0uiS9fh0ulgUa7bNuIO23Jw'
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 123456789  
CHANNEL_ID = "@ehtio_free_internet_et"
GROUP_ID = "@crypto_free_internet_et"

# --- DATA STORAGE ---
user_languages = {} 

# --- TRANSLATIONS ---
LANG_DATA = {
    'om': {
        'welcome': "✨ Assalaamu Alaykum! Gola barbaaddan filadhaa:",
        'join_err': "⚠️ Botii kana fayyadamuuf dura Channel fi Group keenya Join gochuu qabdu!",
        'audio_btn': '🔊 Gola Audio (114)',
        'my_bot': '👤 My Bot (Kiyya)',
        'back': '🔙 Menu Guddaa',
        'choose_cat': "🎧 Garee suuraa filadhaa:",
        'verify': "✅ Mirkaneessi (Join Godheera)",
        'lang_set': "✅ Afaan Oromoo filatameera!",
    },
    'en': {
        'welcome': "✨ Assalaamu Alaykum! Please choose a category:",
        'join_err': "⚠️ You must join our Channel and Group to use this bot!",
        'audio_btn': '🔊 Audio Gallery (114)',
        'my_bot': '👤 My Bot',
        'back': '🔙 Main Menu',
        'choose_cat': "🎧 Choose a Surah group:",
        'verify': "✅ Verify (Joined)",
        'lang_set': "✅ English language selected!",
    },
    'am': {
        'welcome': "✨ አሰላሙ አለይኩም! የሚፈልጉትን ክፍል ይምረጡ፦",
        'join_err': "⚠️ ይህንን ቦት ለመጠቀም መጀመሪያ ቻናላችንን እና ግሩፓችንን መቀላቀል አለብዎት!",
        'audio_btn': '🔊 የድምጽ ማህደር (114)',
        'my_bot': '👤 የእኔ ቦት',
        'back': '🔙 ወደ ዋና ማውጫ',
        'choose_cat': "🎧 የሱራ ምድብ ይምረጡ፦",
        'verify': "✅ አረጋግጥ (ተቀላቅያለሁ)",
        'lang_set': "✅ አማርኛ ቋንቋ ተመርጧል!",
    },
    'ar': {
        'welcome': "✨ السلام عليكم! يرجى اختيار القسم:",
        'join_err': "⚠️ يجب عليك الانضمام إلى القناة والمجموعة لاستخدام هذا البوت!",
        'audio_btn': '🔊 مكتبة الصوت (114)',
        'my_bot': '👤 حسابي',
        'back': '🔙 القائمة الرئيسية',
        'choose_cat': "🎧 اختر مجموعة السورة:",
        'verify': "✅ تحقق (تم الانضمام)",
        'lang_set': "✅ تم اختيار اللغة العربية!",
    }
}

# --- SURAH DATA (1-114) ---
SURAH_NAMES = {
    "1-12": ["1. Al-Faatiha", "2. Al-Baqarah", "3. Aal-Imran", "4. An-Nisaa", "5. Al-Ma'idah", "6. Al-An'am", "7. Al-A'raf", "8. Al-Anfal", "9. At-Tawbah", "10. Yunus", "11. Hud", "12. Yusuf"],
    "13-24": ["13. Ar-Ra'd", "14. Ibrahim", "15. Al-Hijr", "16. An-Nahl", "17. Al-Isra", "18. Al-Kahf", "19. Maryam", "20. Ta-Ha", "21. Al-Anbiya", "22. Al-Hajj", "23. Al-Mu'minun", "24. An-Nur"],
    "25-36": ["25. Al-Furqan", "26. Ash-Shu'ara", "27. An-Naml", "28. Al-Qasas", "29. Al-Ankabut", "30. Ar-Rum", "31. Luqman", "32. As-Sajdah", "33. Al-Ahzab", "34. Saba", "35. Fatir", "36. Ya-Sin"],
    "37-48": ["37. As-Saffat", "38. Sad", "39. Az-Zumar", "40. Ghafir", "41. Fussilat", "42. Ash-Shura", "43. Az-Zukhruf", "44. Ad-Dukhan", "45. Al-Jathiyah", "46. Al-Ahqaf", "47. Muhammad", "48. Al-Fath"],
    "49-60": ["49. Al-Hujurat", "50. Qaf", "51. Adh-Dhariyat", "52. At-Tur", "53. An-Najm", "54. Al-Qamar", "55. Ar-Rahman", "56. Al-Waqi'ah", "57. Al-Hadid", "58. Al-Mujadila", "59. Al-Hashr", "60. Al-Mumtahanah"],
    "61-72": ["61. As-Saff", "62. Al-Jumu'ah", "63. Al-Munafiqun", "64. At-Taghabun", "65. At-Talaq", "66. At-Tahrim", "67. Al-Mulk", "68. Al-Qalam", "69. Al-Haqqah", "70. Al-Ma'arij", "71. Nuh", "72. Al-Jinn"],
    "73-84": ["73. Al-Muzzammil", "74. Al-Muddaththir", "75. Al-Qiyamah", "76. Al-Insan", "77. Al-Mursalat", "78. An-Naba", "79. An-Nazi'at", "80. 'Abasa", "81. At-Takwir", "82. Al-Infitar", "83. Al-Mutaffifin", "84. Al-Inshiqaq"],
    "85-96": ["85. Al-Buruj", "86. At-Tariq", "87. Al-A'la", "88. Al-Ghashiyah", "89. Al-Fajr", "90. Al-Balad", "91. Ash-Shams", "92. Al-Layl", "93. Ad-Duha", "94. Ash-Sharh", "95. At-Tin", "96. Al-'Alaq"],
    "97-108": ["97. Al-Qadr", "98. Al-Bayyinah", "99. Az-Zalzalah", "100. Al-'Adiyat", "101. Al-Qari'ah", "102. At-Takathur", "103. Al-'Asr", "104. Al-Humazah", "105. Al-Fil", "106. Quraysh", "107. Al-Ma'un", "108. Al-Kawthar"],
    "109-114": ["109. Al-Kafirun", "110. An-Nasr", "111. Al-Masad", "112. Al-Ikhlas", "113. Al-Falaq", "114. An-Nas"]
}

# --- FUNCTIONS ---
def is_user_joined(user_id):
    try:
        ch = bot.get_chat_member(CHANNEL_ID, user_id)
        gr = bot.get_chat_member(GROUP_ID, user_id)
        allowed = ['member', 'administrator', 'creator']
        return ch.status in allowed and gr.status in allowed
    except: return False

def lang_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("Oromoo 🌳", callback_data="set_om"),
        types.InlineKeyboardButton("English 🇬🇧", callback_data="set_en"),
        types.InlineKeyboardButton("አማርኛ 🇪🇹", callback_data="set_am"),
        types.InlineKeyboardButton("العربية 🇸🇦", callback_data="set_ar")
    ]
    return markup.add(*btns)

def join_buttons(lang):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("📢 Channel", url=f"https://t.me/{CHANNEL_ID[1:]}")
    btn2 = types.InlineKeyboardButton("💬 Group", url=f"https://t.me/{GROUP_ID[1:]}")
    btn3 = types.InlineKeyboardButton(LANG_DATA[lang]['verify'], callback_data="check_join")
    return markup.add(btn1, btn2, btn3)

def main_menu_kb(lang):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(LANG_DATA[lang]['audio_btn'], LANG_DATA[lang]['my_bot'])
    markup.add("🌐 Change Language")
    return markup

def audio_categories_kb(lang):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btns = [types.KeyboardButton(f"🎼 {key}") for key in SURAH_NAMES.keys()]
    markup.add(*btns).add(LANG_DATA[lang]['back'])
    return markup

# --- HANDLERS ---

@bot.message_handler(commands=['start'])
def start_message(message):
    # Menu yoo jiraate dura balleessi
    bot.send_message(message.chat.id, "Please choose language / Afaan filadhu:", reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "Select Language:", reply_markup=lang_keyboard())

@bot.callback_query_handler(func=lambda call: call.data.startswith('set_'))
def handle_lang_selection(call):
    lang_code = call.data.split('_')[1]
    user_languages[call.from_user.id] = lang_code
    
    # Afaan erga filatamee booda join sakatta'i
    if is_user_joined(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, LANG_DATA[lang_code]['welcome'], reply_markup=main_menu_kb(lang_code))
    else:
        # Join yoo hin godhin xalayaa join qofa agarsiisi
        bot.edit_message_text(LANG_DATA[lang_code]['join_err'], call.message.chat.id, call.message.message_id, reply_markup=join_buttons(lang_code))

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def verify_membership(call):
    lang = user_languages.get(call.from_user.id, 'om')
    if is_user_joined(call.from_user.id):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, LANG_DATA[lang]['welcome'], reply_markup=main_menu_kb(lang))
    else:
        bot.answer_callback_query(call.id, "❌ Join First! / Maaloo dura Join godhaa!", show_alert=True)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    uid = message.from_user.id
    lang = user_languages.get(uid, None)
    
    # 1. Afaan yoo hin filatamne ta'e dura afaan filachiisi
    if lang is None:
        bot.send_message(message.chat.id, "Please choose language first:", reply_markup=lang_keyboard())
        return

    # 2. Join yoo hin godhin ta'e menu kamuu hin agarsiisin
    if not is_user_joined(uid):
        bot.send_message(message.chat.id, LANG_DATA[lang]['join_err'], reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, "Join:", reply_markup=join_buttons(lang))
        return

    # 3. Dalagaa Botii (Erga Join godhee booda)
    text = message.text
    if text == "🌐 Change Language":
        bot.send_message(message.chat.id, "Select language:", reply_markup=lang_keyboard())
    elif text == LANG_DATA[lang]['audio_btn']:
        bot.send_message(message.chat.id, LANG_DATA[lang]['choose_cat'], reply_markup=audio_categories_kb(lang))
    elif text == LANG_DATA[lang]['back']:
        bot.send_message(message.chat.id, LANG_DATA[lang]['welcome'], reply_markup=main_menu_kb(lang))
    elif text == LANG_DATA[lang]['my_bot']:
        bot.send_message(message.chat.id, f"👤 Name: {message.from_user.first_name}\n🆔 ID: `{uid}`", parse_mode="Markdown")
    elif text.startswith('🎼 '):
        key = text.replace('🎼 ', '').strip()
        if key in SURAH_NAMES:
            markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            btns = [types.KeyboardButton(name) for name in SURAH_NAMES[key]]
            markup.add(*btns).add(LANG_DATA[lang]['back'])
            bot.send_message(message.chat.id, f"Suuraa {key}:", reply_markup=markup)
    elif '.' in text and text.split('.')[0].isdigit():
        try:
            num = text.split('.')[0].strip().zfill(3)
            audio_url = f"https://server8.mp3quran.net/afs/{num}.mp3"
            bot.send_chat_action(message.chat.id, 'upload_audio')
            bot.send_audio(message.chat.id, audio_url, caption=f"🔊 {text}\n\n{CHANNEL_ID}")
        except:
            bot.send_message(message.chat.id, "⚠️ Error!")

print("Botiin hojii jalqabeera...")
bot.polling(none_stop=True)# Koodii kee dhuma irratti kan jiru:
try:
    print("Botiin hojii jalqabeera...")
    bot.polling(none_stop=True, timeout=60)
except Exception as e:
    print(f"Error: {e}")

