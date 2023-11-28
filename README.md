# Telegram News Bot

## Overview

This Telegram bot is designed to send you the latest news from Telegram's official blog. It's a great way to stay updated with what's new and happening in the world of Telegram.

## Getting Started
### Prerequisites

Before setting up the bot, make sure you have the following:

- Python 3.6 or higher
- 'pip' for installing Python packages

### Installation
1. *Clone the Repository*
```bash
git clone https://github.com/essent02/Telegram-news-bot.git
cd Telegram-news-bot
```
2. *Install Dependencies*
Install the required Python packages:
```bash
pip install -r requirements.txt
```
3. *Environment Setup*
Create a .env file in the root directory of the project:
#### Linux
```bash
touch .env
```
#### Windows
```bash
New-Item .env
```
Inside the .env file, add the following line:
```makefile
API_TOKEN="your_telegram_bot_api_token"
```
Replace your_telegram_bot_api_token with the actual API token you received from BotFather on Telegram.
3. *Configuration*
- Navigate to the src folder.
- Open or create a file named config.py.
- Inside config.py, set your Telegram chat ID as CHAT_ID. This is where the bot will send news updates. Example:
```python
CHAT_ID = your_chat_id
```
- Optionally, you can also set TOPIC_ID if you need to specify a message thread ID. Example:
```python
TOPIC_ID = your_topic_id
```

## Running the Bot
To start the bot, run the following command in the project's root directory:
```bash
python main.py
```
Enjoy staying up-to-date with the latest Telegram news!
