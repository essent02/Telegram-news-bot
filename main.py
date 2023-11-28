from aiogram import executor
import asyncio

from src.config import bot, dp, CHAT_ID, TOPIC_ID
from src.classes import NEWS
from src.db import DATABASE

# Define an asynchronous function named 'start', which takes 'message' as an argument.
async def start(message):
    # Send a reply to the received message asynchronously.
    await message.answer(
        "Welcome! 👋 I'm Telegram News Bot. Stay updated with the latest news about Telegram right here. "
        "If you have any questions or need help, feel free to reach out to me at @essent_02!"
    )


# Define an asynchronous function named 'startup', which takes 'dp' as an argument.
async def startup(dp):
    # Start an infinite loop.
    while True:
        # Create an instance of NEWS class.
        news = NEWS()

        # Create an instance of DATABASE class.
        db_tools = DATABASE()

        # Asynchronously get data from the news.
        data = await news.get_async()

        # Asynchronously select a URL from the database.
        select_url = await db_tools.select(data[3])

        # If the URL is not found in the database:
        if not select_url:
            # Asynchronously insert the URL into the database.
            await db_tools.insert(data[3])

            # Asynchronously download a photo associated with the news.
            photo = await news.download_photo(data[-1])
            
            # Send a photo to a specified chat with a formatted caption containing news details.
            await bot.send_photo(
                chat_id=CHAT_ID, 
                message_thread_id=TOPIC_ID, 
                photo=photo, 
                caption=f"<b><a href='{data[3]}'>{data[0]}</a></b>\n\n{data[1]}\n<i>{data[2]}</i>", 
                parse_mode="HTML"
            )

        # Wait for an hour before repeating the loop.
        await asyncio.sleep(60 * 60)

# This if statement checks if this script is the main program and is not being imported as a module in another script.
if __name__ == "__main__":
    # Start the aiogram bot's polling. This is how the bot listens for new messages.
    executor.start_polling(
        dp,                       # Pass the Dispatcher object 'dp' to handle incoming updates.
        skip_updates=True,        # Skip any pending updates at startup to avoid processing old messages.
        on_startup=startup        # Assign the 'startup' function to be called when the bot starts.
    )