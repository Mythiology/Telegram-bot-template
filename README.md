## About

This is a tutorial of a template of a simple telegram bot that includes a menu function. 
Feel free to edit and clone to repo if u need.

## Cloning the repo/downloading repo
```
$ git clonegithub.com/Mythiology/Telegram-bot-template.git
```

## Downloading the neccessary modules
```
$ pip install requirements.txt
```

## Warnings!

It's important to also check your version of Python since the `pyTelegramBotAPI` is only available to `python 3.10` and above. From my experience working with `pyTelegramBotAPI`, try to use the version `4.16.1` as it is less buggy compared to the newer versions which causes some functions to fail unexpectedly.

## Rundown of pyTelegramBotAPI functions

The most important functions or rather the more commonly used functions are:
1) [callback_query_handler](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.callback_query_handler): allows us to be able to utilize the menu function by assigning a callback value to each button of the menu.
2) [register_next_step_handler](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.register_callback_query_handler): allows us to register the next python function that will be run **AFTER** the user sends a message to the bot.
3) [message_handler](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.message_handler): allows our bot to look out for any function keywords that the user sends. Example: In the script, there is a `command = ['start']`, you can further add on keywords to the list so that the bot is able to recognize the keywords and associate them with a function.
4) [polling](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.polling): allows our bot to keep on running so that we are able to continously select an option from the menu
5) There is a significiant difference between `call` and `message`. To put it simply, `message` is a subset of `call` and they both are in dictionary format, so if you want to call any value, you can simply write `call.message.chat.id` etc but never `message.call`.
6) If you wish to host this bot online permanently, please take note that [polling](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.polling) is susceptible to api failures from the telegram API server side. Do use [infinity_polling](https://pytba.readthedocs.io/en/latest/sync_version/index.html#telebot.TeleBot.infinity_polling), which allows the telegram bot to ignore the api failures and restart itself

## Additional Info
Should you need any other information, do refer to the [documentation](https://pytba.readthedocs.io/en/latest/)
