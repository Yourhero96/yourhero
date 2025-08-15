# Telegram Bot (aiogram 3)

Минимальный каркас Telegram-бота на Python с `aiogram 3`.

## Быстрый старт

1. Установите Python 3.10+.
2. Создайте виртуальное окружение и установите зависимости:

```bash
python3 -m venv .venv
./.venv/bin/pip install -U pip
./.venv/bin/pip install -r requirements.txt
```

3. Скопируйте файл `.env.example` в `.env` и вставьте токен вашего бота:

```bash
cp .env.example .env
# отредактируйте .env и укажите BOT_TOKEN
```

4. Запустите бота (long polling):

```bash
./.venv/bin/python bot.py
```

Бот ответит на команды `/start`, `/help` и будет эхо-ответом на текстовые сообщения.

## Полезно
- Переменная окружения: `BOT_TOKEN`.
- Зависимости: `aiogram 3`, `python-dotenv`.
- Для развёртывания через webhook потребуется дополнительная настройка (NGINX/https) — при необходимости добавим.