import telebot
from telebot import types

# 📌 Token del bot (REEMPLÁZALO POR TU TOKEN SEGURO)
TOKEN = "8003877407:AAGai3qjxuEOrVaS5_-rPcq2f7rkSEa-Q-k"
bot = telebot.TeleBot(TOKEN)

# 📌 Función para mostrar el menú principal
def mostrar_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("🦷 Consejos")
    btn2 = types.KeyboardButton("📅 Agendar cita")
    btn3 = types.KeyboardButton("❓ Preguntas frecuentes")
    btn4 = types.KeyboardButton("☎ Información general")
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(
        chat_id,
        "👋 ¡Hola! Soy *Fivebot* 🦷\n"
        "¿En qué puedo ayudarte?\n\n"
        "📌 *Selecciona una opción del menú:*",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# 📌 Manejo del comando /start
@bot.message_handler(commands=["start"])
def start(message):
    mostrar_menu(message.chat.id)

# 📌 Responder a mensajes
@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()

    # 🚑 Consejos de higiene y dolor de muela
    if "consejos" in texto:
        bot.reply_to(
            message, 
            "*Recomendaciones para el dolor de muelac:*\n"
            "✅ Enjuágate con agua tibia y sal.\n"
            "✅ Toma un analgésico si es necesario.\n"
            "✅ *Agenda cita para revisión.*\n\n"
            "*Consejos para una buena higiene bucal:*\n"
            "✅ Cepíllate *mínimo* 2 veces al día con pasta con flúor.\n"
            "✅ Usa *hilo dental* diariamente.\n"
            "✅ Reduce el consumo de *azúcar* y *bebidas ácidas*.\n"
            "✅ *Visita al dentista* cada 6 meses.",
            parse_mode="Markdown"
        )

    # 📅 Agendar cita
    elif "agendar cita" in texto:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("📆 Lunes")
        btn2 = types.KeyboardButton("📆 Miércoles")
        btn3 = types.KeyboardButton("📆 Viernes")
        btn4 = types.KeyboardButton("🔙 Volver al menú")
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(
            message.chat.id,
            "📅 *Selecciona un día para tu cita:*",
            reply_markup=markup,
            parse_mode="Markdown"
        )

    elif "lunes" in texto or "miércoles" in texto or "viernes" in texto:
        bot.reply_to(
            message, 
            f"✅ *Cita programada para el {message.text}.*\n"
            "📞 Un asesor se pondrá en contacto contigo pronto. 😊",
            parse_mode="Markdown"
        )

    # ❓ Preguntas frecuentes
    elif "preguntas frecuentes" in texto:
        bot.reply_to(
            message, 
            "❓ *Preguntas Frecuentes:*\n"
            "1️⃣ *¿Cada cuánto debo ir al dentista?*\n"
            "   - *Respuesta:* Cada 6 meses.\n\n"
            "2️⃣ *¿Qué hago si me sangran las encías?*\n"
            "   - *Respuesta:* Usa un cepillo suave y consulta a tu odontólogo.\n\n"
            "3️⃣ *¿Es recomendable el blanqueamiento dental?*\n"
            "   - *Respuesta:* Sí, pero siempre con supervisión profesional.",
            parse_mode="Markdown"
        )

    # ☎ Información general
    elif "información" in texto or "contacto" in texto:
        bot.reply_to(
            message, 
            "☎ *Información general:*\n"
            "📧 *Email:* contacto@odontoasistente.com\n"
            "📞 *Teléfono:* +57 3182284445\n"
            "🌐 *Página web:* www.fivebotodontologico.com\n"
            "➡️ *Dirección:* calle69b#00-01",
            parse_mode="Markdown"
        )

    # 🔙 Volver al menú
    elif "volver al menú" in texto:
        mostrar_menu(message.chat.id)

    # 📝 Responder a mensajes no predefinidos
    else:
        respuestas_generales = {
            "hola": "¡Hola! 😊 ¿En qué puedo ayudarte?",
            "gracias": "¡De nada! Siempre aquí para ayudarte. 🦷",
            "cómo estás": "¡Estoy listo para ayudarte con cualquier duda odontológica! 🦷",
            "adiós": "¡Hasta luego! No olvides cuidar tu sonrisa. 😁"
        }

        # Si el mensaje está en la lista de respuestas generales
        if texto in respuestas_generales:
            bot.reply_to(message, respuestas_generales[texto])
        else:
            bot.reply_to(
                message, 
                "🤔 No entiendo tu consulta. ¿Puedes reformularla?\n"
                "📌 Usa el menú para seleccionar una opción.",
                parse_mode="Markdown"
            )

# 📌 Iniciar el bot
if __name__ == "__main__":
    print("🤖 Bot iniciado...")
    bot.polling(none_stop=True)

