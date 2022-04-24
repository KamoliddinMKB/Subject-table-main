from telegram.ext import Updater,MessageHandler,ConversationHandler,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram.update import Update
import tokenfile
updater:Updater=Updater(token=tokenfile.token1())
dispatcher=updater.dispatcher
def ch_mon(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /monday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/monday Birinchi_dars\nIkkinchi_dars\nUchinchi_dars\n...\nOltinchi_dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_tu(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /tuesday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/tuesday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_w(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /wednesday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/wedday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_th(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /thursday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/thursday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_f(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /friday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/friday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE

def ch_s(update:Update,context:CallbackContext):
    update.message.reply_text("Darslarni /saturday buyrug'idan so'ng qatorma qator raqamlamasdan kiriting!!!\nMasalan:\n/saturday Birinchi dars\nIkkinchi dars\nUchinchi dars\n...\nOltinchi dars",reply_markup=ReplyKeyboardMarkup([[KeyboardButton("Admin panelning bosh sahifasiga o'tish"),KeyboardButton("Menyu panelga qaytish")]], resize_keyboard=True))
    return CHANGE_STATE