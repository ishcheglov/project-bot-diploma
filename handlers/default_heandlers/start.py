from telebot.types import Message
from loader import bot
from database.db_controller import save_user
from loguru import logger


@bot.message_handler(commands=["start"])
@logger.catch
def bot_start(message: Message) -> None:
    """
    Функция, реагирующая на команду "start". Выводит приветственное сообщение.

    """

    save_user(message)
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, f"🏝 Я чат-бот от сайта турагентства 'Too Easy Travel'\n"
                                      f"Мы создаем для туристов комфортное проживание\n"
                                      f"приемлемые цены и рекомендуем удобно расположенные\n"
                                      f"отели. Наша задача сделать ваш отдых незабываемым.\n"
                                      f"Я помогу найти подходящий Вам отель.\n\n"                                                                  
                                      f"👋 Привет, {message.from_user.first_name}!\n"
                                      f"Для получения информации ведите команду: 🆘 <b>/help</b>", parse_mode="html")
