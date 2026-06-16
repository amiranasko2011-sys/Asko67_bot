8910048683:AAENK_cjf5YvGFGqNpG6xM6wgXyGwkKswRA
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
BOT_TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"
API_KEY = "ТВОЙ_OPENROUTER_KEY"

bot = telebot.TeleBot(BOT_TOKEN)

def ask_ai(text):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [{"role": "user", "content": text}]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я AI бот. Задай вопрос 🙂")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        answer = ask_ai(message.text)
        bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, "Ошибка AI 😔 попробуй позже")

bot.polling()
