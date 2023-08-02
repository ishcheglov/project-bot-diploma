from loader import bot, db
import handlers
import config_data
from utils.set_bot_commands import set_default_commands
from keyboards.inline.filters import CityCallbackFilter, HistoryCallbackFilter
from telebot.custom_filters import StateFilter, IsDigitFilter
from database.models import User, History, SearchResult
from loguru import logger


@logger.catch
def run_bot() -> None:
    with db:
        db.create_tables([User, History, SearchResult])
    set_default_commands(bot)
    bot.add_custom_filter(StateFilter(bot))
    bot.add_custom_filter(IsDigitFilter())
    bot.add_custom_filter(CityCallbackFilter())
    bot.add_custom_filter(HistoryCallbackFilter())
    bot.polling(non_stop=True)


if __name__ == '__main__':
    run_bot()
