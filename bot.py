from telegram.ext import *
from urllib.request import urlopen
import json
import re
from datetime import datetime
import calendar
import os
from dotenv import load_dotenv

trek_no = 0
load_dotenv()
API_KEY = os.getenv('IND_BOT_TOKEN')

print("Bot has started")

def date(mm,yyyy):
    global trek_no
    url = f"https://booking.indiahikes.com/tms-service/public-api/v1/available-batches/{trek_no}?month={mm}&year={yyyy}"
    response = urlopen(url)
    data = json.loads(response.read())
    if len(data)==0:
        return "NULL"
    tdate = """
START DATE\t\t\t\t\t\t\t\tEND DATE\t\t\t\t\t\t\t\tSLOTS LEFT\n
    """
    
    for i in data :
        sd = str(i["startDate"])
        sd = sd[:sd.index("T")]
        sd_date = sd[2:]
        sddate = datetime.strptime(sd_date,'%y-%m-%d')
        sdmonth = str(calendar.month_name[sddate.month])
        sdday = str(calendar.day_name[sddate.weekday()])
        sdf = f"{sddate.day}-{sdmonth[:3]}-{sddate.year} ({sdday[:3]})"
        ed = str(i["endDate"])
        ed = ed[:ed.index("T")]
        ed_date = ed[2:]
        eddate = datetime.strptime(ed_date,'%y-%m-%d')
        edmonth = str(calendar.month_name[eddate.month])
        edday = str(calendar.day_name[eddate.weekday()])
        edf = f"{eddate.day}-{edmonth[:3]}-{eddate.year} ({edday[:3]})"
        slots = str(i["availableSlots"])
        tdate+= f"{sdf}\t\t\t{edf}\t\t\t{slots}\n"
        trek_no = 0
    return(tdate)


def start(update,context):
    update.message.reply_text(
        """
Use /help command to know about the different commands.
Or just use the Menu button on the left hand corner 
        """
    )
def help(update,context):
    update.message.reply_text(
        """
        /start -> To Begin the adventure
/help -> What command did u just call
/checkdates -> Used to check the availability 
for your trek based on the month and year
/booktrek -> Gives the link to redirect 
you to the indiahikes website
        """

    )

def reply(update,context):
    pattern = "[0-9]?[0-9]\/[0-9][0-9][0-9][0-9]"
    text = str(update.message.text).lower()
    if (re.search(pattern,text)):
        update.message.reply_text("Yes")
        dl = re.findall(pattern,text)
        dlstr = str(dl[0])
        mm = int(dlstr[:dlstr.index("/")])
        yyyy = int(dlstr[dlstr.index("/")+1 : ])
        if(trek_no==0):
            update.message.reply_text("Trek is not selected , Please use /checkdates")
            return
        tdates = date(mm,yyyy)
        if(tdates=="NULL"):
            update.message.reply_text("No dates available for the input month and year , Try again !\n To change treks, use /checkdates ")
            return
        update.message.reply_text(tdates)
    else:
        update.message.reply_text("Cant recognize the input ! Please provide valid input")



def check_dates(update,context):
    global trek_no
    trek_no = 0

    update.message.reply_text(
    """
/DAYARA_BUGYAL_TREK :- 
easy-moderate, 6 days ,level 1
/PHULARA_RIDGE_TREK :- 
easy-moderate, 6 days ,level 3
/DEORIATAL_CHANDRASHILA_TREK :- 
easy-moderate, 6 days ,level 2
/KEDARKANTHA_TREK :- 
easy-moderate, 6 days ,level 2
/KUARI_PASS :- 
easy-moderate, 6 days ,level 3
/BRAHMATAL_TREK :- 
easy-moderate, 6 days ,level 2
/SANDAKPHU_PHALUT_TREK :- 
moderate , 7 days , level 3
/HAR_KI_DUN_TREK :- 
moderate , 8 days , level 3
    """)
    pass

def DAYARA_BUGYAL_TREK(update,context):
    global trek_no
    trek_no =  73
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def PHULARA_RIDGE_TREK(update,context):
    global trek_no
    trek_no =  72
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def DEORIATAL_CHANDRASHILA_TREK(update,context):
    global trek_no
    trek_no =  32
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def KEDARKANTHA_TREK(update,context):
    global trek_no
    trek_no =  8
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def KUARI_PASS(update,context):
    global trek_no
    trek_no =  21
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def BRAHMATAL_TREK(update,context):
    global trek_no
    trek_no =  37
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def SANDAKPHU_PHALUT_TREK(update,context):
    global trek_no
    trek_no =  17
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")

def HAR_KI_DUN_TREK(update,context):
    global trek_no
    trek_no =  94
    update.message.reply_text("Enter the Month and year for the trek in mm/yyyy format")



def book_trek(update,context):
    pass

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(CommandHandler("checkdates",check_dates))
    dp.add_handler(CommandHandler("booktrek",book_trek))

    dp.add_handler(CommandHandler("DAYARA_BUGYAL_TREK",DAYARA_BUGYAL_TREK))
    dp.add_handler(CommandHandler("PHULARA_RIDGE_TREK",PHULARA_RIDGE_TREK))
    dp.add_handler(CommandHandler("DEORIATAL_CHANDRASHILA_TREK",DEORIATAL_CHANDRASHILA_TREK))
    dp.add_handler(CommandHandler("KEDARKANTHA_TREK",KEDARKANTHA_TREK))
    dp.add_handler(CommandHandler("KUARI_PASS",KUARI_PASS))
    dp.add_handler(CommandHandler("BRAHMATAL_TREK",BRAHMATAL_TREK))
    dp.add_handler(CommandHandler("SANDAKPHU_PHALUT_TREK",SANDAKPHU_PHALUT_TREK))
    dp.add_handler(CommandHandler("HAR_KI_DUN_TREK",HAR_KI_DUN_TREK))



    dp.add_handler(MessageHandler(Filters.text, reply))

    #dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()

