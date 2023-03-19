schedule = {
    "Monday": {
        "3:30-4:30 PM": "Study Subject 1 (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Workout (1 hour)",
        "6:00-7:00 PM": "Watch YouTube (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 2 (1 hour)",
    },
    "Tuesday": {
        "3:30-4:30 PM": "Watch YouTube (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Study Subject 3 (1 hour)",
        "6:00-7:00 PM": "Workout (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 4 (1 hour)",
    },
    "Wednesday": {
        "3:30-4:30 PM": "Workout (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Study Subject 1 (1 hour)",
        "6:00-7:00 PM": "Watch YouTube (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 2 (1 hour)",
    },
    "Thursday": {
        "3:30-4:30 PM": "Study Subject 3 (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Watch YouTube (1 hour)",
        "6:00-7:00 PM": "Workout (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 4 (1 hour)",
    },
    "Friday": {
        "3:30-4:30 PM": "Workout (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Study Subject 1 (1 hour)",
        "6:00-7:00 PM": "Watch YouTube (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 3 (1 hour)",
    },
    "Saturday": {
        "3:30-4:30 PM": "Study Subject 2 (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Watch YouTube (1 hour)",
        "6:00-7:00 PM": "Workout (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 4 (1 hour)",
    },
    "Sunday": {
        "3:30-4:30 PM": "Workout (1 hour)",
        "4:30-5:00 PM": "Meditation (30 minutes)",
        "5:00-6:00 PM": "Study Subject 1 (1 hour)",
        "6:00-7:00 PM": "Watch YouTube (1 hour)",
        "7:00-7:15 PM": "Break (15 minutes)",
        "7:15-7:45 PM": "Play Video Games (30 minutes)",
        "7:45-8:45 PM": "Study Subject 3 (1 hour)",
    },
}


import datetime
import time
import telegram
import os
import threading

# Set up the command handlers
from telegram.ext import CommandHandler, Updater

from dotenv import load_dotenv
load_dotenv()

bot = telegram.Bot(token=os.getenv("BOT_TOKEN"))
updater = Updater(os.getenv("BOT_TOKEN"), use_context=True, request_kwargs={'timeout': 60})

def send_reminder(activity, start_time):
    now = datetime.datetime.now()
    start = datetime.datetime.strptime(start_time, "%I:%M %p")
    delta = start - now
    if delta.seconds <= 1800:  # send reminder 30 minutes before activity
        message = f"Don't forget to {activity} in 30 minutes!"
        print(message)

# Define commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm your personal assistant bot. You can set reminders for your daily activities using the /reminder command.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="To set a reminder, use the /reminder command followed by the activity and the time in the format HH:MM AM/PM. For example: /reminder Workout 3:30 PM")

def reminder(update, context):
    try:
        # get the activity and time from the message
        message = update.message.text.split()
        activity = message[1]
        time = message[2] + ' ' + message[3]

        # set the reminder and send confirmation message
        send_reminder(activity, time)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Reminder set: {activity} at {time}")
    except:
        # handle invalid command
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid command. Please use the format /reminder [activity] [time]. For example: /reminder Workout 3:30 PM")

# def show_schedule(update, context):
#     message = "Here's your schedule for the week:\n\n"
#     for day, tasks in schedule.items():
#         message += f"<b>{day}:</b>\n"
#         for time, task in tasks.items():
#             message += f"{time} - {task}\n"
#         message += "\n"
#     context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode="HTML")

def show(update, context):
    # get today's schedule
    today = datetime.datetime.now().strftime("%A")
    schedule_today = schedule.get(today)

    # check if schedule for today exists
    if schedule_today:
        # construct message
        message = f"Here is your schedule for {today}:\n\n"
        for key, value in schedule_today.items():
            message += f"{key}: {value}\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="There is no schedule for today.")



start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
reminder_handler = CommandHandler('reminder', reminder)
show_schedule = CommandHandler('show', show)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(reminder_handler)
dispatcher.add_handler(show_schedule)

commands = [
    ('start', 'Start the bot'),
    ('help', 'Get help'),
    ('show', 'Show the schedule'),
    ('reminder', 'Add a reminder '),
]
bot.set_my_commands(commands)

# Start the bot
updater.start_polling()

updater.idle()