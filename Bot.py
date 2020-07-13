from Partida import Partida
from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def start(bot, update):
    update.message.reply_text('Texto Informativo')

def main():
    updater = Updater("424323881:AAG1ZFSVti-959-oQCQH8Oadr-WxuM0qcaY")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", start))

    dispatcher.add_error_handler(error)

    updater.start_polling()
if __name__ == '__main__':
    main()