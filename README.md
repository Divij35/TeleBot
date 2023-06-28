# Telegram scheduler bot

## Description

This is a personal assistant bot that helps you manage your daily schedule and set reminders for activities using the Telegram messaging platform. The bot allows you to view your schedule for the day and set reminders for specific activities at specific times.

## Features

* Schedule Display: The bot can show you the schedule for the day, providing a list of activities and their corresponding time slots.
* Reminders: You can set reminders for activities by specifying the activity and the time. The bot will send you a reminder message before the specified time to help you stay organized.
* Command List: The bot provides a list of available commands to help you navigate its functionalities.

## Getting Started

To use the personal assistant bot, follow these steps:
1. Install the necessary dependencies listed in the requirements.txt file.
2. Create a Telegram bot and obtain the API token.
3. Set the API token as an environment variable (e.g., using a .env file).
4. Run the bot script to start the bot.

## Installation

+ Clone the repository.
> https://github.com/Divij35/TeleBot.git

  + Create a virtual environment using Python (If you don't want to create a virtual environment you can skip these step):
      > python -m virtualenv myenv
    ### if this doesn't work try:
      > python -m venv myenv
+ Activate the virtual environment:
For linux/mac:
> source myenv/bin/activate

For windows:
> myenv\Scripts\activate.bat

+ Install the dependenices:
> pip install -r requirement.txt
  
## Usage

Once the bot is running, you can interact with it through the following commands:
+ /start: Start the bot and get a welcome message.
+ /help: Get a list of available commands and their descriptions.
+ /show: Display the schedule for the day.
+ /reminder [activity] [time]: Set a reminder for a specific activity at a specific time.

## Dependencies

+ python-telegram-bot: A Python wrapper for the Telegram Bot API.
+ python-dotenv: A Python library to manage environment variables.

## Runtime Configuration
This project uses python-3.10 as the python-telegram-bot dependencies isn't working in python-3.11.To ensure the correct Python version is used, a runtime.txt file has been included in the repository. The contents of the runtime.txt file specify the Python version as python-3.10. It is recommended to set up your Python environment using this version to avoid any compatibility issues.
**Make sure you have Python 3.10 installed before proceeding with the installation steps mentioned above.**
