from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file.

# Retrieve the API token for the Telegram bot from environment variables.
API_TOKEN = getenv("API_TOKEN")
bot = Bot(API_TOKEN)  # Create an instance of the Bot class with the API token.
dp = Dispatcher(bot)  # Create an instance of the Dispatcher class with the bot.

# Set the CHAT_ID to a specific value. This should be replaced with the user's own chat ID.
CHAT_ID = None
# Set the TOPIC_ID to a specific value. This is optional and can be changed as needed.
TOPIC_ID = None