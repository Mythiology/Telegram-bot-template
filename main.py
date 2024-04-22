import telebot
from telebot import types

# Tying up the .env file to this python file
from dotenv import load_dotenv 
import os
load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# Define the main menu markup
main_menu_markup = types.InlineKeyboardMarkup(row_width=1)
function1_button = types.InlineKeyboardButton("Function 1", callback_data='function1')
function2_button = types.InlineKeyboardButton("Function 2", callback_data='function2')
function3_button = types.InlineKeyboardButton("Function 3", callback_data='function3')
main_menu_markup.add(function1_button, function2_button, function3_button)

# Define the callback query handler
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'function1': # customize ur functions here
        function1_handler(call)
    elif call.data == 'function2':
        function2_handler(call)
    elif call.data == 'function3':
        function3_handler(call)

# Function to handle Function 1
def function1_handler(call):
    bot.send_message(call.message.chat.id, "You selected Function 1 but if you need another function to do a followup message.")
    # Set the user state to indicate that they are in Function 1 mode
    bot.register_next_step_handler(call.message, follow_up)

def follow_up(call):
    bot.send_message(call.message.chat.id, "Just do this!")

# Function to handle Function 2
def function2_handler(call):
    bot.send_message(call.message.chat.id, "You selected Function 2.")

# Function to handle Function 3
def function3_handler(call):
    bot.send_message(call.message.chat.id, "You selected Function 3.")

# Define the command handler for /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the bot. Please select a function:", reply_markup=main_menu_markup)

# Start the bot
bot.polling()
