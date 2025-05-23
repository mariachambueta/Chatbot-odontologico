import telebot
from telebot import types
from db import crear_tabla_citas, guardar_cita, obtener_citas, eliminar_cita

# Token de tu bot aquí
API_TOKEN = "8003877407:AAGai3qjxuEOrVaS5_-rPcq2f7rkSEa-Q-k"
bot = telebot.TeleBot(API_TOKEN)

# Crear tabla al iniciar
crear_tabla_citas()

# Estado temporal para manejo de citas y diálogos por usuario
usuarios_estado = {}

# Función para detectar idioma simple (español / inglés)
def detectar_idioma(texto):
    texto = texto.lower()
    palabras_esp = ["hola", "agendar", "cita", "cancelar", "menu", "ayuda"]
    palabras_eng = ["hi", "schedule", "appointment", "cancel", "help", "menu"]

    if any(p in texto for p in palabras_esp):
        return "es"
    elif any(p in texto for p in palabras_eng):
        return "en"
    else:
        # Default español
        return "es"

# Textos en ambos idiomas para reutilizar
TEXTOS = {
    "menu_es": "📌 Selecciona una opción del menú:\n\n🗓 Agendar cita\n❌ Cancelar cita\n📋 Ver mis citas\n🦷 Servicios odontológicos\nℹ️ Información del consultorio\n📞 Contactar al consultorio\n❓ Ayuda\n🚪 Salir",
    "menu_en": "📌 Please choose an option:\n\n🗓 Book appointment\n❌ Cancel appointment\n📋 View my appointments\n🦷 Dental services\nℹ️ Clinic information\n📞 Contact the clinic\n❓ Help\n🚪 Exit",

    "saludo_es": "👋 ¡Hola! Soy Fivebot 🦷\n¿En qué puedo ayudarte?",
    "saludo_en": "👋 Hi! I'm Fivebot 🦷\nHow can I assist you?",

    "seleccion_dia_es": "📅 Selecciona un día para tu cita:",
    "seleccion_dia_en": "📅 Select a day for your appointment:",

    "seleccion_hora_es": "⏰ Ahora selecciona una hora:",
    "seleccion_hora_en": "⏰ Now select a time:",

    "cita_agendada_es": "✅ Cita programada para el {}.\n📞 Un asesor se pondrá en contacto contigo pronto. 😊",
    "cita_agendada_en": "✅ Appointment scheduled for {}.\n📞 An agent will contact you soon. 😊",

    "no_entendido_es": "🤔 No entendí eso. Por favor usa el menú.",
    "no_entendido_en": "🤔 I didn’t understand. Please use the menu.",

    "cancelar_cita_es": "🗑️ Selecciona la cita que deseas cancelar:",
    "cancelar_cita_en": "🗑️ Select the appointment you want to cancel:",

    "cita_cancelada_es": "✅ Cita cancelada correctamente.",
    "cita_cancelada_en": "✅ Appointment cancelled successfully.",

    "sin_citas_es": "ℹ️ No tienes citas programadas.",
    "sin_citas_en": "ℹ️ You have no scheduled appointments.",

    "ayuda_es": "Puedes agendar, cancelar o ver tus citas usando el menú.",
    "ayuda_en": "You can schedule, cancel, or view your appointments using the menu.",

    "volver_menu_es": "🔙 Volver al menú",
    "volver_menu_en": "🔙 Back to menu",

    "ver_citas_es": "📋 Aquí están tus citas programadas:",
    "ver_citas_en": "📋 Here are your scheduled appointments:",

    "servicios_es": "🦷 Servicios odontológicos disponibles:\n- Limpieza dental\n- Ortodoncia\n- Blanqueamiento\n- Consultas generales",
    "servicios_en": "🦷 Available dental services:\n- Dental cleaning\n- Orthodontics\n- Whitening\n- General consultations",

    "info_consultorio_es": "ℹ️ Información del consultorio:\nDirección: Calle 123 #45-67\nTeléfono: +57 300 123 4567\nHorario: Lun-Vie 8am - 6pm",
    "info_consultorio_en": "ℹ️ Clinic information:\nAddress: Calle 123 #45-67\nPhone: +57 300 123 4567\nHours: Mon-Fri 8am - 6pm",

    "contacto_consultorio_es": "📞 Para contactar al consultorio, llama al +57 300 123 4567 o envía un correo a contacto@consultorio.com",
    "contacto_consultorio_en": "📞 To contact the clinic, call +57 300 123 4567 or email contact@clinic.com",

    "salir_es": "🚪 Gracias por usar el bot. ¡Hasta luego!",
    "salir_en": "🚪 Thanks for using the bot. Goodbye!",
}

# Fechas y horas ejemplo (puedes modificar)
FECHAS = ["2025-05-26", "2025-05-28", "2025-05-30"]
HORAS = ["09:00", "11:00", "15:00"]

def crear_menu_opciones(idioma):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if idioma == "es":
        markup.add(
            "🗓 Agendar cita", "❌ Cancelar cita", "📋 Ver mis citas",
            "🦷 Servicios odontológicos", "ℹ️ Información del consultorio",
            "📞 Contactar al consultorio", "❓ Ayuda", "🚪 Salir"
        )
    else:
        markup.add(
            "🗓 Book appointment", "❌ Cancel appointment", "📋 View my appointments",
            "🦷 Dental services", "ℹ️ Clinic information",
            "📞 Contact the clinic", "❓ Help", "🚪 Exit"
        )
    return markup

def crear_menu_fechas(idioma):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for fecha in FECHAS:
        markup.add(fecha)
    if idioma == "es":
        markup.add(TEXTOS["volver_menu_es"])
    else:
        markup.add(TEXTOS["volver_menu_en"])
    return markup

def crear_menu_horas(idioma):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for hora in HORAS:
        markup.add(hora)
    if idioma == "es":
        markup.add(TEXTOS["volver_menu_es"])
    else:
        markup.add(TEXTOS["volver_menu_en"])
    return markup

def crear_menu_citas(citas, idioma):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for cita in citas:
        # cita = (id, fecha_hora)
        texto = f"{cita[0]} - {cita[1]}"
        markup.add(texto)
    if idioma == "es":
        markup.add(TEXTOS["volver_menu_es"])
    else:
        markup.add(TEXTOS["volver_menu_en"])
    return markup

@bot.message_handler(func=lambda m: True)
def manejar_mensaje(message):
    chat_id = message.chat.id
    texto = message.text.strip()
    idioma = detectar_idioma(texto)

    # Estado del usuario
    estado = usuarios_estado.get(chat_id, {"estado": None})

    # Si usuario quiere volver al menú principal en cualquier paso
    if texto in [TEXTOS["volver_menu_es"], TEXTOS["volver_menu_en"]]:
        usuarios_estado.pop(chat_id, None)
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["menu_es"], reply_markup=crear_menu_opciones(idioma))
        else:
            bot.send_message(chat_id, TEXTOS["menu_en"], reply_markup=crear_menu_opciones(idioma))
        return

    # Estado: esperando selección de día para agendar
    if estado.get("estado") == "esperando_dia":
        if texto in FECHAS:
            usuarios_estado[chat_id]["dia"] = texto
            usuarios_estado[chat_id]["estado"] = "esperando_hora"
            if idioma == "es":
                bot.send_message(chat_id, TEXTOS["seleccion_hora_es"], reply_markup=crear_menu_horas(idioma))
            else:
                bot.send_message(chat_id, TEXTOS["seleccion_hora_en"], reply_markup=crear_menu_horas(idioma))
        else:
            if idioma == "es":
                bot.send_message(chat_id, "❌ Fecha inválida. Por favor selecciona una fecha del menú.")
            else:
                bot.send_message(chat_id, "❌ Invalid date. Please select a date from the menu.")
        return

    # Estado: esperando selección de hora para agendar
    if estado.get("estado") == "esperando_hora":
        if texto in HORAS:
            fecha_hora = f"{usuarios_estado[chat_id]['dia']} {texto}"
            guardar_cita(chat_id, fecha_hora)
            usuarios_estado.pop(chat_id)
            if idioma == "es":
                bot.send_message(chat_id, TEXTOS["cita_agendada_es"].format(fecha_hora), reply_markup=crear_menu_opciones(idioma))
            else:
                bot.send_message(chat_id, TEXTOS["cita_agendada_en"].format(fecha_hora), reply_markup=crear_menu_opciones(idioma))
        else:
            if idioma == "es":
                bot.send_message(chat_id, "❌ Hora inválida. Por favor selecciona una hora del menú.")
            else:
                bot.send_message(chat_id, "❌ Invalid time. Please select a time from the menu.")
        return

    # Estado: esperando selección de cita para cancelar
    if estado.get("estado") == "esperando_cancelacion":
        if texto == TEXTOS["volver_menu_es"] or texto == TEXTOS["volver_menu_en"]:
            usuarios_estado.pop(chat_id, None)
            if idioma == "es":
                bot.send_message(chat_id, TEXTOS["menu_es"], reply_markup=crear_menu_opciones(idioma))
            else:
                bot.send_message(chat_id, TEXTOS["menu_en"], reply_markup=crear_menu_opciones(idioma))
            return
        # Esperamos formato: "id - fecha_hora"
        try:
            id_cita = int(texto.split(" - ")[0])
            eliminado = eliminar_cita(id_cita, chat_id)
            if eliminado:
                if idioma == "es":
                    bot.send_message(chat_id, TEXTOS["cita_cancelada_es"], reply_markup=crear_menu_opciones(idioma))
                else:
                    bot.send_message(chat_id, TEXTOS["cita_cancelada_en"], reply_markup=crear_menu_opciones(idioma))
            else:
                if idioma == "es":
                    bot.send_message(chat_id, "❌ No se pudo cancelar esa cita. Intenta de nuevo.")
                else:
                    bot.send_message(chat_id, "❌ Could not cancel that appointment. Try again.")
            usuarios_estado.pop(chat_id, None)
        except Exception:
            if idioma == "es":
                bot.send_message(chat_id, "❌ Formato inválido. Por favor selecciona la cita del menú.")
            else:
                bot.send_message(chat_id, "❌ Invalid format. Please select the appointment from the menu.")
        return

    # Menú principal según texto
    if texto in ["🗓 Agendar cita", "🗓 Book appointment"]:
        usuarios_estado[chat_id] = {"estado": "esperando_dia"}
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["seleccion_dia_es"], reply_markup=crear_menu_fechas(idioma))
        else:
            bot.send_message(chat_id, TEXTOS["seleccion_dia_en"], reply_markup=crear_menu_fechas(idioma))
        return

    if texto in ["❌ Cancelar cita", "❌ Cancel appointment"]:
        citas = obtener_citas(chat_id)
        if not citas:
            if idioma == "es":
                bot.send_message(chat_id, TEXTOS["sin_citas_es"], reply_markup=crear_menu_opciones(idioma))
            else:
                bot.send_message(chat_id, TEXTOS["sin_citas_en"], reply_markup=crear_menu_opciones(idioma))
            return
        usuarios_estado[chat_id] = {"estado": "esperando_cancelacion"}
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["cancelar_cita_es"], reply_markup=crear_menu_citas(citas, idioma))
        else:
            bot.send_message(chat_id, TEXTOS["cancelar_cita_en"], reply_markup=crear_menu_citas(citas, idioma))
        return

    if texto in ["📋 Ver mis citas", "📋 View my appointments"]:
        citas = obtener_citas(chat_id)
        if not citas:
            if idioma == "es":
                bot.send_message(chat_id, TEXTOS["sin_citas_es"], reply_markup=crear_menu_opciones(idioma))
            else:
                bot.send_message(chat_id, TEXTOS["sin_citas_en"], reply_markup=crear_menu_opciones(idioma))
            return
        lista_citas = "\n".join([f"- {c[1]}" for c in citas])
        if idioma == "es":
            bot.send_message(chat_id, f"{TEXTOS['ver_citas_es']}\n{lista_citas}", reply_markup=crear_menu_opciones(idioma))
        else:
            bot.send_message(chat_id, f"{TEXTOS['ver_citas_en']}\n{lista_citas}", reply_markup=crear_menu_opciones(idioma))
        return

    if texto in ["🦷 Servicios odontológicos", "🦷 Dental services"]:
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["servicios_es"], reply_markup=crear_menu_opciones(idioma))
        else:
            bot.send_message(chat_id, TEXTOS["servicios_en"], reply_markup=crear_menu_opciones(idioma))
        return

    if texto in ["ℹ️ Información del consultorio", "ℹ️ Clinic information"]:
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["info_consultorio_es"], reply_markup=crear_menu_opciones(idioma))
        else:
            bot.send_message(chat_id, TEXTOS["info_consultorio_en"], reply_markup=crear_menu_opciones(idioma))
        return

    if texto in ["📞 Contactar al consultorio", "📞 Contact the clinic"]:
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["contacto_consultorio_es"], reply_markup=crear_menu_opciones(idioma))
        else:
            bot.send_message(chat_id, TEXTOS["contacto_consultorio_en"], reply_markup=crear_menu_opciones(idioma))
        return

    if texto in ["❓ Ayuda", "❓ Help"]:
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["ayuda_es"], reply_markup=crear_menu_opciones(idioma))
        else:
            bot.send_message(chat_id, TEXTOS["ayuda_en"], reply_markup=crear_menu_opciones(idioma))
        return

    if texto in ["🚪 Salir", "🚪 Exit"]:
        usuarios_estado.pop(chat_id, None)
        if idioma == "es":
            bot.send_message(chat_id, TEXTOS["salir_es"], reply_markup=types.ReplyKeyboardRemove())
        else:
            bot.send_message(chat_id, TEXTOS["salir_en"], reply_markup=types.ReplyKeyboardRemove())
        return

    # Si no reconoce comando
    if idioma == "es":
        bot.send_message(chat_id, TEXTOS["no_entendido_es"], reply_markup=crear_menu_opciones(idioma))
    else:
        bot.send_message(chat_id, TEXTOS["no_entendido_en"], reply_markup=crear_menu_opciones(idioma))


if __name__ == "__main__":
    print("Bot iniciado...")
    bot.polling()
