import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()


def get_bot_token() -> str:
	"""Return BOT_TOKEN from env or raise an explicit error if missing."""
	token = os.environ.get("BOT_TOKEN", "").strip()
	if not token:
		raise RuntimeError(
			"Environment variable BOT_TOKEN is not set. Create .env with BOT_TOKEN=<token> or export it before running."
		)
	return token


dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def handle_start(message: Message) -> None:
	await message.answer(
		"Привет! Я каркас Telegram-бота на aiogram 3.\n"
		"Доступные команды: /start, /help."
	)


@dispatcher.message(Command("help"))
async def handle_help(message: Message) -> None:
	await message.answer(
		"Подсказка:\n"
		"- Установите зависимости из requirements.txt\n"
		"- Создайте файл .env с BOT_TOKEN=...\n"
		"- Запустите: python bot.py"
	)


@dispatcher.message(F.text)
async def handle_echo(message: Message) -> None:
	await message.answer(message.text)


async def main() -> None:
	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
	)
	bot = Bot(
		token=get_bot_token(),
		default=DefaultBotProperties(parse_mode=ParseMode.HTML),
	)
	await dispatcher.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())