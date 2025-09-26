# Telegram Download Bot

A Telegram bot that searches your uploaded Neobox videos and returns streaming + download links.

## Setup

1. Copy `.env.example` → rename to `.env`
2. Put your bot token inside `.env`
3. Add your videos inside `videos.json`

## Run Locally
```bash
pip install -r requirements.txt
python telegram_neobox_bot.py
```

## Deploy on Render.com / Railway.app
- Connect your GitHub repo
- Set `TELEGRAM_TOKEN` in Environment Variables
- Start Command:
```bash
python hck_dwnl_bot.py
```
