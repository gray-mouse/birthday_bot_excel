import telebot
from datetime import datetime
import openpyxl as xl
import re
import schedule
from schedule import every, repeat, run_pending
import time


bot = telebot.TeleBot("TOKEN", parse_mode=None)


def BirthdayNotification():


    path = r'FILE PATH'
    wb = xl.load_workbook(filename=path, read_only=True)
    ws = wb['Sheet']

    current_datetime = datetime.now()
    current_date = current_datetime.date()
    date = str(current_date)[5:10]  # Формат строки YYYY-MM-DD, после среза MM-DD

    #val = ws.cell(row=173, column=3).value


    for row in ws.rows:
        for cell in row:
            if re.match(date, str(cell.value)[5:10]):
                msg = " Сегодня празднует свой день рождения " + "\n" + row[3].internal_value + "\n" + row[2].internal_value + "\n"
                # для отображения сожержимого строки с рядом стоящей искомой ячейкой надо изменить параметр row, где значение параметра будет номер столбца


                bot.send_message(chat_id=1717876558 ,text=msg)
    bot.infinity_polling()

#schedule.every(2).minutes.do(BirthdayNotification)

job = schedule.every().minutes.at('2').do(BirthdayNotification)
schedule.cancel_job(job)

