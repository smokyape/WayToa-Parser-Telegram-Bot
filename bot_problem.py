from telegram.ext import Updater, CommandHandler
import csv

TOKEN = '6169321212:AAEEfrli8agy5l-7NmzaejuzluSrm7No4Ww'
filename = 'percod.csv'

def start(update, context):
    context.user_data['start'] = 0
    update.message.reply_text('Привет! Введите /next, чтобы получить следующие 10 строк из CSV-файла.')

def next(update, context):
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < context.user_data['start']:
                continue
            if i >= context.user_data['start'] + 10:
                break
            rows.append(row)
    if len(rows) > 0:
        result = '\n'.join([', '.join(row) for row in rows])
        update.message.reply_text('Вот следующие 10 строк:\n' + result)
        context.user_data['start'] += 10
    else:
        update.message.reply_text('Все строки уже были выведены.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("next", next))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()



