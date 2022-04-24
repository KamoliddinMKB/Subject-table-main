from telegram.ext import Updater,MessageHandler,ConversationHandler,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram.update import Update
import tokenfile
updater:Updater=Updater(token=tokenfile.token1())
dispatcher=updater.dispatcher
def mon(update:Update,context:CallbackContext):
    with open('dush.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr)==4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr)==3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr)==2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr)==5:
            a = satr[0]
            update.message.reply_text(f"Dushanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def tue(update:Update,context:CallbackContext):
    with open('sesh.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr)==4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr)==3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr)==2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr)==5:
            a = satr[0]
            update.message.reply_text(f"Seshanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def wed(update:Update,context:CallbackContext):
    with open('chor.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Chorshanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def thu(update:Update,context:CallbackContext):
    with open('pay.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Payshanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def fri(update:Update,context:CallbackContext):
    with open('juma.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Juma kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")

def sat(update:Update,context:CallbackContext):
    with open('shan.txt', 'r') as fayl:
        satr=fayl.readlines()
        if len(satr)==6:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            f = satr[5]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}6.{f}")
        elif len(satr)==5:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            e = satr[4]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}5.{e}")
        elif len(satr) == 4:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            d = satr[3]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}4.{d}")
        elif len(satr) == 3:
            a = satr[0]
            b = satr[1]
            c = satr[2]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}3.{c}")
        elif len(satr) == 2:
            a = satr[0]
            b = satr[1]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}2.{b}")
        elif len(satr) == 5:
            a = satr[0]
            update.message.reply_text(f"Shanba kungi darslar jadvali:\n1.{a}")
        else:
            update.message.reply_text(f"""Xatolik!!! Darslar kiritilmagan!!!""")