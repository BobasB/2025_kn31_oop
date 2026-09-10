import logging
from dotenv import load_dotenv
import os

from sqlalchemy import update
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger("Telegram Bot")


# Session and Runner
async def setup_session_and_runner(app_name: str, user_id: str, session_id: str):
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service)
    return session, runner

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    logger.info(f"Користувач {user.username} розпочав діалог.")
    await update.message.reply_html(
        rf"Привіт студенте {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def ai_message_responce(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    user_message = str(update.message.text)
    user_name = str(update.message.from_user.username)
    session_id = str(update.message.chat_id)
    logger.info(f"Отримано повідомлення від користувача {user_name}: {user_message}")
    session, runner = await setup_session_and_runner(app_name="Telegram Bot", user_id=user_name, session_id=session_id)
    
    content = types.Content(role='user', parts=[types.Part(text=f"Користувач {user_name}.\n"), types.Part(text=user_message)])
    # Тут можна додати логіку для обробки повідомлення та формування відповіді
    events = runner.run_async(user_id=user_name, session_id=session_id, new_message=content)

    async for event in events:
        if event.is_final_response():   
            final_response = event.content.parts[0].text   
            logger.info("Відповідь: %s", final_response)
            await update.message.reply_text(final_response)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    logger.info("Запуск бота...")
    application = Application.builder().token(os.getenv("TOKEN")).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_message_responce))

    # Run the bot until the user presses Ctrl-C
    logger.info("Бот запущено. Очікую на повідомлення...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()